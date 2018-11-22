import threading
import random
import time

gMoney = 1000
gLock = threading.Lock()
gTotalTimes = 10
gTimes = 0


class Producer(threading.Thread):
    def run(self):
        global gMoney
        global gTimes
        while True:
            money = random.randint(100,1000)
            gLock.acquire()
            if gTimes >=gTotalTimes:
                gLock.release()
                break
            gMoney = gMoney+money
            print('%s生产了%d元钱，剩余%d元钱'%(threading.current_thread(),money,gMoney))
            gTimes +=1
            gLock.release()
            time.sleep(1)



class Consumer(threading.Thread):
    def run(self):
        while True:
            global gMoney
            global gTimes
            money = random.randint(100,1000)
            gLock.acquire()
            if gMoney >= money:
                gMoney -= money
                print('%s消费了%d元钱，剩余%d元钱'%(threading.current_thread(),money,gMoney))
            else:
                # 或者这里直接break
                gTimes = 0
                print('%s消费者准备消费%d元钱，剩余%d元钱，不足！'%(threading.current_thread(),money,gMoney))
            gLock.release()
            time.sleep(0.5)


def main():
    for x in range(5):
        t = Consumer(name="消费者线程%d"%x)
        t.start()
    for x in range(5):
        t = Producer(name="生产者线程%d"%x)
        t.start()


if __name__ == '__main__':
    main()