from threading import *
from time import sleep
class Hello(Thread):

    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)

class Hi(Thread):

    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

s1 = Hello()
s2 = Hi()

s1.start()
sleep(0.2)
s2.start()

s1.join()
s2.join()

print("Bye")