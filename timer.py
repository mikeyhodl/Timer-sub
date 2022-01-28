import time
time = time.time()

ts = time

file = open("readme.md", 'w')
file.write("Time x : ")
file.write(str(ts))
file.close()
