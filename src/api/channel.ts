import { RequestHandler } from 'express'
import { Db } from 'mongodb'

export const apiChannelGET = (db: Db): RequestHandler => async (req, res) => {
  // Verify if the user exists.
  const token = req.headers['token']
  const user = await db.collection('users').findOne({ token })
  if (!user) {
    res.sendStatus(401)
    return
  }
  // Get the channel.
  // TODO: Properly get REST parameter.
  const id = req.url.split('/').pop()
  const channel = await db.collection('channels').findOne({ id })
  // Send it.
  channel['_id'] = undefined
  res.send(channel)
}
