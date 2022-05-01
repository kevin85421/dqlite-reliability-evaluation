import matplotlib.pyplot as plt
   
data = {'Baseline (4 cores)': 562905 // 60, '3 cores': 260028 // 60, '2 cores': 169137 // 60, '1 core': 65772 // 60 }
key_list = list(data.keys())
throughput_list = list(data.values())
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(key_list, throughput_list, color ='maroon',
        width = 0.4)
 
plt.xlabel("Type of Slowness")
plt.ylabel("throughput (GET requests / sec)")
plt.title("Slow CPU (Leader)")
plt.show()