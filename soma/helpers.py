from datetime import datetime
from random import choice, choices
import hashlib


def datetime_to_timestamp(dt) -> int:
    return int(round(dt.timestamp()))

def timestamp_to_datetime(s: int):
    return datetime.fromtimestamp(s)

def status_display(status: int):
    if status == 1:
        return '已启用'
    elif status == 0:
        return '已禁用'
    else:
        return '未知'

def generate_api_key(url: str, salt=None, salt_length=8) -> str:
    if salt is None:
        population = list('abcdefghijklmnopqrstuvwxyz1234567890')
        salt = ''.join(choices(population, k=salt_length))
    timestamp = str(datetime_to_timestamp(datetime.now()))
    params = [
        url,
        timestamp,
        salt,
    ]
    
    method = choice(['sha256', 'md5'])
    hash_func = hashlib.new(method) # 选择哈希算法
    hash_func.update(''.join(params).encode())
    return hash_func.hexdigest()[:32]

# 单笔收款最小金额限制
def limit_onemin(total: float, limitation: int) -> bool:
    if limitation == 0:
        return True
    else:
        return total >= limitation

# 单笔收款最大金额限制
def limit_onemax(total: float, limitation: int) -> bool:
    if limitation == 0:
        return True
    else:
        return total <= limitation

# 收款笔数限制
def limit_num(curnum: int, limitation: int) -> bool:
    if limitation == 0:
        return True
    else:
        return curnum < limitation

# 收款金额限制
def limit_money(total: float, limitation: float, curmoney: float) -> bool:
    if limitation == 0:
        return True
    else:
        return total <= limitation - curmoney