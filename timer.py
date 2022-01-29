import time

localtime = time.asctime( time.localtime(time.time()) )

execTime = localtime

file = open("readme.md", 'w')
file.write("Executed code Time: ")
file.write(str(execTime))
file.close()
