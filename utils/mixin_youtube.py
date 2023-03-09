import os
from googleapiclient.discovery import build



class Mixin_youtube:
    @classmethod
    def get_service(cls):
        '''создается специальный объект для работы с API'''
        api_key: str = os.getenv('YOUTUBE_API')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube
