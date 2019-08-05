import { Endpoint } from '../types'

export const apiChannelGET: Endpoint = (db) => async (req, res) => {
  // Verify if the user exists.
  const token = req.headers['token']
  const user = await db.collection('users').findOne({ token })
  if (!user) {
    res.sendStatus(401)
    return
  }
  // Get the channel.
  const id = req.params['channel_id']
  const channel = await db.collection('channels').findOne({ id })
  // Send it.
  channel['_id'] = undefined
  res.send(channel)
}
