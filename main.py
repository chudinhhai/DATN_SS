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
    i=1
    # Init other nodes
    while len(node_list)<N:
        node = Node()
        node.ID = i 
        node.x = random.uniform(0,X)
        node.y = random.uniform(0,Y)
        for component_node in node_list:
            if component_node.x == node.x:
                node.x = random.uniform(0,X)
                node.y = random.uniform(0,Y)
                break
        node.append
        
    # save_path = "C:/Users/ADMIN/Desktop/DATN/" + str(l) + "/"
    save_path = "C:/Users/haicd/Desktop/DATN_SS/" + str(l) + "/"
    name_of_file = str(l) + "-" + str(n) + "-" + str(t) + '.txt'
    full_directory = os.path.join(save_path, name_of_file)
    with open (full_directory, 'w') as f:
        for component_node in node_list:
            f.write(str(component_node.x) + "," + str(component_node.y) + '\n')  
            

def NDR_scheduling(node_list, i, scheduled_list, unscheduled_list):
    leaf_id_list = []
    
    for component_node in node_list:
        if component_node.ready == 0 and component_node.scheduled == False:
            if component_node.ID != 0:
                leaf_id_list.append(component_node.ID)
        
    
    
    for node_v_id in leaf_id_list:
        degree_list_of_u = []
        for node_u_id in node_list[node_v_id].neighbors:
            degree_list_of_u.append(len(node_list[node_u_id].neighbors))
    
        node_list[node_v_id].rank = sum(degree_list_of_u)
    
    leaf_node_list = []
    for node_id in leaf_id_list:
        leaf_node_list.append(node_list[node_id])
        
    sorted_list = sorted(leaf_node_list, key=lambda x: x.rank, reverse=True)
    
    current_scheduled_list = []
    current_collision = None
    for component_node in sorted_list:
        if primary_collision_checking(component_node, node_list, current_scheduled_list) == False and second_collision_checking(component_node, node_list, current_scheduled_list) == False:
            current_scheduled_list.append(component_node.ID)
            node_list[component_node.ID].timeslot = i
            node_list[component_node.ID].scheduled = True
            node_list[component_node.parentID].ready -= 1
                
            scheduled_list.append(component_node.ID)
            unscheduled_list.remove(component_node.ID)
        else:
            current_collision = component_node.ID
                
    return leaf_id_list, current_scheduled_list

def NDR_scheduling_with_k(node_list, i, scheduled_list, unscheduled_list, k_value, current_scheduled_list):
    leaf_id_list = []
    
    for component_node in node_list:
        if component_node.ready == 0 and component_node.scheduled == False :
            if component_node.ID != 0:
                leaf_id_list.append(component_node.ID)
        
    
    
    for node_v_id in leaf_id_list:
        degree_list_of_u = []
        for node_u_id in node_list[node_v_id].neighbors:
            degree_list_of_u.append(len(node_list[node_u_id].neighbors))
    
        node_list[node_v_id].rank = sum(degree_list_of_u)
    
    leaf_node_list = []
    for node_id in leaf_id_list:
        leaf_node_list.append(node_list[node_id])
        
    sorted_list = sorted(leaf_node_list, key=lambda x: x.rank, reverse=True)
    
    # current_scheduled_list = []
    current_collision = None
    for component_node in sorted_list:
        if primary_collision_checking(component_node, node_list, current_scheduled_list) == False and second_collision_checking(component_node, node_list, current_scheduled_list) == False:
            current_scheduled_list.append(component_node.ID)
            node_list[component_node.ID].timeslot = i
            node_list[component_node.ID].scheduled = True
            node_list[component_node.parentID].ready -= 1
            
            # he so k
            node_list[component_node.parentID].receivedMessage += 1
                
            scheduled_list.append(component_node.ID)
            unscheduled_list.remove(component_node.ID)
        else:
            current_collision = component_node.ID
                
    return leaf_id_list, current_scheduled_list
    

def primary_collision_checking(node, node_list, current_scheduled_set):
    if len(current_scheduled_set)!=0:
        for node_ID in current_scheduled_set:
            if node_list[node_ID].parentID == node.parentID:
                return True
    return False


def second_collision_checking(node_u, node_list, current_scheduled_list):
    for neighbor_id in node_u.neighbors:
        for childrenID in node_list[neighbor_id].childrenIDs:
            if childrenID in current_scheduled_list:
                return True
    for neighbor_id in node_list[node_u.parentID].neighbors:
        if neighbor_id in current_scheduled_list:
            return True
    return False

