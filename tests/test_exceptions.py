from utils.youtube_api import Video

def test_wrong_link():
    broken_video = Video('broken_video_id')
    assert broken_video.video_name == None
    assert broken_video.video_data == None
    assert broken_video.video_info == None
    assert broken_video.video_like_count == None
    assert broken_video.video_view_count == None