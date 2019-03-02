from pymongo.database import Database


class Channels:
    def __init__(self, db: Database):
        self.channels = db.channels

    def get_channel(self, channel_id: str):
        self.channels.find_one({channel_id: channel_id})
