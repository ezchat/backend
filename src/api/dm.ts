import { RequestHandler } from 'express'
import { Db } from 'mongodb'

export const apiDmGET = (db: Db): RequestHandler => async (req, res) => {
  // Verify if the user exists.
  const token = req.headers['token']
  const user = await db.collection('users').findOne({ token })
  if (!user) {
    res.sendStatus(401)
    return
  }
  // Check if the user is in the DMs.
  const id = req.url.split('/').pop()
  if (!user['direct_messages'] || !user['direct_messages'].includes(id)) {
    res.sendStatus(403)
    return
  }
  // Get the DM.
  const directMessage = await db.collection('direct_messages').findOne({ id })
  if (!directMessage) {
    res.status(410).send('DM channel was deleted!')
    return
  }
  // Send it.
  directMessage['_id'] = undefined
  res.send(directMessage)
}