def primary_collision_for_ss(u_node_id, v_node_id, node_list, current_scheduled_list):
    if len(current_scheduled_list)!=0:
        for node_id in node_list[v_node_id].childrenIDs:
            if node_id in current_scheduled_list:
                return True
    return False

def secondary_collision_for_ss(u_node_id, v_node_id, node_list, current_scheduled_list):
    for node_id in node_list[u_node_id].neighbors:
        if node_id in current_scheduled_list:
            return True
    for node_id in node_list[v_node_id].neighbors:
        if node_id in current_scheduled_list:
            return True
    return False

def supplement_scheduling(node_list, remaining_node_set, current_scheduled_list, i, scheduled, unscheduled):
    remaining_node_list = list(remaining_node_set)
    for u_node_id in remaining_node_list:
        for v_node_id in node_list[u_node_id].neighbors:
            if node_list[v_node_id].ready != 0 and node_list[v_node_id].scheduled == False:
                if primary_collision_for_ss(u_node_id, v_node_id, node_list, current_scheduled_list) == False and secondary_collision_for_ss(u_node_id, v_node_id, node_list, current_scheduled_list)==False:
                    current_scheduled_list.append(u_node_id)
                    
                    node_list[node_list[u_node_id].parentID].childrenIDs.remove(u_node_id)
                    node_list[node_list[u_node_id].parentID].ready -= 1
                    
                    node_list[u_node_id].parentID = v_node_id
                    node_list[v_node_id].childrenIDs.add(u_node_id)
                    
                    remaining_node_list.remove(u_node_id)
                    
                    node_list[u_node_id].timeslot = i
                    node_list[u_node_id].scheduled = True
                    
                    scheduled.append(u_node_id)
                    unscheduled.remove(u_node_id)
                    
                    break
                    
    for u_node_id in remaining_node_list:
        for v_node_id in node_list[u_node_id].neighbors:
            if node_list[v_node_id].ready == 0 and node_list[v_node_id].scheduled == False:
                if primary_collision_for_ss(u_node_id, v_node_id, node_list, current_scheduled_list) == False and secondary_collision_for_ss(u_node_id, v_node_id, node_list, current_scheduled_list)==False:
                    current_scheduled_list.append(u_node_id)
                    
                    node_list[node_list[u_node_id].parentID].childrenIDs.remove(u_node_id)
                    node_list[node_list[u_node_id].parentID].ready -= 1
                    
                    node_list[u_node_id].parentID = v_node_id
                    node_list[v_node_id].childrenIDs.add(u_node_id)
                    
                    remaining_node_list.remove(u_node_id)
                    
                    node_list[u_node_id].timeslot = i
                    node_list[u_node_id].scheduled = True
                    
                    scheduled.append(u_node_id)
                    unscheduled.remove(u_node_id)
                    
                    break
                
    return current_scheduled_list, remaining_node_set
                
def supplement_scheduling_with_k(node_list, remaining_node_set, current_scheduled_list, i, scheduled, unscheduled):
    remaining_node_list = list(remaining_node_set)
    for u_node_id in remaining_node_list:
        for v_node_id in node_list[u_node_id].neighbors:
            if node_list[v_node_id].ready != 0 and node_list[v_node_id].scheduled == False:
                if primary_collision_for_ss(u_node_id, v_node_id, node_list, current_scheduled_list) == False and secondary_collision_for_ss(u_node_id, v_node_id, node_list, current_scheduled_list)==False:
                    current_scheduled_list.append(u_node_id)
                    
                    node_list[node_list[u_node_id].parentID].childrenIDs.remove(u_node_id)
                    node_list[node_list[u_node_id].parentID].ready -= 1
                    #he so k
                    # node_list[node_list[u_node_id].parentID].parentReady -= 1
                    node_list[node_list[u_node_id].parentID].receivedMessage += 1
                    
                    node_list[u_node_id].parentID = v_node_id
                    node_list[v_node_id].childrenIDs.add(u_node_id)
                    
                    remaining_node_list.remove(u_node_id)
                    
                    node_list[u_node_id].timeslot = i
                    node_list[u_node_id].scheduled = True
                    
                    scheduled.append(u_node_id)
                    unscheduled.remove(u_node_id)
                    
                    break
                    
    for u_node_id in remaining_node_list:
        for v_node_id in node_list[u_node_id].neighbors:
            if node_list[v_node_id].ready == 0 and node_list[v_node_id].scheduled == False:
                if primary_collision_for_ss(u_node_id, v_node_id, node_list, current_scheduled_list) == False and secondary_collision_for_ss(u_node_id, v_node_id, node_list, current_scheduled_list)==False:
                    current_scheduled_list.append(u_node_id)
                    
                    node_list[node_list[u_node_id].parentID].childrenIDs.remove(u_node_id)
                    node_list[node_list[u_node_id].parentID].ready -= 1
                    node_list[u_node_id].parentID = v_node_id
                    node_list[v_node_id].childrenIDs.add(u_node_id)
                    
                    remaining_node_list.remove(u_node_id)
                    
                    node_list[u_node_id].timeslot = i
                    node_list[u_node_id].scheduled = True
                    
                    scheduled.append(u_node_id)
                    unscheduled.remove(u_node_id)
                    
                    break
                
    return current_scheduled_list, remaining_node_set
                
