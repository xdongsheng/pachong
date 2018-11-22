import threading
import random
import time

gMoney = 1000
gCondition = threading.Condition()
gTotalTimes = 10
gTimes = 0


class Producer(threading.Thread):
    def run(self):
        global gMoney
        global gTimes
        while True:
            money = random.randint(100,1000)
            gCondition.acquire()
            if gTimes >=gTotalTimes:
                gCondition.release()
                break
            gMoney = gMoney+money
            print('%s生产了%d元钱，剩余%d元钱'%(threading.current_thread(),money,gMoney))
            gTimes +=1
            gCondition.notify_all()
            gCondition.release()
            time.sleep(1)



class Consumer(threading.Thread):
    def run(self):
        while True:
            global gMoney
            global gTimes
            money = random.randint(100,1000)
            gCondition.acquire()
            # 注意这个是while循环
            while gMoney < money:
                if gTimes >= gTotalTimes:
                    gCondition.release()
                    return
                print('%s准备消费%d元钱，剩余%d元钱，不足！'%(threading.current_thread(),money,gMoney))
                gCondition.wait()
            gMoney -= money
            print('%s消费了%d元钱，剩余%d元钱'%(threading.current_thread(),money,gMoney))

            gCondition.release()
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