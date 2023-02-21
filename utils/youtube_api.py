import os
import json
from googleapiclient.discovery import build



class Channel:

    def __init__(self, channel_id):
        self.channel_id = channel_id

    def print_info(self):
        api_key: str = os.getenv('YOUTUBE_API')
        youtube = build('youtube', 'v3', developerKey=api_key)
        self.channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))


vdud = Channel("UC1eFXmJNkjITxPFWTy6RsWg")
vdud.print_info()



