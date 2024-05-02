import heapq

def manhattan_distance(state, goal):
    distance = 0
    for i in range(1, 9):
        xi, yi = divmod(state.index(i), 3)
        xg, yg = divmod(goal.index(i), 3)
        distance += abs(xi - xg) + abs(yi - yg)
    return distance

def solve_puzzle(start, goal):
    open_list = []
    start_tuple = tuple(start)
    goal_tuple = tuple(goal)
    heapq.heappush(open_list, (manhattan_distance(start_tuple, goal_tuple), 0, start_tuple, None))
    closed_list = set()
    parents = {}
    
    while open_list:
        f, g, current_tuple, parent_tuple = heapq.heappop(open_list)
        
        if current_tuple in closed_list:
            continue
        
        parents[current_tuple] = parent_tuple
        if current_tuple == goal_tuple:
            path = []
            while current_tuple:
                path.append(list(current_tuple))
                current_tuple = parents.get(current_tuple)
            return path[::-1]
        
        closed_list.add(current_tuple)
        
        current = list(current_tuple)
        zero_idx = current.index(0)
        row, col = divmod(zero_idx, 3)
        for move in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = row + move[0], col + move[1]
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                successor = current[:]
                new_idx = new_row * 3 + new_col
                successor[zero_idx], successor[new_idx] = successor[new_idx], successor[zero_idx]
                successor_tuple = tuple(successor)
                if successor_tuple not in closed_list:
                    heapq.heappush(open_list, (g + 1 + manhattan_distance(successor_tuple, goal_tuple), g + 1, successor_tuple, current_tuple))
    return "No solution found."

start = [1, 5, 3, 
         4, 0, 6, 
         2, 7, 8]
goal = [1, 2, 3, 
        4, 5, 6, 
        7, 8, 0]

path = solve_puzzle(start, goal)
if isinstance(path, list):
    for state in path:
        print(state)
else:
    print(path) 
