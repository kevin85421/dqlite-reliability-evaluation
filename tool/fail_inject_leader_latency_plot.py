import matplotlib.pyplot as plt
   
data = {'Baseline': 0.865786, 'Slow CPU': 6.672633, 'Mem Contention': 0.872565}
key_list = list(data.keys())
throughput_list = list(data.values())
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(key_list, throughput_list, color ='maroon',
        width = 0.4)
 
plt.xlabel("Type of Slowness")
plt.ylabel("latency (ms)")
plt.title("Fail Injection Testing (Leader)")
plt.show()


