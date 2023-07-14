from main import time_scheduling
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # list = []
    # for i in range(0,30):
    #     delay = time_scheduling(85, 2, i)
    #     list.append(delay)
    # print(sum(list)/len(list))
    x = []
    y = []
    k = 15
    while k <= 95:
        list = []
        for i in range(0,30):
            delay = time_scheduling(k, 2, i)
            list.append(delay)
        x.append(k)
        y.append(sum(list)/len(list))
        k += 10
    plt.plot(x,y)
    
    plt.xlabel('Density')
    plt.ylabel('Delay')
    plt.show()