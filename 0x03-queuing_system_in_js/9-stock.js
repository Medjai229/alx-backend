import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

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

// Array of the products
const listProducts = [
  {
    id: 1, name: 'Suitcase 250', price: 50, stock: 4,
  },
  {
    id: 2, name: 'Suitcase 450', price: 100, stock: 10,
  },
  {
    id: 3, name: 'Suitcase 650', price: 350, stock: 2,
  },
  {
    id: 4, name: 'Suitcase 1050', price: 550, stock: 5,
  },
];

// Retrieve an item by its id
function getItemById(id) {
  return listProducts.find((product) => product.id === id);
}

// Set the item id to the remaining available stock
function reserveStockById(itemId, stock) {
  client.set(`item.${itemId}`, stock);
}

// Get the stored reserved stock
async function getCurrentReservedStockById(itemId) {
  const getAsync = promisify(client.get).bind(client);
  const stock = await getAsync(`item.${itemId}`);
  return parseInt(stock, 10);
}

// Server route to list all the products
app.get('/list_products', (req, res) => {
  const formattedProducts = listProducts.map((product) => ({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
  }));
  res.json(formattedProducts);
});

// Server route to list product details by itemId
app.get('/list_products/:itemId', async (req, res) => {
  const { itemId } = req.params;
  const productId = parseInt(itemId, 10);

  const product = getItemById(productId);

  if (!product) {
    return res.status(404).json({ status: 'Product not found' });
  }

  const currentQuantity = await getCurrentReservedStockById(productId);

  return res.json({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
    currentQuantity,
  });
});

// Server route to reserver a product
app.get('/reserve_product/:itemId', async (req, res) => {
  const { itemId } = req.params;
  const productId = parseInt(itemId, 10);

  const product = getItemById(productId);

  if (!product) {
    return res.status(404).json({ status: 'Product not found' });
  }

  const currentQuantity = await getCurrentReservedStockById(productId);

  if (currentQuantity >= product.stock) {
    return res.status(400).json({
      status: 'Not enough stock available',
      itemId: productId,
    });
  }

  reserveStockById(productId, currentQuantity + 1);
  return res.json({
    status: 'Reservation confirmed',
    itemId: productId,
  });
});

// Running the server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
