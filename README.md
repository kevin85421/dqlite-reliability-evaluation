# dqlite
* canonical/raft: https://github.com/canonical/raft
* canonical/dqlite: https://github.com/canonical/dqlite
* canonical/go-dqlite: https://github.com/canonical/go-dqlite

**canonical/dqlite** is a C library that implements an embeddable and replicated SQL database engine with high-availability and automatic failover based on **canonical/raft**.
In addition, **canonical/go-dqlite** is a pure-Go client for the dqlite wire protocol.

# How to run?
```
# Step1: Build docker image
docker build -t dqlite .

# Step2: Build a 3-node dqlite cluster
docker-compose up
```

