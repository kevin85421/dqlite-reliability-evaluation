import matplotlib.pyplot as plt

data = {'Baseline': 562905 // 60, 'Slow CPU': 532818 // 60, 'Mem Contention': 547353 // 60, 'Crash': 520470 // 60}
key_list = list(data.keys())
throughput_list = list(data.values())
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(key_list, throughput_list, color ='maroon',
        width = 0.4)
 
plt.xlabel("Type of Slowness")
plt.ylabel("throughput (GET requests / sec)")
plt.title("Fail Injection Testing (Follower)")
plt.show()