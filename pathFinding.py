from collections import deque


class PathFinding:
    '''classe que representa o algoritmo de pathfinding'''
    def __init__(self, game):
        '''inicializa o algoritmo de pathfinding'''
        self.game = game
        self.map = game.gameMap.game_map
        self.ways = [-1, 0], [0, -1], [1, 0], [0, 1] # , [-1, -1], [1, -1], [1, 1], [-1, 1]
        self.graph = {}
        self.get_graph()

    def get_path(self, start, goal):
        '''retorna o caminho entre dois pontos'''
        self.visited = self.bfs(start, goal, self.graph)
        path = [goal]
        step = self.visited.get(goal, start)

        while step and step != start:
            path.append(step)
            step = self.visited[step]
        return path[-1]

    def bfs(self, start, goal, graph):
        '''retorna o caminho entre dois pontos'''
        queue = deque([start])
        visited = {start: None}

        while queue:
            cur_node = queue.popleft()
            if cur_node == goal:
                break
            next_nodes = graph[cur_node]

            for next_node in next_nodes:
                if next_node not in visited and next_node not in self.game.object_handler.enemy_positions:
                    queue.append(next_node)
                    visited[next_node] = cur_node
        return visited

    def get_next_nodes(self, x, y):
        ''' retorna os próximos nós possíveis'''
        return [(x + dx, y + dy) for dx, dy in self.ways if (x + dx, y + dy) not in self.game.gameMap.map_complt]

    def get_graph(self):
        '''retorna o grafo do mapa'''
        for y, row in enumerate(self.map):
            for x, col in enumerate(row):
                if not col:
                    self.graph[(x, y)] = self.graph.get((x, y), []) + self.get_next_nodes(x, y)