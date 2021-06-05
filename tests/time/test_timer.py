import time
from datetime import timedelta

from more_ds.time.timer import Timer


def test_timer() -> None:  # noqa: D103
    with Timer() as t:
        time.sleep(0.001)  # 1 msec
    assert t.duration >= 1_000_000  # 1 msec expressed as nanoseconds
    assert t.elapsed >= timedelta(microseconds=1_000)  # 1 msec expressed as microseconds
