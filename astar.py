import csv
import queue
edgeFile = 'edges.csv'
heuristicFile = 'heuristic.csv'


def astar(start, end):
    # Begin your code (Part 4)
    # raise NotImplementedError("To be implemented")
    
    graph = dict()
    visited = dict()
    path = list()
    dist = float(0.0)
    num_visited = int(0)
    heuristic = dict() # [start point, straight dist]
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
            
            graph[data[0]][data[1]] = (float(data[2]), float(data[3]))
    
    # load data in heuristic.csv
    with open(heuristicFile) as file:
        for line in file:
            data = line.split(',')
            if data[0] == 'node': # first line
                for i in range (1,4):
                    if int(data[i]) == int(end):
                        case = i
                        break
            else:
                heuristic[data[0]] = float(data[case])
                
    # start implementing A*
    pq = queue.PriorityQueue()
    pq.put([0.0 + heuristic[str(start)], str(start)])
    visited[str(start)] = (0.0, 'start')
    reached = bool(0)
    
    while pq.empty() == 0 and reached == 0:
        current = pq.get()
        cur_location = current[1] # str
        num_visited += 1
        for next in graph[cur_location]:
            # weight = cur2next + prev dist + straight2next - straight2cur
            weight = graph[cur_location][next][0] + current[0] + heuristic[next] - heuristic[cur_location]
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
    dist = visited[current][0]
    while current != str(start):
        path.insert(0, int(current))
        current = visited[current][1] # trace back
    path.insert(0, start)
    
    return path, dist, num_visited
    # End your code (Part 4)


if __name__ == '__main__':
    path, dist, num_visited = astar(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
