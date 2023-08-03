from main import time_scheduling, time_scheduling_with_k
import matplotlib.pyplot as plt
import os
if __name__ == "__main__":
    # list = []
    # for i in range(0,30):
    #     delay = time_scheduling(85, 2, i)
    #     list.append(delay)
    # print(sum(list)/len(list))
    # L = 4
    # D_limit = 95
    # x = []
    # y = []
    
    # y_with_k_2 = []
    # y_with_k_3 = []
    # y_with_k_5 = []
    # k = 5
    # while k <= D_limit:
    #     list = []
    #     for i in range(0,20):
    #         delay = time_scheduling(k, L, i)
    #         list.append(delay)
    #         print("D: " + str(k) + " time: " + str(i) + " L: " + str(L) + " without k")
    #     x.append(k)
    #     y.append(sum(list)/len(list))
    #     k += 10
    # k1 = 5

    # k2 = 5
    # while k2 <= D_limit:
    #     list_with_k = []
    #     for i in range(0,20):
    #         delay = time_scheduling_with_k(k2, L , i, 2)
    #         list_with_k.append(delay)
    #         print("D: " + str(k2) + " time: " + str(i) + " L: " + str(L) + " with k = 2")
    #     # x.append(k)
    #     y_with_k_2.append(sum(list_with_k)/len(list_with_k))
    #     k2 += 10
    # k3 = 5 
    # while k3 <= D_limit:
    #     list_with_k = []
    #     for i in range(0,20):
    #         delay = time_scheduling_with_k(k3, L , i, 3)
    #         list_with_k.append(delay)
    #         print("D: " + str(k3) + " time: " + str(i) + " L: " + str(L) + " with k = 3")
    #     # x.append(k)
    #     y_with_k_3.append(sum(list_with_k)/len(list_with_k))
    #     k3 += 10
    # k5 = 5 
    # while k5 <= D_limit:
    #     list_with_k = []
    #     for i in range(0,20):
    #         delay = time_scheduling_with_k(k5, L , i, 5)
    #         list_with_k.append(delay)
    #         print("D: " + str(k5) + " time: " + str(i) + " L: " + str(L) + " with k = 5")
    #     # x.append(k)
    #     y_with_k_5.append(sum(list_with_k)/len(list_with_k))
    #     k5 += 10
    # x = [5,15,25,35,45,55,65,75,85,95]
    # y = [15.15, 23.25, 29.95, 36.65, 43.25, 49.2, 55.25, 62.45, 68.1, 74.45]
    # y_with_k_2 = [15.55, 24.8, 32.95, 40.45, 47.55, 53.7, 60.8, 68.75, 75.75, 82.55]
    # y_with_k_3 = [15.2, 23.85, 30.5, 37.85, 44.8, 50.75, 57.15, 64.75, 70.15, 77.15]
    # print("x:")
    # print(x)
    # print("y without K:")
    # print(y)
    # # print("y with k = 1")
    # # print(y_with_k_1)
    # print("y with k = 2")
    # print(y_with_k_2)
    # print("y with k = 3")
    # print(y_with_k_3)
    # # print("y with k = 5")
    # # print(y_with_k_5)
    # plt.plot(x,y, label = "without k")
    # # plt.plot(x,y_with_k_1, label = "with k=1")
    # plt.plot(x,y_with_k_2, label = "with k=2")
    # plt.plot(x,y_with_k_3, label = "with k=3")
    
    # # plt.plot(x,y_with_k_5, label = "with k=5")
    # plt.xticks(range(5, 105, 10))
    # plt.yticks(range(0, 100, 25))
    # plt.legend()
    # plt.xlabel('Density')
    # plt.ylabel('Delay')
    # plt.show()
    # x = []
    # y = []
    # save_path = "C:/Users/ADMIN/Desktop/DATN/2/"
    # # save_path = "C:/Users/haicd/Desktop/DATN_SS/2"
    # name_of_file = "2-19-0.txt"
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
    
    L = 2
    x = [2,3,5,7,10]
    y=[]
    list = []
    list_with_k_2 = []
    list_with_k_3 = []
    list_with_k_5 = []
    list_with_k_7 = []
    list_with_k_10 = []
    init_value = None
    for i in range(0,20):
        delay = time_scheduling(55, L , i)
        list.append(delay)
        print("D: " + str(55) + " time: " + str(i) + " L: " + str(L))
    init_value = sum(list)/len(list)
    for i in range(0,20):
        delay = time_scheduling_with_k(55, L , i, 2)
        list_with_k_2.append(delay)
        print("D: " + str(55) + " time: " + str(i) + " L: " + str(L) + " with k = 2")
    y.append(sum(list_with_k_2)/len(list_with_k_2) - init_value)
    for i in range(0,20):
        delay = time_scheduling_with_k(55, L , i, 3)
        list_with_k_3.append(delay)
        print("D: " + str(55) + " time: " + str(i) + " L: " + str(L) + " with k = 3")
    y.append(sum(list_with_k_3)/len(list_with_k_3) - init_value)
    for i in range(0,20):
        delay = time_scheduling_with_k(55, L , i, 5)
        list_with_k_5.append(delay)
        print("D: " + str(55) + " time: " + str(i) + " L: " + str(L) + " with k = 5")
    y.append(sum(list_with_k_5)/len(list_with_k_5) - init_value)
    for i in range(0,20):
        delay = time_scheduling_with_k(55, L , i, 7)
        list_with_k_7.append(delay)
        print("D: " + str(55) + " time: " + str(i) + " L: " + str(L) + " with k = 7")
    y.append(sum(list_with_k_7)/len(list_with_k_7) - init_value)
    for i in range(0,20):
        delay = time_scheduling_with_k(55, L , i, 10)
        list_with_k_10.append(delay)
        print("D: " + str(55) + " time: " + str(i) + " L: " + str(L) + " with k = 10")
    y.append(sum(list_with_k_10)/len(list_with_k_10) - init_value)
    plt.plot(x,y)
    plt.xlabel("k")
    plt.ylabel("delay")
    plt.show()  