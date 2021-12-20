import sys

num = 2147483647

bytes_val = num.to_bytes(4, 'big')
print(sys.getsizeof(num))
print(bytes_val)
print(sys.getsizeof(bytes_val))
print(int.from_bytes(bytes_val, 'big'))