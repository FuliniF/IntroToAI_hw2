import csv
import queue
edgeFile = 'edges.csv'
heuristicFile = 'heuristic.csv'


def astar_time(start, end):
    # Begin your code (Part 6)
    # raise NotImplementedError("To be implemented")
    
    graph = dict()
    visited = dict()
    path = list()
    time = float(0.0)
    num_visited = int(0)
    heuristic = dict() # [start point, straight dist]
    maxSpeed = int(0)
    case = int(0)
    
    # load data in edges.csv
    with open(edgeFile) as file:
        for line in file:
            data = line.split(',')
            if data[0] == 'start':
                continue
            
            # initialize visited to -1 (not visited)
            visited[data[0]] = int(-1)
            if data[0] not in graph:
                graph[data[0]] = dict()
            visited[data[1]] = int(-1)
            if data[1] not in graph:
                graph[data[1]] = dict()
            
            # change speed unit from km/h to m/sec, and save max speed in here
            graph[data[0]][data[1]] = (float(data[2]), float(data[3]) * 1000 / 3600)
            maxSpeed = max(maxSpeed, float(data[3]) * 1000 / 3600)
    
    # load data in heuristic.csv
    with open(heuristicFile) as file:
        for line in file:
            data = line.split(',')
            
            if data[0] == 'node': # first line
                for i in range (1,4):
                    if end == int(data[i]):
                        case = i
                        break
                continue
            else:
                heuristic[data[0]] = float(data[case])
                
    # start implementing A* time
    pq = queue.PriorityQueue()
    pq.put([0.0 + heuristic[str(start)]/maxSpeed, str(start)])
    visited[str(start)] = (0.0, 'start')
    reached = bool(0)
    
    while pq.empty() == 0 and reached == 0:
        current = pq.get()
        cur_location = current[1] # str
        num_visited += 1
        for next in graph[cur_location]:
            # weight = time from cur to next + prev time + straight2next(time) - straight2cur(time)
            weight = graph[cur_location][next][0]/graph[cur_location][next][1] + current[0] + heuristic[next]/maxSpeed - heuristic[cur_location]/maxSpeed
            if visited[next] == -1: # haven't visited
                visited[next] = (weight, cur_location)
                pq.put([weight, next])
            if weight < visited[next][0]: # found better route
                visited[next] = (weight, cur_location)
                pq.put([weight, next])
            if next == str(end): # if reach end
                reached = 1
                break
                
    # trace back from end to start, get dist and path[int]
    current = str(end)
    time = visited[current][0]
    while current != str(start):
        path.insert(0, int(current))
        current = visited[current][1] # trace back
    path.insert(0, start)
    
    return path, time, num_visited
    # End your code (Part 6)


if __name__ == '__main__':
    path, time, num_visited = astar_time(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total second of path: {time}')
    print(f'The number of visited nodes: {num_visited}')
