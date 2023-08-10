from main import time_scheduling, time_scheduling_DFS, time_scheduling_BFS, time_scheduling_no_SS
import matplotlib.pyplot as plt
import os
if __name__ == "__main__":
    # list = []
    # for i in range(0,30):
    #     delay = time_scheduling(85, 2, i)
    #     list.append(delay)
    # print(sum(list)/len(list))
    L = 7
    L_limit = 8
    D = 45
    D_limit = 95
    x = []
    y = []
    y_no_SS = []
    # D=15
    # y_wires = [3, 14, 18, 21, 23.5, 24.5, 26.5, 28]
    # y_sda =   [3, 14, 17, 19, 22.5  , 22  , 24  , 26]
    #D=45
    # y = [12.55, 23.6, 27.7, 33.5, 37.2, 40.7, 43.25, 45.15]
    # y_wires = [12.55, 45, 49.5, 54  , 59, 64, 66  , 69]
    # y_sda =   [12.55, 45, 47.5, 49.5, 50, 49, 49.8, 51.5]
    #D=85
    # y = [24.75, 37.05, 46.9, 51.45, 59.45, 64.3, 68.1, 70.6]
    # y_wires = [24.75, 87, 90  , 102, 110 , 115, 120 , 122]
    # y_sda =   [24.75, 87, 88.5, 90 , 87.5, 86 , 86.4, 86.4]
    
    # x = [5, 15, 25, 35, 45, 55, 65, 75, 85, 95]
    # L=7
    # y = [15.15, 23.25, 29.95, 36.65, 43.25, 49.2, 55.25, 62.45, 68.1, 74.45]
    ## L=2
    # y_wires = [4.45,15,25,35,45,55,65,75,85,95]
    # y_sda = [4.45,15,25,35,45,55,65,75,85,95]
    ## L=4
    # y_wires = [9.15, 21  , 31.25, 44, 55, 66, 73, 87.5, 105, 115]
    # y_sda =   [9.15, 20.5, 29.5 , 42, 50, 60, 70, 83  , 94 , 99]
    ## L=7
    # y_wires = [16, 27, 38, 55, 67, 80, 94, 105, 117, 130]
    # y_sda =   [16, 25, 32, 42, 50, 58, 69, 78 , 87 , 95]
    ##
    y_with_DFS = []
    y_with_BFS = []
    
    k = 5
    while k <= D_limit:
        list = []
        for i in range(0,20):
            delay = time_scheduling_no_SS(k, L, i)
            list.append(delay)
            print("D: " + str(k) + " time: " + str(i) + " L: " + str(L) + " with MLST")
        x.append(k)
        y.append(sum(list)/len(list))
        k += 10
    # k1 = 1
    # while k1 <= L_limit:
    #     list = []
    #     for i in range(0,20):
    #         delay = time_scheduling_no_SS(D, k1, i)
    #         list.append(delay)
    #         print("D: " + str(D) + " time: " + str(k1) + " L: " + str(L) + " with MLST no SS")
    #     y_no_SS.append(sum(list)/len(list))
    #     k1 += 1

    k2 = 5
    while k2 <= D_limit:
        list_with_k = []
        for i in range(0,20):
            delay = time_scheduling_DFS(k2, L , i)
            list_with_k.append(delay)
            print("D: " + str(k2) + " time: " + str(i) + " L: " + str(L) + " with DFS")
        # x.append(k)
        y_with_DFS.append(sum(list_with_k)/len(list_with_k))
        k2 += 10
    k3 = 5 
    while k3 <= D_limit:
        list_with_k = []
        for i in range(0,20):
            delay = time_scheduling_BFS(k3, L , i)
            list_with_k.append(delay)
            print("D: " + str(k3) + " time: " + str(i) + " L: " + str(L) + " with BFS")
        # x.append(k)
        y_with_BFS.append(sum(list_with_k)/len(list_with_k))
        k3 += 10
        
    print("x:")
    print(x)
    print("y")
    print(y)
    print("y with DFS")
    print(y_with_DFS)
    print("y with BFS")
    print(y_with_BFS)
    plt.plot(x,y, label = "MLST", marker=".")
    # plt.plot(x,y_no_SS, label = "without SS", marker="*")
    # plt.plot(x,y_sda, label = "SDA", marker="|")
    plt.plot(x,y_with_DFS, label = "DFS", marker="*")
    plt.plot(x,y_with_BFS, label = "BFS", marker="|")
    plt.xticks(range(5, 105, 10))
    plt.yticks(range(0, 120, 20))
    plt.legend(loc='best')
    plt.xlabel('node density (D)')
    plt.ylabel('Delay')
    plt.title('side length L=' + str(L))
    plt.show()
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
