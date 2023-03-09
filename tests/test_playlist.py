from utils.yt_playlist import Playlist
import datetime
import pytest

def test_pl_name():
    pl = Playlist('PLZfhqd1-Hl3C5AQ6LPcMsVBIpduqckjPB')
    assert pl.title == 'Уэс и Флинн'

def test_pl_url():
    pl = Playlist('PLZfhqd1-Hl3C5AQ6LPcMsVBIpduqckjPB')
    assert pl.link == 'https://www.youtube.com/playlist?list=PLZfhqd1-Hl3C5AQ6LPcMsVBIpduqckjPB'

def test_duration():
    pl = Playlist('PLZfhqd1-Hl3C5AQ6LPcMsVBIpduqckjPB')
    assert pl.all_duration == datetime.timedelta(seconds=27377)

def test_duration_in_seconds():
    pl = Playlist('PLZfhqd1-Hl3C5AQ6LPcMsVBIpduqckjPB')
    duration = pl.all_duration
    assert duration.total_seconds() == 27377.0

def test_link_best_video():
    pl = Playlist('PLZfhqd1-Hl3C5AQ6LPcMsVBIpduqckjPB')
    assert pl.best_video() == 'https://www.youtube.com/watch?v=49WfzoqBzC4'