import os

from googleapiclient.discovery import build


# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('YT_API_KEY')
print(api_key)

 #создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)

