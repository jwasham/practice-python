import random
import threading
import time


def synchronize(func):
    def lock_resource(*args, **kwargs):
        global lock
        lock.acquire()

        try:
            func(*args, **kwargs)
        finally:
            lock.release()

    return lock_resource


@synchronize
def count_up(num):

    global database

    time.sleep(random.randrange(3))
    database.append(num)


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
