import time
tim = time.time()
i = 0
while i < 1000000000:
    i += 1
print(time.time() - tim)