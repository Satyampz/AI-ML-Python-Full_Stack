import threading
import time

class Job1(threading.Thread):

    #Override
    def run(self):
        print(threading.current_thread().name)
        for i in range(10):
            print("Shruti")
            time.sleep(2)
        print("End of run Method")

print("Start of main method")
print(threading.current_thread().name)

t1=Job1()
t1.start()

for i in range(10):
    print("Harshda")
    time.sleep(2)
print("End of main method")
