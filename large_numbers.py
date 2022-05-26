import random
import time

bits = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

for size in bits:
    print(f'{size}: {2**size}')

for size in bits:
    key = hex(random.getrandbits(size))

    st = time.time()
    guess = hex(random.getrandbits(size))
    while key != guess:
        guess = hex(random.getrandbits(size))
    print(f'size: {size}, time: {(time.time() - st) * 1000} ms, key: {key}')

