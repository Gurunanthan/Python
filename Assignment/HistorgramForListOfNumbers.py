import matplotlib.pyplot as plt
def create_histogram(data):
    plt.hist(data, bins=range(min(data), max(data) + 2), edgecolor='black')
    plt.title('Histogram of Given Data')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.show()
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
create_histogram(data)
