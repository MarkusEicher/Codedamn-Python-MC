import time
import multiprocessing
# A CPU heavy calculation, just
# as an example. This can be
# anything you like
def heavy(n, myid):
    for x in range(1, n):
        for y in range(1, n):
            x**y
    print(myid, x, y, "is done")
def multiproc(n):
    processes = []
    for i in range(n):
        p = multiprocessing.Process(target=heavy, args=(500,i,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()
if __name__ == "__main__":
    start = time.time()
    multiproc(80)
    end = time.time()
    print("Took: ", end - start)