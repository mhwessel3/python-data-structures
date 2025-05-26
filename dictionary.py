DEFAULT_HASH_TABLE_SIZE = 4096

class Dictionary:
    """
    Python dunder operator overloading
    Check if d is a built-in object & use overloaded method if possible
    | Method                          | Triggered By       |
    | ------------------------------- | ------------------ |
    | `__getitem__(self, key)`        | `obj[key]`         |
    | `__setitem__(self, key, value)` | `obj[key] = value` |
    | `__delitem__(self, key)`        | `del obj[key]`     |
    | `__len__(self)`                 | `len(obj)`         |
    | `__iter__(self)`                | `for x in obj`     |
    | `__next__(self)`                | `next(obj)`        |
    | `__contains__(self, item)`      | `item in obj`      |
    | `__reversed__(self)`            | `reversed(obj)`    |
    """
    def __init__(self, hash_table_size=DEFAULT_HASH_TABLE_SIZE):
        self.hash_table_size = hash_table_size
        self.hash_table = [None] * hash_table_size

    def get_hash_key(self, key):
        return hash(key) % self.hash_table_size

    def __setitem__(self, key, value):
        idx = self.get_hash_key(key)
        self.hash_table[idx] = (key, value)
        return
    
    def __getitem__(self, key):
        idx = self.get_hash_key(key)
        # get the value from the tuple
        return self.hash_table[idx][1]

    def __delitem__(self, key):
        idx = self.get_hash_key(key)
        self.hash_table[idx] = None

    def __len__(self):
        return sum(1 for item in self.hash_table if item)
                
   
    def __repr__(self):
        ret = '{'
        for item in self.hash_table:
            if item:
                key = item[0]
                val = item[1]
                ret += f'\n  {key}: {val}'
        ret += f"\n" + '}'
        return ret

d = Dictionary()
d["A"] = 15
print(d['A'])

d['m'] = 2398457
del d['m']

# delete something that doesn't exist
del d['k']

print(len(d))

print(d)
