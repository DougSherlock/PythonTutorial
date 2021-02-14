import threading
import concurrent.futures
import time


start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return('Done sleeping')

def do_something_return(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done sleeping {seconds} second(s)...'


# threading using a thread pool - map function (waits for all threads to complete before returning results)
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something_return, secs)
    for f in concurrent.futures.as_completed(results):
        print(f.result())


# threading using a thread pool - iterate results
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     secs = [5, 4, 3, 2, 1]
#     results = [executor.submit(do_something_return, sec) for sec in secs]
#     for f in concurrent.futures.as_completed(results):
#         print(f.result())

# threading in a loop
# threads = []
# for _ in range(10):
#     t = threading.Thread(target=do_something, args=[1.5])
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()

# threading without a loop
# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)
# t1.start()
# t2.start()
# t1.join()
# t2.join()

# non-threaded
# do_something()
# do_something()

finish = time.perf_counter()


print(f'Finished in {round(finish-start, 2)} second(s)')