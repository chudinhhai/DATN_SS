from node import Node
from mlst import build_mlst
from trees import mlst
import random
import math
import sys
import queue
import os
import matplotlib.pyplot as plt
INFINITY = sys.maxsize - 1

def distance (node1, node2):
    # print("distance: " + str(math.sqrt(pow((node1.x-node2.x), 2) + pow((node1.y-node2.y), 2))))
    return math.sqrt(pow((node1.x-node2.x), 2) + pow((node1.y-node2.y), 2))

def count_Cv(node, child):
    count = 0
    for child in node.childrenIDs:
        count += 1
        count += count_Cv(node, child)
        
    return count

# def build_MLST(node_list):
#     Tree = []
#     Tree.append(node_list[0])
#     while

def build_DFS(node_list):
    list = []
    list.append(0)
    while len(list) > 0:
        v = list[-1]
        list.remove(v)
        if node_list[v].discovered is False:
            node_list[v].discovered = True
            for k in node_list[v].neighbors:
                if k not in list and node_list[k].discovered is False:
                    node_list[k].parentID = v
                    node_list[v].childrenIDs.append(k)
                    list.append(k)
        
def sort_ranking(leaf_set, node_list):
    max = 0
    
    sorted_list = []
    for each in leaf_set:
        for each_leaf in leaf_set:
            for list in node_list:
                if list.ID == each_leaf:
                    if list.rank >= max:
                        max = list.rank
                        currentID = list.ID
        sorted_list.append(currentID)
        max = 0
                    
         
    return sorted_list
                    
def primary_collision_checking(node, node_list, scheduled):
    if scheduled:
        for node_ID in scheduled:
            if node_list[node_ID].parentID == node.parentID:
                return True
        return False
    else:
        return False


def second_collision_checking(node, neighbor, leaf_list, node_list):
    if node.parentID == neighbor.ID:
        return False
    else:
        for neighbor_id in node.neighbors:
            for component_node in node_list:
                if component_node.ID == neighbor_id:
                    for id in component_node.childrenIDs:
                        if id in leaf_list:
                            leaf_list.remove(id)   
                            return False                
        for component_node in node_list:
            if component_node.ID == node.parentID:
                for id in component_node.neighbors:
                    if id in leaf_list:
                        leaf_list.remove(id)
                        return False
    return True

def create_fixed_topology():
    sink_node = Node()
    sink_node.ID = 0
    sink_node.neighbors = [1,3,5]
    sink_node.childrenIDs = {1,3,5}
    
    node1 = Node()
    node1.ID = 1
    node1.neighbors = [0,2,5,6]
    node1.parentID = 0
    node1.childrenIDs = {2,6}
    
    node2 = Node()
    node2.ID = 2
    node2.parentID = 1
    node2.neighbors = [1]
    
    node3 = Node()
    node3.ID = 3
    node3.neighbors = [0]
    node3.parentID = 0
    
    node4 = Node()
    node4.ID = 4
    node4.neighbors = [5]
    node4.parentID = 5
    
    node5 = Node()
    node5.ID = 5
    node5.neighbors = [0,4]
    node5.parentID = 0
    node5.childrenIDs = {4}
    
    node6 = Node()
    node6.ID = 6
    node6.neighbors = [1]
    node6.parentID = 1
    
    list = []
    list.append(sink_node)
    list.append(node1)
    list.append(node2)
    list.append(node3)
    list.append(node4)
    list.append(node5)
    list.append(node6)
    
    return list
    
    
    
    

def node_sort_key(node):
    return node.rank
        
def build_BFS(node_list):
    for each_node in node_list:
        each_node.distance = INFINITY
    node_list[0].distance = 0
    q = queue.Queue()
    q.put(node_list[0])
    count = 0
    while q.empty() is False:
        current = q.get()
        count += 1
        for each_node_id in current.neighbors:
            if node_list[each_node_id].distance == INFINITY:
                node_list[each_node_id].distance = current.distance + 1
                node_list[each_node_id].parentID = current.ID
                current.childrenIDs.append(each_node_id)
                q.put(node_list[each_node_id])
    else:
        if count < len(node_list):
            print("Disconnected network!!!")
            return False
    return True

def create_and_save_Topology(n,l,t):
    node_list = []
    N = n
    R = 1
    X = l
    Y = l    
    
    # Init sink node
    sink_node = Node()
    sink_node.ID = 0
    sink_node.x = l/2
    sink_node.y = l/2
    node_list.append(sink_node)
    
    # Init other nodes
    for i in range(1,N):
        node = Node()
        node.ID = i 
        node.x = random.uniform(0,X)
        node.y = random.uniform(0,Y)
        for component_node in node_list:
            if component_node.x != node.x and component_node != node.y:
                continue
            else:
                print("collision")
                node.x = random.uniform(0,l)
                node.y = random.uniform(0,l)
        node_list.append(node)
    save_path = "C:/Users/ADMIN/Desktop/DATN/" + str(l) + "/"
    name_of_file = str(l) + "-" + str(n) + "-" + str(t) + '.txt'
    full_directory = os.path.join(save_path, name_of_file)
    with open (full_directory, 'w') as f:
        for component_node in node_list:
            f.write(str(component_node.x) + "," + str(component_node.y) + '\n')  

    
