import express from 'express'
import { resolve } from 'path'
import { MongoClient } from 'mongodb'
import { api } from './api'
import { apiDmGET } from './api/dm'

const app = express()
const port = 3000

// Connect to MongoDB.
const client = new MongoClient('mongodb://localhost:27017')
client.connect().then(() => {
  console.log('Connected to MongoDB successfully!')
  // Get database.
  const db = client.db('ezchat')
  // Assign API endpoints.
  app.get('/api', api)
  app.get('/api/dm', apiDmGET(db))
  // Disabled endpoints.
  // app.get('/api/guild', apiGuildGet(db))
  // app.get('/api/channel', apiChannelGET(db))
}).catch(console.error.bind('Failed to initialize API!'))

// Primary endpoints.
app.get('/', (req, res) => res.sendFile(resolve('src/index.html')))
app.get('/playground', (req, res) => res.sendFile(resolve('src/playground.html')))

app.listen(port, () => console.log(`Server listening on port ${port}!`))
