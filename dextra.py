import sys


def shortestpath(graph, start, end, visited=[], distances={}, predecessors={}):
    if not visited: distances[start] = 0

    if start == end:
        path = []
        while end != None:
            path.append(end)
            end = predecessors.get(end, None)
        return 'DISTANCE: '+str(distances[start]), 'PATH: '+str(path[::-1])

    for neighbor in graph[start]:
        if neighbor not in visited:
            neighbordist = distances.get(neighbor, sys.maxint)
            tentativedist = distances[start] + graph[start][neighbor]
            if tentativedist < neighbordist:
                distances[neighbor] = tentativedist
                predecessors[neighbor] = start

    visited.append(start)

    unvisiteds = dict((k, distances.get(k, sys.maxint)) for k in graph if k not in visited)
    closestnode = min(unvisiteds, key=unvisiteds.get)

    return shortestpath(graph, closestnode, end, visited, distances, predecessors)


if __name__ == "__main__":
    graph = {'1': {'5': 4, '7': 1},
             '2': {'5': 2, '6': 8},
             '3': {'7': 3, '8': 9},
             '4': {'6': 1, '8': 3},
             '5': {'7': 2, '8': 2, '6': 7, '1': 4, '2': 2},
             '6': {'2': 8, '8': 1, '5': 7, '4': 1},
             '7': {'5': 2, '1': 1, '8': 8, '3': 3},
             '8': {'6': 1, '5': 2, '7': 8, '3': 9, '4': 3}}
    print shortestpath(graph, '4', '7')
