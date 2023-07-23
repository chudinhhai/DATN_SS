from main import time_scheduling, time_scheduling_with_k
import matplotlib.pyplot as plt
import os

if __name__ == "__main__":
    # list = []
    # for i in range(0,30):
    #     delay = time_scheduling(85, 2, i)
    #     list.append(delay)
    # print(sum(list)/len(list))
    x = []
    y = []
    y_with_k = []
    k = 5
    while k <= 95:
        list = []
        for i in range(0,20):
            delay = time_scheduling(k, 7 , i)
            list.append(delay)
            print("D: " + str(k) + " time: " + str(i) + " without k")
        x.append(k)
        y.append(sum(list)/len(list))
        k += 10
    kk = 5
    while kk <= 95:
        list_with_k = []
        for i in range(0,20):
            delay = time_scheduling_with_k(kk, 7 , i, 5)
            list_with_k.append(delay)
            print("D: " + str(k) + " time: " + str(i) + " with k")
        # x.append(k)
        y_with_k.append(sum(list_with_k)/len(list_with_k))
        kk += 10
    print(y_with_k)
    print(y)
    plt.plot(x,y, label = "Org")
    plt.plot(x,y_with_k, label = "with k")
    plt.xticks(range(5, 105, 10))
    plt.yticks(range(0, 100, 25))
    plt.legend()
    plt.xlabel('Density')
    plt.ylabel('Delay')
    plt.show()
    # x = []
    # y = []
    # # save_path = "C:/Users/ADMIN/Desktop/DATN/7/"
    # save_path = "C:/Users/haicd/Desktop/DATN_SS/7"
    # name_of_file = "7-1481-0.txt"
    # full_directory = os.path.join(save_path, name_of_file)
    # file = open(full_directory)
    # for node_coordinate in file.readlines():
    #     x.append(float(node_coordinate.split(',')[0]))
    #     y.append(float(node_coordinate.split(',')[1]))
    # plt.scatter(x,y)
    # count = 0
    # for (xi, yi) in zip(x, y):
    #     plt.text(xi, yi, count, va='bottom', ha='center')
    #     count += 1
    # plt.show()