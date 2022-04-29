import subprocess
from threading import Thread
from time import perf_counter
import random

node_http_api = ["http://172.24.2.1:8001/", "http://172.24.2.2:8002/", "http://172.24.2.3:8003/"]

num_kvpair = 1000
size_value = 81920
num_thread = 2
num_gets = 1000

def setup():
    for index in range(num_kvpair):
        key = str(index)
        value = format(index, "0" + str(size_value) +  "d")
        cmd = ["curl", "-X", "PUT", "-d",  value,  "http://172.24.2.1:8001/" + key]
        result = subprocess.run(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    print("Finish setup DB: PUT " + str(num_kvpair) + " key-value pairs into DB")

setup()

def get_function(nget):
    for _ in range(nget):
        http_api = random.choice(node_http_api)
        key = random.randrange(num_kvpair)
        cmd = ["curl", http_api + str(key)]
        result = subprocess.run(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)

def launch_threads(nt, nget):
    threads = []
    for _ in range(nt):
        t = Thread(target=get_function, args=(nget,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

start_time = perf_counter()
launch_threads(num_thread, num_gets)
end_time = perf_counter()

print(f'It took {end_time- start_time: 0.2f} second(s) to complete. ({num_thread} threads; {num_gets} GET requests/thread)')
