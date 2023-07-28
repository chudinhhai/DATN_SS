from main import time_scheduling, time_scheduling_with_k
import matplotlib.pyplot as plt
import os

if __name__ == "__main__":
    # list = []
    # for i in range(0,30):
    #     delay = time_scheduling(85, 2, i)
    #     list.append(delay)
    # print(sum(list)/len(list))
    L = 2
    x = []
    y = []
    y_with_k_1 = []
    y_with_k_2 = []
    y_with_k_3 = []
    k = 5
    while k <= 95:
        list = []
        for i in range(0,20):
            delay = time_scheduling(k, L, i)
            list.append(delay)
            print("D: " + str(k) + " time: " + str(i) + " L: " + str(L) + " without k")
        x.append(k)
        y.append(sum(list)/len(list))
        k += 10
    k1 = 5
    while k1 <= 95:
        list_with_k = []
        for i in range(0,20):
            delay = time_scheduling_with_k(k1, L , i, 3)
            list_with_k.append(delay)
            print("D: " + str(k1) + " time: " + str(i) + " L: " + str(L) + " with k = 1")
        # x.append(k)
        y_with_k_1.append(sum(list_with_k)/len(list_with_k))
        k1 += 10
    k2 = 5
    while k2 <= 95:
        list_with_k = []
        for i in range(0,20):
            delay = time_scheduling_with_k(k2, L , i, 3)
            list_with_k.append(delay)
            print("D: " + str(k2) + " time: " + str(i) + " L: " + str(L) + " with k = 2")
        # x.append(k)
        y_with_k_2.append(sum(list_with_k)/len(list_with_k))
        k2 += 10
    k3 = 5 
    while k3 <= 95:
        list_with_k = []
        for i in range(0,20):
            delay = time_scheduling_with_k(k3, L , i, 3)
            list_with_k.append(delay)
            print("D: " + str(k3) + " time: " + str(i) + " L: " + str(L) + " with k = 3")
        # x.append(k)
        y_with_k_3.append(sum(list_with_k)/len(list_with_k))
        k3 += 10
    print("x:")
    print(x)
    print("y without K:")
    print(y)
    print("y with k = 1")
    print(y_with_k_1)
    print("y with k = 2")
    print(y_with_k_2)
    print("y with k = 3")
    print(y_with_k_3)
    plt.plot(x,y, label = "without k")
    plt.plot(x,y_with_k_1, label = "with k=1")
    plt.plot(x,y_with_k_2, label = "with k=2")
    plt.plot(x,y_with_k_3, label = "with k=3")
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