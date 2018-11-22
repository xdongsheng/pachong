import threading

VALUE = 0

glock =threading.Lock()

def add_value():
    global VALUE
    glock.acquire()
    for x in range(1000000):
        VALUE +=1
    glock.release()
    print('Value:%d'%VALUE)
def main():
    for x in range(2):
       t =threading.Thread(target=add_value)
       t.start()

if __name__ == '__main__':
    main()