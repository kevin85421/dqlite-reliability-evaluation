import matplotlib.pyplot as plt

data = {'Baseline':  0.865786, 'Slow CPU': 0.915429, 'Mem Contention': 0.882218, 'Crash': 0.931356}
key_list = list(data.keys())
throughput_list = list(data.values())
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(key_list, throughput_list, color ='maroon',
        width = 0.4)
 
plt.xlabel("Type of Slowness")
plt.ylabel("latency (ms)")
plt.title("Fail Injection Testing (Follower)")
plt.show()