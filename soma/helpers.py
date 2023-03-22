from datetime import datetime
from random import choice, choices
import hashlib


def helper_datetime_to_timestamp(dt) -> int:
    return int(round(dt.timestamp()))

def helper_timestamp_to_datetime(s: int):
    return datetime.fromtimestamp(s)

def helper_status_display(status: int):
    if status == 1:
        return '已启用'
    elif status == 0:
        return '已禁用'
    else:
        return '未知'

def helper_generate_api_key(url: str, salt=None, salt_length=8) -> str:
    if salt is None:
        population = list('abcdefghijklmnopqrstuvwxyz1234567890')
        salt = ''.join(choices(population, k=salt_length))
    timestamp = str(helper_datetime_to_timestamp(datetime.now()))
    params = [
        url,
        timestamp,
        salt,
    ]
    
    method = choice(['sha256', 'md5'])
    hash_func = hashlib.new(method) # 选择哈希算法
    hash_func.update(''.join(params).encode())
    return hash_func.hexdigest()[:32]


if __name__ == "__main__":
    api_key = helper_generate_api_key("http://www.hello.com")
    print(api_key)