import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

latency = [0.370157, 0.414971, 0.455561, 0.504444, 0.538750, 0.589262, 0.685941, 0.780392, 0.865786, 0.975616, 1.049814, 1.163521, 1.264086, 1.349939, 1.434248, 1.543519]
throughput = [154225, 269596, 373455, 445440, 516240, 549462, 559951, 554784, 562905, 545330, 550594, 537948, 524368, 526932, 519645, 505520]
throughput = list(map(lambda x: x // 60, throughput))

plt.xlim([0, max(throughput) + 300])
plt.plot(throughput, latency, linestyle='--', marker='o', color='b', label='line with marker')

for i in range(len(latency)):
    plt.annotate(str(i + 1),
                 (throughput[i], latency[i]), 
                 textcoords="offset points", 
                 xytext=(-12,0), 
                 ha='center')
plt.ylabel("latency (ms)")
plt.xlabel("throughput (GET requests / sec)")

plt.show()