def time_scheduling_with_k(D, L, t, k_value):
    n = (D*L*L)/(math.pi)
    # print(n)
    r,im = divmod(n,1)
    
    # create_and_save_Topology(int(r//1), L, t)
    
    node_list = []
    count = 0
    save_path_distance = "C:/Users/ADMIN/Desktop/DATN/" + str(L) + "/"
    # save_path_distance = "C:/Users/haicd/Desktop/DATN_SS/" + str(L) + "/"
    name_of_file_distance = str(L) + "-" + str(int(r//1)) + "-" + str(t) + '.txt'
    full_directory_distance = os.path.join(save_path_distance, name_of_file_distance)
    file_distance = open(full_directory_distance)
    
    for node_coordinate in file_distance.readlines():
        node = Node()
        node.ID = count
        node.x = float(node_coordinate.split(',')[0])
        node.y = float(node_coordinate.split(',')[1])
            
        node_list.append(node)
        count += 1
        pass
    time = 0
    save_path = "C:/Users/ADMIN/Desktop/DATN/" +  str(L) + "-" + str(L) + "/" 
    # save_path = "C:/Users/haicd/Desktop/DATN_SS/" +  str(L) + "-" + str(L) + "/" 
    name_of_file = str(L) + "-" + str(int(r//1)) + "-" + str(t) + '.txt'
    full_directory = os.path.join(save_path, name_of_file)
    file = open(full_directory)
    for children_set in file.readlines():
        for childrenID in children_set.split(','):
            if childrenID != "0" and childrenID != "\n":
                node_list[time].childrenIDs.add(int(childrenID))
                node_list[time].ready += 1
        time +=1
    for node in node_list:
        if len(node.childrenIDs) > 0:
            for children_id in node.childrenIDs:
                node_list[children_id].parentID = node.ID
                node_list[children_id].depth = node.depth + 1
    

    for i in range(0,len(node_list)):
        for k in range(0,len(node_list)):
            if distance(node_list[i], node_list[k]) < 1 and k!=i:
                node_list[i].neighbors.append(k)
                
    
    # build_mlst(node_list, int(r//1), L, t )
    i=0
    
    unscheduled = []
    scheduled = []
    
    
    # append unscheduled node
    for component_node in node_list:
        unscheduled.append(component_node.ID)


    # assign for k
    for node in node_list:
        if len(node.childrenIDs) >= k_value:
            node.k_ready = k_value - 1
        else:
            node.k_ready = len(node.childrenIDs)
            
    


    # value of iteration    
    i = 0
    # Neighbor Degree Ranking
    while len(unscheduled) > 1:
        # timeslot 
        i = i + 1
        # print(i)
        current_scheduled_list = []
        for node_id in unscheduled:
            if node_list[node_id].receivedMessage == node_list[node_id].k_ready and node_id != 0 and len(node_list[node_id].childrenIDs) > 0  and node_list[node_id].ready > 0 and node_list[node_id].scheduled == False:
                test1 = primary_collision_checking(node_list[node_id], node_list, current_scheduled_list)
                test2 = second_collision_checking(node_list[node_id], node_list, current_scheduled_list)
                if primary_collision_checking(node_list[node_id], node_list, current_scheduled_list) == False and second_collision_checking(node_list[node_id], node_list, current_scheduled_list) == False:
                    if node_list[node_list[node_id].parentID].receivedMessage < node_list[node_list[node_id].parentID].k_ready:
                        node_list[node_id].sendingTime += 1
                        node_list[node_list[node_id].parentID].receivedMessage += 1
                        node_list[node_id].receivedMessage = 0
                        if k_value*node_list[node_id].sendingTime < len(node_list[node_id].childrenIDs)+1:
                            remain_children = len(node_list[node_id].childrenIDs) - k_value*node_list[node_id].sendingTime + 1
                            if remain_children >= k_value:
                                node_list[node_id].k_ready = k_value
                            else:
                                node_list[node_id].k_ready = remain_children
                        elif k_value*node_list[node_id].sendingTime >= len(node_list[node_id].childrenIDs)+1:
                            node_list[node_list[node_id].parentID].ready -= 1
                            node_list[node_id].timeslot = i
                            node_list[node_id].receivedMessage = 0
                            node_list[node_id].scheduled = True
                            unscheduled.remove(node_id)
                            scheduled.append(node_id)
                        current_scheduled_list.append(node_id)
                
        node_leaf_id_list, current_scheduled_list = NDR_scheduling_with_k(node_list, i, scheduled, unscheduled, k_value, current_scheduled_list)
        


        if len(node_leaf_id_list)>=len(current_scheduled_list):
            remaining_set = set(node_leaf_id_list).difference(set(current_scheduled_list))
            current_scheduled_list, remaining_node_set = supplement_scheduling_with_k(node_list, remaining_set, current_scheduled_list, i , scheduled, unscheduled)
         
        for component_node in node_list:
            for node_id in scheduled:
                if node_id in component_node.neighbors:
                    component_node.neighbors.remove(node_id)
                    
        listsss = []



        
    # print(i)
    return i

def time_scheduling(D, L, t):
    n = (D*L*L)/(math.pi)
    r,im = divmod(n,1)
    
    # create_and_save_Topology(int(r//1), L, t)
    
    node_list = []
    count = 0
    save_path_distance = "C:/Users/ADMIN/Desktop/DATN/" + str(L) + "/"
    # save_path_distance = "C:/Users/haicd/Desktop/DATN_SS/" + str(L) + "/"
    name_of_file_distance = str(L) + "-" + str(int(r//1)) + "-" + str(t) + '.txt'
    full_directory_distance = os.path.join(save_path_distance, name_of_file_distance)
    file_distance = open(full_directory_distance)
    
    for node_coordinate in file_distance.readlines():
        node = Node()
        node.ID = count
        node.x = float(node_coordinate.split(',')[0])
        node.y = float(node_coordinate.split(',')[1])
            
        node_list.append(node)
        count += 1
        pass
    time = 0
    save_path = "C:/Users/ADMIN/Desktop/DATN/" +  str(L) + "-" + str(L) + "/" 
    # save_path = "C:/Users/haicd/Desktop/DATN_SS/" +  str(L) + "-" + str(L) + "/" 
    name_of_file = str(L) + "-" + str(int(r//1)) + "-" + str(t) + '.txt'
    full_directory = os.path.join(save_path, name_of_file)
    file = open(full_directory)
    for children_set in file.readlines():
        for childrenID in children_set.split(','):
            if childrenID != "0" and childrenID != "\n":
                node_list[time].childrenIDs.add(int(childrenID))
                node_list[time].ready += 1
        time +=1

    for node in node_list:
        if len(node.childrenIDs) > 0:
            for children_id in node.childrenIDs:
                node_list[children_id].parentID = node.ID
                node_list[children_id].depth = node.depth + 1
    
    # for node in node_list:
    #     print("ID: " + str(node.ID))

    #     print(node.childrenIDs)
    # Update neighbors
    # loop through node_list
    for i in range(0,len(node_list)):
        for k in range(0,len(node_list)):
            if distance(node_list[i], node_list[k]) < 1 and k!=i:
                node_list[i].neighbors.append(k)
                
    
    # build_mlst(node_list, int(r//1), L, t )
    i=0
    
    unscheduled = []
    scheduled = []
    
    # append unscheduled node
    for component_node in node_list:
        unscheduled.append(component_node.ID)
    # value of iteration    
    i = 0
    # Neighbor Degree Ranking
    while len(unscheduled) > 1:
        # timeslot 
        i = i + 1
        
        node_leaf_id_list, current_scheduled_list = NDR_scheduling(node_list, i, scheduled, unscheduled)
        


        if len(node_leaf_id_list)>=len(current_scheduled_list):
            remaining_set = set(node_leaf_id_list).difference(set(current_scheduled_list))
            supplement_scheduling(node_list, remaining_set, current_scheduled_list, i , scheduled, unscheduled)
            
        for component_node in node_list:
            for node_id in scheduled:
                if node_id in component_node.neighbors:
                    component_node.neighbors.remove(node_id)

            
    # print(i)
    return i
    
    
if __name__ == "__main__":
    # t=0
    l=2
    D = 95
    for t in range(0,20):
        delay = time_scheduling(D,l,t)
        delay2 = time_scheduling_with_k(D,l,t,2)
        delay3 = time_scheduling_with_k(D,l,t,3)
        
        print("without k: " + str(delay))
        print("with k=2: " + str(delay2))
        print("with k=3: " + str(delay3))