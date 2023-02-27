from utils.youtube_api import Channel
import pytest

@pytest.fixture
def channel1():
    channel = Channel('UC7sDT8jZ76VLV1u__krUutA')
    return channel
@pytest.fixture()
def channel2():
    channel = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
    return channel

def test_str(channel1):
    assert str(channel1) == 'Channel: DUST'

def test_gt(channel1, channel2):
    assert channel1.__gt__(channel2) is False

def test_lt(channel1, channel2):
    assert channel1.__lt__(channel2) is True
def test_add(channel1, channel2):
    assert channel1 + channel2 == 13260000