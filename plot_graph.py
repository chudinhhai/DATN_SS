from main import time_scheduling
import matplotlib.pyplot as plt
import os

if __name__ == "__main__":
    # list = []
    # for i in range(0,30):
    #     delay = time_scheduling(85, 2, i)
    #     list.append(delay)
    # print(sum(list)/len(list))
    # x = []
    # y = []
    # k = 5
    # while k <= 95:
    #     list = []
    #     for i in range(0,20):
    #         delay = time_scheduling(k, 2 , i)
    #         list.append(delay)
    #     x.append(k)
    #     y.append(sum(list)/len(list))
    #     k += 10
    # plt.plot(x,y)
    
    # plt.xlabel('Density')
    # plt.ylabel('Delay')
    # plt.show()
    x = []
    y = []
    # save_path = "C:/Users/ADMIN/Desktop/DATN/7/"
    save_path = "C:/Users/haicd/Desktop/DATN_SS/7"
    name_of_file = "7-1481-0.txt"
    full_directory = os.path.join(save_path, name_of_file)
    file = open(full_directory)
    for node_coordinate in file.readlines():
        x.append(float(node_coordinate.split(',')[0]))
        y.append(float(node_coordinate.split(',')[1]))
    plt.scatter(x,y)
    count = 0
    for (xi, yi) in zip(x, y):
        plt.text(xi, yi, count, va='bottom', ha='center')
        count += 1
    plt.show()