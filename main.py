import hashlib
import random
import string
import time

class Timer:
    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    def end(self):
        if self.start_time is None:
            raise ValueError("Timer has not been started.")
        return time.time() - self.start_time

    def has_time_elapsed(self, timeout):
        if self.start_time is None:
            raise ValueError("Timer has not been started.")
        return (time.time() - self.start_time) >= timeout

def p(t, r) -> str:
    return t[:r] == "0" * r

def ArkosePOW(seed, leadingZeroCount, timeout):
    iterationCount: int = 0

    timer = Timer()
    timer.start()

    while True:
        random_string: str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=15))
        hash_str = hashlib.sha512((seed + random_string).encode('utf-8')).hexdigest()
        iterationCount +=1

        if p(hash_str, leadingZeroCount):
            executionTime = timer.end()
            hashRate = iterationCount / executionTime

            return {
                "iteration_count": iterationCount,
                "result": random_string,
                "hash": hash_str,
                "execution_time": round(executionTime),
                "hash_rate": hashRate
            }
        
        if timer.has_time_elapsed(timeout):
            raise Exception("Timed Out")

if __name__ == "__main__": 
    print(ArkosePOW("tVhnMKUHO6FJX6Qdji", 4, 30000))