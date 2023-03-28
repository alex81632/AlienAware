import pygame as pg
import random
import numpy as np

_ = 0

# sala inicial 10x10 com paredes em volta
mapa_inicial = [[1,1,1,1,1,1,1,1,1,1,1]] + [[1,_,_,_,_,_,_,_,_,_,1] for i in range(9)] + [[1,1,1,1,1,_,1,1,1,1,1]]

# sala final 20x20 com paredes em volta
mapa_final = [[1]*21] + [[1]+[0]*19+[1] for i in range(19)] + [[1]*21]


class GameMap:
    def __init__(self, game):
        self.game = game
        self.game_map = mapa_inicial
        self.game.constants.mapa_atual = 0
        self.game.constants.map_height = len(self.game_map)
        self.game.constants.map_width = len(self.game_map[0])
        self.game.constants.player_initial_position = self.game.constants.map_width/2, 1.5
        self.map_complt  = {}
        self.const_mapa()
        self.map_inversed = {}
        self.invert_map()
    
    def next_map(self):
        self.game.constants.map_height = 50
        self.game.constants.map_width = 20
        self.game.constants.mapa_atual += 1
        self.game.constants.max_level = max(self.game.constants.max_level, self.game.constants.mapa_atual)
        if self.game.constants.mapa_atual == 3:
            self.game_map = mapa_final
        else:
            self.game_map = self.generate_map(self.game.constants.map_height, self.game.constants.map_width)
        self.game.constants.player_initial_position = self.game.constants.map_width/2, 1.5
        self.map_complt  = {}
        self.const_mapa()
        self.map_inversed = {}
        self.invert_map()


    def const_mapa(self):
        for i,coluna in enumerate(self.game_map):
            for j, valor in enumerate(coluna):
                if valor == 1:
                    self.map_complt[(j,i)] = valor
    
    def invert_map(self):
        for i,coluna in enumerate(self.game_map):
            for j, valor in enumerate(coluna):
                if valor == 0:
                    self.map_inversed[(j,i)] = valor
    
# o algorítmo de geração de mapas é feito com base em uma dfs para gerar um labirinto

    def generate_map(self, width, height):
        visited = {}
        stack = []
        map_ = np.zeros((width, height))
        # inicialmente faz-se uma dfs gerando o labirinto
        # a dfs é feita a partir do ponto (1,height//2)
        map_ = self.alg_dir(map_)
        map_ = self.alg_inv(map_)

        # o mapa é circundado por paredes
        for i in range(width):
            map_[i][0] = 1
            map_[i][height-1] = 1
        for i in range(height):
            map_[0][i] = 1
            map_[width-1][i] = 1

        # o ponto de entrada é definido como (1,height//2)
        map_[1][height//2+1] = 0
        map_[1][height//2] = 0
        map_[1][height//2-1] = 0

        # o ponto de saída é definido como (width-2,height//2)
        map_[width-2][height//2+1] = 0
        map_[width-2][height//2] = 0
        map_[width-2][height//2-1] = 0

        # depois é feita uma dfs para checar se é possível chegar em todos os pontos do mapa

        self.dfs(map_, 1, height//2, visited, stack)

        # se não for possível chegar em (width-2, height//2), o mapa é gerado novamente
        if (width-2, height//2) not in visited:
            print("gerando novo mapa...")
            return self.generate_map(width, height)

        # se não for possível chegar em algum ponto, esse ponto é transformado em uma parede
        for i in range(width):
            for j in range(height):
                if (i,j) not in visited:
                    map_[i][j] = 1

        map_[width-1][height//2] = 0
        map_ = np.append(map_, np.ones((1, height)), axis=0)

        #self.print_map(map_, visited)

        return map_

    def alg_dir(self, map_):
        height = len(map_)
        width = len(map_[0])
        for i in range(len(map_)):
            for j in range(len(map_[i])):
                if map_[i][j] != 1:
                    chose = 0 if random.random() > 0.5 else 1
                    if chose == 0 and i+1 < height:
                        map_[i+1][j] = 1
                    elif j+1 < width:
                        map_[i][j+1] = 1
        
        return map_

    def alg_inv(self, map_):
        for i in range(len(map_)):
            for j in range(len(map_[i])):
                if random.random() > 0.5:
                    if map_[i][j] != 1:
                        chose = 0 if random.random() > 0.5 else 1
                        if chose == 0 and i-1 > 1:
                            map_[i-1][j] = 0
                        elif j-1 > 1:
                            map_[i][j-1] = 0
        
        return map_

    # dfs com stack

    def dfs(self, map_, x, y, visited={}, stack=[]):
        stack.append((x,y))
        while len(stack) > 0:
            current = stack.pop()
            if current not in visited:
                visited[current] = 1
                x = current[0]
                y = current[1]
                if x+1 < len(map_) and map_[x+1][y] != 1:
                    stack.append((x+1,y))
                if x-1 > 0 and map_[x-1][y] != 1:
                    stack.append((x-1,y))
                if y+1 < len(map_[0]) and map_[x][y+1] != 1:
                    stack.append((x,y+1))
                if y-1 > 0 and map_[x][y-1] != 1:
                    stack.append((x,y-1))
            # se chegou no ponto de saída, retorna
            # if current == (len(map_)-2, len(map_[0])//2):
            #     return

    def print_map(self, map_, visited={}):
        for i in range(len(map_)):
            for j in range(len(map_[i])):
                # se tiver em visited, printa #
                if (i,j) in visited:
                    print(" # ", end="")
                elif map_[i][j] == 0:
                    print(" _ ", end="")
                else:
                    print(" 1 ", end="")
            print()