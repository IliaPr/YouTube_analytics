import os
import json
from googleapiclient.discovery import build



class Channel:

    def __init__(self, channel_id):
        '''Инициализация'''
        self.channel_id = channel_id

    def print_info(self):
        '''Получение информации о канале'''
        api_key: str = os.getenv('YOUTUBE_API')
        youtube = build('youtube', 'v3', developerKey=api_key)
        self.channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))


dust = Channel("UC7sDT8jZ76VLV1u__krUutA")
dust.print_info()



