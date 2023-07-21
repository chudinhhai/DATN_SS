from node import Node
import random
import os
import math
from mlst import build_mlst



def create_and_save_topology(n,l,t):
    node_list = []
    N = n
    R = 1
    X = l
    Y = l    
    gap = round(L/100, 2)
    val_list = []
    k = gap
    while k<l:
        val_list.append(k)
        k += gap
        
    # Init sink node
    sink_node = Node()
    sink_node.ID = 0
    sink_node.x = l/2
    sink_node.y = l/2
    node_list.append(sink_node)
    i=1
    collision = True
    while len(node_list)<N:
        node = Node()
        node.ID = i
        node.x = random.choice(val_list)
        node.y = random.choice(val_list)
        k = 0
        while k<=len(node_list):
            curent_len = len(node_list)
            for component_node in node_list:
                if component_node.x == node.x and component_node.y == node.y:
                    node.x = random.choice(val_list)
                    node.y = random.choice(val_list)
                
                
        
                
        node_list.append(node)
        
        i += 1
        
    try:
        build_mlst(node_list)
        save_path = "C:/Users/ADMIN/Desktop/DATN/" + str(l) + "/"
        name_of_file = str(l) + "-" + str(n) + "-" + str(t) + '.txt'
        full_directory = os.path.join(save_path, name_of_file)
        with open (full_directory, 'w') as f:
            for component_node in node_list:
                f.write(str(component_node.x) + "," + str(component_node.y) + '\n')  
        return True
    except:
        print("t = " + str(t) + " again")
        return False
        
if __name__ == "__main__":
    i = 0
    k = 0
    D = 95
    L = 4
    n = (D*L*L)/(math.pi)
    print(n)
    r,im = divmod(n,1)
    while D <= 95:
        while i<20:
            if create_and_save_topology(r//1, L, i) == True:
                i += 1
            else:
                continue
        D += 10
        
        