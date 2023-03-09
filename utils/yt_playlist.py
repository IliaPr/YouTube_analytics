from datetime import timedelta
import isodate

from utils.mixin_youtube import Mixin_youtube
class Playlist(Mixin_youtube):
    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        youtube = self.get_service()
        self.link = f'https://www.youtube.com/playlist?list=' + playlist_id
        self.playlist = youtube.playlists().list(id=playlist_id, part='snippet').execute()
        self.playlist_videos = youtube.playlistItems().list(playlistId=playlist_id, part='contentDetails', maxResults=50, ).execute()
        self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        self.video_response = youtube.videos().list(part='contentDetails,statistics', id=','.join(self.video_ids)).execute()
        self.title = self.playlist['items'][0]['snippet']['title']

    @property
    def all_duration(self):
        all_duration = timedelta()
        for video in self.video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            all_duration += duration
        return all_duration

    def best_video(self):
        '''Получение ссылки на лучшее по количеству лайков видео в плейлисте'''
        biggest_likes_amt = 0
        for i in self.video_response['items']:
            if int(i['statistics']['likeCount']) > biggest_likes_amt:
                biggest_likes_amt = int(i['statistics']['likeCount'])
        for i in self.video_response['items']:
            if i['statistics']['likeCount'] == str(biggest_likes_amt):
                return f"https://www.youtube.com/watch?v={i['id']}"

if __name__ == '__main__':
    pl = Playlist('PLZfhqd1-Hl3C5AQ6LPcMsVBIpduqckjPB')
    print(pl.title)
    duration = pl.all_duration
    print(duration)
    print(duration.total_seconds())
    print(pl.link)
    print(pl.best_video())
