class MyHashMap:

    def __init__(self):
        self.bucket_size = 1000
        self.buckets = [[-1] * 1001 for _ in range(1000)]

    def put(self, key: int, value: int) -> None:
        bucket = key % self.bucket_size
        index = key // self.bucket_size
        self.buckets[bucket][index] = value

    def get(self, key: int) -> int:
        bucket = key % self.bucket_size
        index = key // self.bucket_size
        return self.buckets[bucket][index]

    def remove(self, key: int) -> None:
        bucket = key % self.bucket_size
        index = key // self.bucket_size
        self.buckets[bucket][index] = -1