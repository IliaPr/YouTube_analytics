from utils.youtube_api import Channel, Video, PLVideo
import pytest

@pytest.fixture
def channel1():
    channel = Channel('UC7sDT8jZ76VLV1u__krUutA')
    return channel
@pytest.fixture()
def channel2():
    channel = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
    return channel
@pytest.fixture()
def video1():
    video1 = Video('9lO06Zxhu88')
    return video1

@pytest.fixture()
def video2():
    video2 = PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')
    return video2

def test_str(channel1):
    assert str(channel1) == 'Channel: DUST'

def test_gt(channel1, channel2):
    assert channel1.__gt__(channel2) is False

def test_lt(channel1, channel2):
    assert channel1.__lt__(channel2) is True
def test_add(channel1, channel2):
    assert channel1 + channel2 == 13270000

def test_video_info(video1):
    assert video1.__str__() == 'Название видео: Как устроена IT-столица мира / Russian Silicon Valley (English subs)'

def test_plvideo_info(video2):
    assert video2.__str__() == 'Название видео: Пушкин: наше все? / Название плейлиста: Литература'