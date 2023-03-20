from datetime import datetime


def helper_datetime_to_timestamp(dt) -> int:
    return int(round(dt.timestamp()))

def helper_timestamp_to_datetime(s: int):
    return datetime.fromtimestamp(s)