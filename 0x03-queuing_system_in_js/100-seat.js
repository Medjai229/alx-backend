import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';
import { createQueue } from 'kue';

// Initializing the server
const app = express();
const PORT = 1245;

// Create the redis client
const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

// Initialize the Kue queue
const queue = createQueue();

// Promisify redis get method
const getAsync = promisify(client.get).bind(client);
// Setting the available seats to 50 when the app is launched
client.set('available_seats', 50);
// Indicator if the user can reserve a seat or not
let reservationEnabled = true;

// Function to reserve a seat by setting the number of available seats
function reserveSeat(number) {
  client.set('available_seats', number);
}

// Function to get the current available seats
async function getCurrentAvailableSeats() {
  const seats = await getAsync('available_seats');
  return parseInt(seats, 10);
}

// Server route to get the number of available seats
app.get('/available_seats', async (req, res) => {
  const seats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: seats });
});

// Server route to reserve a seat
app.get('/reserve_seat', async (req, res) => {
  // Check if reservation is enabled
  if (!reservationEnabled) {
    return res.json({ status: 'Reservations are blocked' });
  }

  // Get the current number of available seats
  const seats = await getCurrentAvailableSeats();

  // If no seats are available, block further reservations
  if (seats === 0) {
    reservationEnabled = false;
    return res.json({ status: 'Reservations are blocked' });
  }

  // Create a job to reserve a seat
  const job = queue.create('reserve_seat').save((err) => {
    if (err) {
      return res.json({ status: 'Reservation failed' });
    }
    return res.json({ status: 'Reservation in process' });
  });

  // Handle job completion and ensure it's logged only once
  job.on('complete', async () => {
    console.log(`Seat reservation job ${job.id} completed`);

    // After the job is done, check available seats
    const updatedSeats = await getCurrentAvailableSeats();
    if (updatedSeats === 0) {
      reservationEnabled = false; // Disable further reservations
    }
  });

  // Handle job failure
  job.on('failed', (err) => {
    console.log(`Seat reservation job ${job.id} failed: ${err}`);
  });
});

// Server route to process the queue
app.get('/process', (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    try {
      const seats = await getCurrentAvailableSeats();

      if (seats > 0) {
        // Decrement available seats in the job processing
        await reserveSeat(seats - 1);
        done(); // Mark the job as done
      } else {
        const error = new Error('Not enough seats available');
        done(error); // Fail the job
      }
    } catch (error) {
      done(error); // Fail the job
    }
  });
});

// Running the server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
