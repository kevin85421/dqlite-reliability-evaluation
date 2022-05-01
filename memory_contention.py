import subprocess
import time
import sys

# Usage:    python3 memory_contention.py ${master, follower1, follower2} ${memory (MB)}
# Example:  python3 memory_contention.py master 100 

dqlite_node_dict = { "master": "assignment2_raft1_1", "follower1": "assignment2_raft2_1", "follower2": "assignment2_raft3_1"}

def start_cluster():
    subprocess.run(["rm", "-r", "output"], shell=False, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    subprocess.run(["mkdir", "output"], shell=False, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    subprocess.Popen(["docker-compose", "up"], shell=False, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)

def memory_contention(target: str, memory_mb: int):
    time.sleep(2)
    mem = str(memory_mb) + "M" 
    swap = str(5 * memory_mb) + "M"
    subprocess.run(["docker", "update", "--memory", mem, "--memory-swap", swap, dqlite_node_dict[target]])

def close_cluster():
    time.sleep(70)
    subprocess.run(["docker-compose", "down"]) 


start_cluster()
memory_contention(sys.argv[1], int(sys.argv[2]))
close_cluster()