def time_scheduling(D, L, t):
    n = (D*L*L)/(math.pi)
    r,im = divmod(n,1)
    # create_and_save_Topology(int(r//1), L, t)
    node_list = []
    count = 0
    save_path = "C:/Users/ADMIN/Desktop/DATN/" + str(L) + "/"
    name_of_file = str(L) + "-" + str(int(r//1)) + "-" + str(t) + '.txt'
    full_directory = os.path.join(save_path, name_of_file)
    # print(full_directory)
    file = open(full_directory)
    for node_coordinate in file.readlines():
        node = Node()
        node.ID = count
        node.x = float(node_coordinate.split(',')[0])
        node.y = float(node_coordinate.split(',')[1])
        
        node_list.append(node)
        count += 1
        pass
    
    # Update neighbors
    # loop through node_list
    for i in range(0,len(node_list)):
        for k in range(1,len(node_list)):
            if(distance(node_list[i], node_list[k]) < 1):
                node_list[i].neighbors.append(k)
    
    # for component_node in graph_list:
    #     print(component_node.neighbors)
    build_mlst(node_list)
    # for component_node in node_list:
        # print("\nID: " + str(component_node.ID))
        # print(component_node.depth)
    
    # for component_node in node_list:
    #     print(component_node.ID)
    # Print check neighbor

    # # Build a tree on the node_list
    # mlst(node_list)
    unscheduled = []
    scheduled = []
    
    # append unscheduled node
    for component_node in node_list:
        unscheduled.append(component_node.ID)
    # value of iteration    
    i = 0
    # Neighbor Degree Ranking
    while len(unscheduled)>0:
        # timeslot 
        i = i + 1
        # list and set of leaf node
        node_leaf_list = []
        node_leaf_id_set = set()
        # for component_node in node_list:
        #     print(component_node.ID)
        #     print(component_node.childrenIDs)
        #     print(component_node.scheduled)
        for component_node in node_list:
            if component_node.parentID != -1 and len(component_node.childrenIDs) == 0:
                node_leaf_list.append(component_node)
                node_leaf_id_set.add(component_node.ID)
        
        # ranking leaf node
 
        for leafID in node_leaf_id_set:
            du = []
            for component_node in node_list:
                if component_node.ID == leafID:
                    for neighborID in component_node.neighbors:
                        du.append(len(node_list[neighborID].childrenIDs))
            s = 0
            for k in du:
                s = s + k
            for component_node in node_list:
                if component_node.ID == leafID:
                    component_node.rank = s
                    
        unsort_list = []
        for leafID in node_leaf_id_set:
            for component_node in node_leaf_list:
                if component_node.ID == leafID:
                    unsort_list.append(component_node)
        # Set timeslot for component node
        sorted_list = sorted(unsort_list, key=node_sort_key, reverse=True)
        
        for component_node in sorted_list:
            if not primary_collision_checking(component_node, node_list, scheduled):
                node_list[component_node.ID].timeslot = i
                
                node_leaf_id_set.remove(component_node.ID)
                
                scheduled.append(component_node.ID)
                unscheduled.remove(component_node.ID)
                
                if component_node.ID !=0:
                    node_list[component_node.parentID].childrenIDs.remove(component_node.ID)
                    node_list[component_node.ID].parentID = -1
            else:
                # node_leaf_id_set.remove(component_node.ID)
                print("collision")

        

        if node_leaf_id_set:
            # Sort the list 
            # Supplementary Scheduling
            
            # Non-leaf neighbor
            non_leaf_neighbor_list = []
            for u_node_id in node_leaf_id_set:
                for v_node_id in node_list[u_node_id].neighbors:
                    for v_node_neighbor_id in node_list[v_node_id].neighbors:
                        if not node_list[v_node_neighbor_id].childrenIDs:
                            non_leaf_neighbor_list.append(node_list[v_node_neighbor_id])
                            
            # line 1 in paper
            for u_node_id in node_leaf_id_set:
                for v_node in non_leaf_neighbor_list:
                    if second_collision_checking(node_list[u_node_id], v_node, node_leaf_id_set, node_list):
                        node_list[u_node_id].timeslot = i
                        
                        
                        node_list[node_list[u_node_id].parentID].childrenIDs.remove(u_node_id)
                        node_list[u_node_id].parentID = v_node.ID
                        scheduled.append(u_node_id)
                        unscheduled.remove(u_node_id)
            
            # Leaf neighbor
            leaf_neighbor_list = []
            for u_node_id in node_leaf_id_set:
                for v_node_id in node_list[u_node_id].neighbors:
                    for v_node_neighbor_id in node_list[v_node_id].neighbor:
                        if node_list[v_node_neighbor_id].childrenIDs:
                            leaf_neighbor_list.append(node_list[v_node_neighbor_id])

            # line 10 in paper
            for u_node_id in node_leaf_id_set:
                for v_node in leaf_neighbor_list:
                    if second_collision_checking(node_list[u_node_id], v_node, node_leaf_id_set, node_list):
                        node_list[u_node_id].timeslot = i
                        node_list[u_node_id].scheduled = True
                        node_list[node_list[u_node_id].parentID].childrenIDs.remove(u_node_id)
                        node_list[u_node_id].parentID = v_node.ID
                        scheduled.append(u_node_id)
                        unscheduled.remove(u_node_id)

            for component_node in node_list:
                for scheduled_node_id in scheduled:
                    if scheduled_node_id in component_node.childrenIDs:
                        component_node.childrenIDs.remove(scheduled_node_id)
                        
        else:
            for component_node in node_list:
                for scheduled_node_id in scheduled:
                    if scheduled_node_id in component_node.childrenIDs:
                        component_node.childrenIDs.remove(scheduled_node_id)
        
    return i
    
    
if __name__ == "__main__":
    print(time_scheduling(35,2,0))
    