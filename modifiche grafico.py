import matplotlib.pyplot as plt

data = {'Marco': 15, 'Luca': 14, 'Giorgia': 14, 'Nicola': 17}
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)
axs[0].bar(names, values)
axs[1].scatter(names, values)
axs[2].plot(names, values)
fig.suptitle('Età studenti')


plt.show()
