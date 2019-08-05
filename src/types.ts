import { Db } from 'mongodb'
import { RequestHandler } from 'express'

export type Endpoint = (db: Db) => RequestHandler
