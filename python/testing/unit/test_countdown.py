import pytest

from python.iterators.countdown import Countdown


def test_countdown():
    countdown = Countdown(3)

    assert next(countdown) == 3
    assert next(countdown) == 2
    assert next(countdown) == 1
    assert next(countdown) == 0

    with pytest.raises(StopIteration):
        next(countdown)


def test_countdown_zero():
    countdown = Countdown(0)

    assert next(countdown) == 0

    with pytest.raises(StopIteration):
        next(countdown)


def test_countdown_negative():
    countdown = Countdown(-1)

    with pytest.raises(StopIteration):
        next(countdown)


def test_iter_returns_same_object():
    countdown = Countdown(3)

    assert iter(countdown) is countdown
