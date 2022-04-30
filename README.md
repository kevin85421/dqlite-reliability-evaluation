# dqlite
* canonical/raft: https://github.com/canonical/raft
* canonical/dqlite: https://github.com/canonical/dqlite
* canonical/go-dqlite: https://github.com/canonical/go-dqlite

**canonical/dqlite** is a C library that implements an embeddable and replicated SQL database engine with high-availability and automatic failover based on **canonical/raft**.
In addition, **canonical/go-dqlite** is a pure-Go client for the dqlite wire protocol.

# Repo structure
* **Dockerfile:** File to build dqlite docker image.
* **docker-compose.yml:** Setup a 3-node dqlite clusters.
* **go-dqlite-master:** The directory is the source code of go-dqlite. This is a little different from `canonical/go-dqlite` in `benchmark/worker.go`.
* **output:** This directory is mounted with the master node and stores the benchmark results. Check `output/172.24.2.1:9001/results` for the experiment results. (exec: PUT requests; query: GET requests)

# Baseline
I stored the baseline experiment results in the directory `experiment_result/baseline`. To elaborate, I ran the benchmark with different number of clients, from 1 thread to 16 threads. Next, I used the `python3 tool/baseline_plot.py` to plot the following figure.

![plot](./figures/baseline.png)

## How to reproduce?
```
# Step0: Make sure the mount directory is empty
rm -r output
mkdir output

# Step1: Build docker image (optional)
docker build -t dqlite .

# Step2: Build a 3-node dqlite cluster
docker-compose up

# Step3: Wait until the experiment finishes. Close the 3-node cluster
docker-compose down

# Step4: Check the experiment result in output/172.24.2.1:9001/results 
```