import csv
edgeFile = 'edges.csv'
import queue

def bfs(start, end):
    # Begin your code (Part 1)
    # raise NotImplementedError("To be implemented")
    
    graph = dict()
    visited = dict()
    path = list()
    dist = float(0.0)
    num_visited = int(0)
    
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
            
    # start implementing BFS
    q = queue.Queue()
    q.put(str(start))
    visited[str(start)] = 'start' # 'start': no prev node
    reached = bool(0) # to record whether reached end point or not
    
    while q.empty() == 0 and reached == 0:
        current = q.get()
        num_visited += 1
        for next in graph[current]:
            if visited[next] == -1: # haven't visited
                # visited[i] record the node come before i
                visited[next] = current
                if next == str(end): # if reach end
                    reached = 1
                    break
                q.put(next)
                
    # trace back from end to start, get dist and path[int]
    current = str(end)
    while current != str(start):
        path.insert(0, int(current))
        dist += graph[visited[current]][current][0] # data[2]: distance
        current = visited[current] # trace back
    path.insert(0, start)
    
    return path, dist, num_visited
    # End your code (Part 1)


if __name__ == '__main__':
    path, dist, num_visited = bfs(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
