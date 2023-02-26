import os
import json
from googleapiclient.discovery import build

class Channel:
    def __init__(self, channel_id):
        '''Инициализация'''
        self.__id_channel = channel_id
        self.channel_info = self.yt_obj().channels().list(id=channel_id, part='snippet, statistics').execute()
        self.link = f"https://www.youtube.com/channel/{self.__id_channel}"
        self.title = self.channel_info['items'][0]['snippet']['title']
        self.description = self.channel_info['items'][0]['snippet']['description']
        self.subscribers = self.channel_info['items'][0]['statistics']['subscriberCount']
        self.amt_video = self.channel_info['items'][0]['statistics']['videoCount']
        self.amt_views = self.channel_info['items'][0]['statistics']['viewCount']
    @classmethod
    def yt_obj(cls):
        '''создается специальный объект для работы с API'''
        api_key: str = os.getenv('YOUTUBE_API')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    def print_info(self):
        '''создание статистики канала'''
        self.info = json.dumps(self.channel_info, indent=4)
        return self.info

    def save_to_file(self, name_file):
        '''запись статистики в файл'''
        with open(name_file, 'w', encoding='UTF-8') as file:
            json.dump(self.channel_info, file, indent=4, ensure_ascii=False)

#Dust = Channel('UC7sDT8jZ76VLV1u__krUutA')
#print(Channel.yt_obj())
