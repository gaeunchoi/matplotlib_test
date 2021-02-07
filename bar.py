import matplotlib.pyplot as plt

data = [5., 25., 50., 20.]

# plt.bar(range(len(data)), data)
plt.bar(range(len(data)), data, width=1.)
plt.show()