BUCKET_SIZE = 100
class HashTable: 
    def __init__(self):
        self.table = [[] for _ in range(BUCKET_SIZE)]
        

t = HashTable()

# Python ORD function returns unicode for a single character
print(ord('a'))
print(ord('A'))
