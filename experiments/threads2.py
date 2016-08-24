import random
import threading
import time


def count_up(num):

    global database, lock

    lock.acquire()

    try:
        time.sleep(random.randrange(3))
        database.append(num)
    finally:
        lock.release()


def main():

    global database, lock

    lock = threading.Lock()
    database = []

    threads = []
    for i in range(15):
        threads.append(threading.Thread(target=count_up, args=(i+1,)))
        threads[i].start()

    for th in threads:
        th.join()

    print(database)


if __name__ == '__main__':
    main()
