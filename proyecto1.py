def solve(graph):
        size = len(graph)
        reach =[i[:] for i in graph]

        for k in range(size):
                for i in range(size):
                        for j in range(size):
                                reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
        return reach
		

graph = [
    [0, 0, 1, 1],
    [1, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 0]] 

solution = solve(graph)

for i in range(len(solution)):
        print(solution[i])
