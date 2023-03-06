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

    def __str__(self):
        '''Метод возврата названия канала'''
        return f'Channel: {self.title}'

    def __gt__(self, other):
        '''Метод сравнения количества подписчиков: если у первого канала - True'''
        return int(self.subscribers) > int(other.subscribers)

    def __lt__(self, other):
        '''Метод сравнения количества подписчиков: если у второго канала - True'''
        return int(self.subscribers) < int(other.subscribers)

    def __add__(self, other):
        '''Метод сложения количества подписчиков'''
        return int(self.subscribers) + int(other.subscribers)

class Video:
    '''Класс статистики видео'''
    def __init__(self, id_video):
        '''Инициализация'''
        self.id_video = id_video
        self.video_data = self.yt_obj().videos().list(id=self.id_video, part='snippet, statistics').execute()
        self.video_info = json.dumps(self.video_data, indent=4)
        self.video_name = self.video_data['items'][0]['snippet']['title']
        self.video_view_count = self.video_data['items'][0]['statistics']['viewCount']
        self.video_like_count = self.video_data['items'][0]['statistics']['likeCount']

    @classmethod
    def yt_obj(cls):
        '''создается специальный объект для работы с API'''
        api_key: str = os.getenv('YOUTUBE_API')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    def __str__(self):
        '''Возврат информации о плейлисте'''
        return f"Название видео: {self.video_name}"


class PLVideo(Video):
    '''Rласс для статистики плейлиста'''
    def __init__(self,id_video, id_playlist):
        '''Инициализация'''
        super().__init__(id_video) #Наследование от класса Video
        self.id_playlist = id_playlist
        self.playlist_data = self.yt_obj().playlists().list(id=self.id_playlist, part='snippet, contentDetails').execute()
        self.playlist_info = json.dumps(self.playlist_data, indent=4)
        self.playlist_name = self.playlist_data['items'][0]['snippet']['title']

    @classmethod
    def yt_obj(cls):
        '''создается специальный объект для работы с API'''
        api_key: str = os.getenv('YOUTUBE_API')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    def __str__(self):
        '''Возврат информации о плейлисте'''
        return f"Название видео: {self.video_name} / Название плейлиста: {self.playlist_name}"



if __name__ == '__main__':
    #Dust = Channel('UC7sDT8jZ76VLV1u__krUutA')
    #print(Dust)
    #print(vdud < Dust)
    #print(vdud > Dust)
    #print(vdud + Dust)
    video1 = Video('9lO06Zxhu88')
    video2 = PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')
    print(video1)
    print(video2)