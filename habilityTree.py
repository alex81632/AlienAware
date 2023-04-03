import pygame as pg
import os

class HabilityTree:
    def __init__(self, screen, constants):
        self.screen = screen
        self.constants = constants
        self.padding = int(40*self.constants.pixel * (self.constants.width / 1920))
        self.font = pg.font.Font('assets/fonts/dogicapixel.ttf', int(self.constants.font_size))
        self.font_decription = pg.font.Font('assets/fonts/dogicapixel.ttf', int(self.constants.font_size)//2)
        self.font_title = pg.font.Font('assets/fonts/dogicapixel.ttf', int(self.constants.font_size)*2)
        self.classes = []
        self.subClasses = []
        self.habilities = []
        self.size = int(50*self.constants.pixel * (self.constants.width / 1920))
        self.selected = 0
        # temporariamente
        nome = 'accuracy'
        descricao = 'aumenta o dano da arma'
        custo = 10
        # contruir arvore de habilidades
        #classes
        self.classes.append(self.hability(0, "Constituição", "Liberar a árvore de constituição", custo, -1, self.size, 5))
        self.classes.append(self.hability(1, "Técnico", "Liberar a árvore técnica", custo, -1, self.size, 6))
        # definir que as classes 0 e 1 tem status 1
        self.classes[0].status = 1
        self.classes[1].status = 1
        #subclasses
        self.subClasses.append(self.hability(2, "Ganância", "Libera a árvore de ganância", custo, 0, self.size, 1))
        self.subClasses.append(self.hability(3, "Armas", "Libera a árvore de armas", custo, 0, self.size, 3))
        self.subClasses.append(self.hability(4, "Furtividade", "Libera a árvore de furtividade", custo, 0, self.size, 1))
        self.subClasses.append(self.hability(5, "Resistência", "Libera a árvore de resistência", custo, 1, self.size, 2))
        self.subClasses.append(self.hability(6, "Saúde", "Libera a árvore de saúde", custo, 1, self.size, 3))
        self.subClasses.append(self.hability(7, "Velocidade", "Libera a árvore de velocidade", custo, 1, self.size, 1))
        # habilidades
        nome = ['Ganância', 'Precisão', 'Tempo', 'Dano', 'Munição', 'Furtividade', 'Resistência física', 'Resistência bala', 'Vida' ,'Mais Frascos' ,'Mais Achados' , 'Velocidade']
        descricao = ['Aumenta em 10% a coleta de recursos',
                     'Aumenta em 10% a precisão com armas', 
                     'Diminui em 10% o tempo de recarga de armas', 
                     'Aumenta em 10% o dano de armas', 
                     'Aumenta em 10% a munição de armas', 
                     'Aumenta em 10% a chance de furtividade', 
                     'Aumenta em 10% a resistência física', 
                     'Aumenta em 10% a resistência a balas', 
                     'Aumenta em 10% a vida', 
                     'Aumenta em 1 a quantidade de frascos inciais', 
                     'Aumenta em 1 a quantidade de frascos achados em salas', 
                     'Aumenta em 10% a velocidade']
        k = " I"
        # linha 1
        self.habilities.append(self.hability(8, nome[0] + k, descricao[0], custo, 2, self.size, 1))
        self.habilities.append(self.hability(9, nome[1] + k, descricao[1], custo, 3, self.size, 1))
        self.habilities.append(self.hability(10, nome[3] + k, descricao[3], custo, 3, self.size, 1))
        self.habilities.append(self.hability(11, nome[4] + k, descricao[4], custo, 3, self.size, 1))
        self.habilities.append(self.hability(12, nome[5] + k, descricao[5], custo, 4, self.size, 1))
        self.habilities.append(self.hability(13, nome[6] + k, descricao[6], custo, 5, self.size, 1))
        self.habilities.append(self.hability(14, nome[7] + k, descricao[7], custo, 5, self.size, 1))    
        self.habilities.append(self.hability(15, nome[8] + k, descricao[8], custo, 6, self.size, 1))
        self.habilities.append(self.hability(16, nome[9] + k, descricao[9], custo, 6, self.size, 1))
        self.habilities.append(self.hability(17, nome[10] + k, descricao[10], custo, 6, self.size, 1))
        self.habilities.append(self.hability(18, nome[11] + k, descricao[11], custo, 7, self.size, 1))
        k = " II"
        # linha 2
        self.habilities.append(self.hability(19, nome[0] + k, descricao[0], custo, 8, self.size, 1))
        self.habilities.append(self.hability(20, nome[1] + k, descricao[1], custo, 9, self.size, 1))
        self.habilities.append(self.hability(21, nome[3] + k, descricao[3], custo, 10, self.size, 1))
        self.habilities.append(self.hability(22, nome[4] + k, descricao[4], custo, 11, self.size, 1))
        self.habilities.append(self.hability(23, nome[5] + k, descricao[5], custo, 12, self.size, 1))
        self.habilities.append(self.hability(24, nome[6] + k, descricao[6], custo, 13, self.size, 1))
        self.habilities.append(self.hability(25, nome[7] + k, descricao[7], custo, 14, self.size, 1))
        self.habilities.append(self.hability(26, nome[8] + k, descricao[8], custo, 15, self.size, 1))
        self.habilities.append(self.hability(27, nome[9] + k, descricao[9], custo, 16, self.size, 1))
        self.habilities.append(self.hability(28, nome[10] + k, descricao[10], custo, 17, self.size, 1))
        self.habilities.append(self.hability(29, nome[11] + k, descricao[11], custo, 18, self.size, 1))
        k = " III"
        # linha 3
        self.habilities.append(self.hability(30, nome[0] + k, descricao[0], custo, 19, self.size, 1))
        self.habilities.append(self.hability(31, nome[2] + " I", descricao[2], custo, 20, self.size, 1))
        self.habilities.append(self.hability(32, nome[3] + k, descricao[3], custo, 21, self.size, 1))
        self.habilities.append(self.hability(33, nome[4] + k, descricao[4], custo, 22, self.size, 1))
        self.habilities.append(self.hability(34, nome[5] + k, descricao[5], custo, 23, self.size, 1))
        self.habilities.append(self.hability(35, nome[6] + k, descricao[6], custo, 24, self.size, 1))
        self.habilities.append(self.hability(36, nome[7] + k, descricao[7], custo, 25, self.size, 1))
        self.habilities.append(self.hability(37, nome[8] + k, descricao[8], custo, 26, self.size, 1))
        self.habilities.append(self.hability(38, nome[9] + k, descricao[9], custo, 27, self.size, 1))
        self.habilities.append(self.hability(39, nome[10] + k, descricao[10], custo, 28, self.size, 1))
        self.habilities.append(self.hability(40, nome[11] + k, descricao[11], custo, 29, self.size, 1))
        k = " IV"
        # linha 4
        self.habilities.append(self.hability(41, nome[0] + k, descricao[0], custo, 30, self.size, 1))
        self.habilities.append(self.hability(42, nome[2] + " II", descricao[2], custo, 31, self.size, 1))
        self.habilities.append(self.hability(43, nome[3] + k, descricao[3], custo, 32, self.size, 1))
        self.habilities.append(self.hability(44, nome[4] + k, descricao[4], custo, 33, self.size, 1))
        self.habilities.append(self.hability(45, nome[5] + k, descricao[5], custo, 34, self.size, 1))
        self.habilities.append(self.hability(46, nome[6] + k, descricao[6], custo, 35, self.size, 1))
        self.habilities.append(self.hability(47, nome[7] + k, descricao[7], custo, 36, self.size, 1))
        self.habilities.append(self.hability(48, nome[8] + k, descricao[8], custo, 37, self.size, 1))
        self.habilities.append(self.hability(49, nome[9] + k, descricao[9], custo, 38, self.size, 1))
        self.habilities.append(self.hability(50, nome[10] + k, descricao[10], custo, 39, self.size, 1))
        self.habilities.append(self.hability(51, nome[11] + k, descricao[11], custo, 40, self.size, 1))
        k = " V"
        # linha 5
        self.habilities.append(self.hability(52, nome[0] + k, descricao[0], custo, 41, self.size, 1))
        self.habilities.append(self.hability(53, nome[2] + " III", descricao[2], custo, 42, self.size, 1))
        self.habilities.append(self.hability(54, nome[3] + k, descricao[3], custo, 43, self.size, 1))
        self.habilities.append(self.hability(55, nome[4] + k, descricao[4], custo, 44, self.size, 1))
        self.habilities.append(self.hability(56, nome[5] + k, descricao[5], custo, 45, self.size, 1))
        self.habilities.append(self.hability(57, nome[6] + k, descricao[6], custo, 46, self.size, 1))
        self.habilities.append(self.hability(58, nome[7] + k, descricao[7], custo, 47, self.size, 1))
        self.habilities.append(self.hability(59, nome[8] + k, descricao[8], custo, 48, self.size, 1))
        self.habilities.append(self.hability(60, nome[9] + k, descricao[9], custo, 49, self.size, 1))
        self.habilities.append(self.hability(61, nome[10] + k, descricao[10], custo, 50, self.size, 1))
        self.habilities.append(self.hability(62, nome[11] + k, descricao[11], custo, 51, self.size, 1))

        # discionario de habilidades {id: status}
        self.habilities_status = {}
        self.habilities_status[-1] = 2
        self.load_game()
        for i in range(len(self.classes)):
            self.habilities_status[self.classes[i].id] = self.classes[i].status
        for i in range(len(self.subClasses)):
            self.habilities_status[self.subClasses[i].id] = self.subClasses[i].status
        for i in range(len(self.habilities)):
            self.habilities_status[self.habilities[i].id] = self.habilities[i].status

        self.habilities_per_row = 11

    def save_game(self):
        # salva habilities_status em um arquivo habilities.txt
        with open("habilities.txt", "w") as file:
            for i in range(len(self.habilities_status)-1):
                file.write(str(self.habilities_status[i]) + "\n")
    
    def load_game(self):
        # se o arquivo habilities.txt existir, carrega as habilidades
        if os.path.exists("habilities.txt"):
            with open("habilities.txt", "r") as file:
                # passar por todas as linhas do arquivo
                for i in range(63):
                    self.habilities_status[i] = int(file.readline())
            # atualiza o status das habilidades
            for i in range(len(self.classes)):
                self.classes[i].status = self.habilities_status[self.classes[i].id]
            for i in range(len(self.subClasses)):
                self.subClasses[i].status = self.habilities_status[self.subClasses[i].id]
            for i in range(len(self.habilities)):
                self.habilities[i].status = self.habilities_status[self.habilities[i].id]


    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.constants.running = False
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.constants.state = 1
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    if self.selected > 0:
                        self.selected -= 1
                if event.key == pg.K_RIGHT:
                    if self.selected < 62:
                        self.selected += 1
                if event.key == pg.K_UP:
                    if self.selected < 5:
                        self.selected = 0
                    elif self.selected < 8:
                        self.selected = 1
                    elif self.selected == 8:
                        self.selected = 2
                    elif self.selected < 12:
                        self.selected = 3
                    elif self.selected == 12:
                        self.selected = 4
                    elif self.selected < 15:
                        self.selected = 5
                    elif self.selected < 18:
                        self.selected = 6
                    elif self.selected == 18:
                        self.selected = 7
                    else:
                        self.selected -= 11
                if event.key == pg.K_DOWN:
                    if self.selected == 0:
                        self.selected = 2
                    elif self.selected == 1:
                        self.selected = 5
                    elif self.selected == 2:
                        self.selected = 8
                    elif self.selected == 3:
                        self.selected = 9
                    elif self.selected == 4:
                        self.selected = 12
                    elif self.selected == 5:
                        self.selected = 13
                    elif self.selected == 6:
                        self.selected = 15
                    elif self.selected == 7:
                        self.selected = 18
                    else:
                        if self.selected + 11 < 63:
                            self.selected += 11
                if event.key == pg.K_RETURN:
                    if self.habilities_status[self.selected] == 1:
                        # achar se o selecionado esta em classe subclasse ou habilidade
                        for i in range(len(self.classes)):
                            if self.classes[i].id == self.selected and self.constants.player_coins >= self.classes[i].cost:
                                self.classes[i].status = 2
                                self.habilities_status[self.selected] = 2
                                self.constants.player_coins -= self.classes[i].cost
                        for i in range(len(self.subClasses)):
                            if self.subClasses[i].id == self.selected and self.constants.player_coins >= self.subClasses[i].cost:
                                self.subClasses[i].status = 2
                                self.habilities_status[self.selected] = 2
                                self.constants.player_coins -= self.subClasses[i].cost
                        for i in range(len(self.habilities)):
                            if self.habilities[i].id == self.selected and self.constants.player_coins >= self.habilities[i].cost:
                                self.habilities[i].status = 2
                                self.habilities_status[self.selected] = 2
                                self.constants.player_coins -= self.habilities[i].cost
                                self.apply_hability(self.habilities[i].id)
    nome = ['Ganância', 'Precisão', 'Tempo', 'Dano', 'Munição', 'Furtividade', 'Resistência física', 'Resistência bala', 'Vida' ,'Mais Frascos' ,'Mais Achados' , 'Velocidade']
        
    def apply_hability(self, id):
        idb = id - 8
        idb = idb % 11
        if idb == 0:
            self.constants.coins_factor += 0.1
        elif idb == 1:
            self.constants.time_factor += 0.3
        elif idb == 2:
            self.constants.damage_factor += 0.1
        elif idb == 3:
            self.constants.ammo_factor += 0.2
        elif idb == 4:
            self.constants.furtivity_factor += 0.1
        elif idb == 5:
            self.constants.short_range_factor += 0.1
        elif idb == 6:
            self.constants.long_range_factor += 0.1
        elif idb == 7:
            self.constants.health_factor += 0.1
        elif idb == 8:
            self.constants.flasks_factor += 1
        elif idb == 9:
            self.constants.flask_room += 1
        elif idb == 10:
            self.constants.speed_factor  += 0.1
    
    def update(self):
        # passar por todas as classes subclasses e habiliades atualizando
        for i in range(len(self.classes)):
            if self.classes[i].id == self.selected:
                self.classes[i].selected = True
            else:
                self.classes[i].selected = False

            # so atualiza se não foi comprado ainda
            if self.classes[i].status == 2:
                pass
            # se o status do pai for 2, e o dinheiro for maior que o custo, entao o status do filho passa a ser 1
            elif self.habilities_status[self.classes[i].father] == 2 and self.constants.player_coins >= self.classes[i].cost and self.classes[i].status == 0:
                self.classes[i].status = 1
                self.habilities_status[self.classes[i].id] = 1
            # se o status do pai for 2, e o dinheiro for menor que o custo, entao o status do filho passa a ser 0
            elif self.habilities_status[self.classes[i].father] == 2 and self.constants.player_coins < self.classes[i].cost:
                self.classes[i].status = 0
                self.habilities_status[self.classes[i].id] = 0
            # se o status do pai for 1, entao o status do filho passa a ser 0
            elif self.habilities_status[self.classes[i].father] == 1:
                self.classes[i].status = 0
                self.habilities_status[self.classes[i].id] = 0
            # se o status do pai for 0, entao o status do filho passa a ser 0
            elif self.habilities_status[self.classes[i].father] == 0:
                self.classes[i].status = 0
                self.habilities_status[self.classes[i].id] = 0
            
        for i in range(len(self.subClasses)):
            if self.subClasses[i].id == self.selected:
                self.subClasses[i].selected = True
            else:
                self.subClasses[i].selected = False
            # so atualiza se não foi comprado ainda
            if self.subClasses[i].status == 2:
                pass
            # se o status do pai for 2, e o dinheiro for maior que o custo, entao o status do filho passa a ser 1
            elif self.habilities_status[self.subClasses[i].father] == 2 and self.constants.player_coins >= self.subClasses[i].cost and self.subClasses[i].status == 0:
                self.subClasses[i].status = 1
                self.habilities_status[self.subClasses[i].id] = 1
            # se o status do pai for 2, e o dinheiro for menor que o custo, entao o status do filho passa a ser 0
            elif self.habilities_status[self.subClasses[i].father] == 2 and self.constants.player_coins < self.subClasses[i].cost:
                self.subClasses[i].status = 0
                self.habilities_status[self.subClasses[i].id] = 0
            # se o status do pai for 1, entao o status do filho passa a ser 0
            elif self.habilities_status[self.subClasses[i].father] == 1:
                self.subClasses[i].status = 0
                self.habilities_status[self.subClasses[i].id] = 0
            # se o status do pai for 0, entao o status do filho passa a ser 0
            elif self.habilities_status[self.subClasses[i].father] == 0:
                self.subClasses[i].status = 0
                self.habilities_status[self.subClasses[i].id] = 0

        for i in range(len(self.habilities)):
            if self.habilities[i].id == self.selected:
                self.habilities[i].selected = True
            else:
                self.habilities[i].selected = False

            # so atualiza se não foi comprado ainda
            if self.habilities[i].status == 2:
                pass
            # se o status do pai for 2, e o dinheiro for maior que o custo, entao o status do filho passa a ser 1
            elif self.habilities_status[self.habilities[i].father] == 2 and self.constants.player_coins >= self.habilities[i].cost and self.habilities[i].status == 0:
                self.habilities[i].status = 1
                self.habilities_status[self.habilities[i].id] = 1
            # se o status do pai for 2, e o dinheiro for menor que o custo, entao o status do filho passa a ser 0
            elif self.habilities_status[self.habilities[i].father] == 2 and self.constants.player_coins < self.habilities[i].cost:
                self.habilities[i].status = 0
                self.habilities_status[self.habilities[i].id] = 0
            # se o status do pai for 1, entao o status do filho passa a ser 0
            elif self.habilities_status[self.habilities[i].father] == 1:
                self.habilities[i].status = 0
                self.habilities_status[self.habilities[i].id] = 0
            # se o status do pai for 0, entao o status do filho passa a ser 0
            elif self.habilities_status[self.habilities[i].father] == 0:
                self.habilities[i].status = 0
                self.habilities_status[self.habilities[i].id] = 0
            
        
    def draw(self):
        # desenhar fundo
        self.screen.fill((0,0,0))
        # desenhar titulo
        self.draw_title()
        # desenhar linhas
        self.draw_lines()
        # desenhar arvore de habilidades
        self.draw_tree()
        # desenhar moedas
        self.draw_coins()
        # desenhar descrição
        self.draw_description()

    def draw_title(self):
        # desenhar o titulo na tela
        text = self.font_title.render("Árvore de Habilidades", True, (255,255,255))
        self.screen.blit(text, (self.constants.width/2 - text.get_width()/2, self.padding*2))

    def draw_description(self):
        # desenhar a descrição do selecionado na arvore no meio da tela em baixo
        if self.selected != -1:
            description = self.get_description(self.selected)
            name = self.get_name(self.selected)
            text = self.font_decription.render(name+": "+description, True, (210,0,0))
            self.screen.blit(text, (self.constants.width/2 - text.get_width()/2, self.constants.height - self.padding - text.get_height()))

    def get_description(self, id):
        for i in range(len(self.classes)):
            if self.classes[i].id == id:
                return self.classes[i].description
        for i in range(len(self.subClasses)):
            if self.subClasses[i].id == id:
                return self.subClasses[i].description
        for i in range(len(self.habilities)):
            if self.habilities[i].id == id:
                return self.habilities[i].description
    
    def get_name(self, id):
        for i in range(len(self.classes)):
            if self.classes[i].id == id:
                return self.classes[i].name
        for i in range(len(self.subClasses)):
            if self.subClasses[i].id == id:
                return self.subClasses[i].name
        for i in range(len(self.habilities)):
            if self.habilities[i].id == id:
                return self.habilities[i].name

    def draw_tree(self):
        space = (self.constants.width - 2*self.constants.padding)/11
        x = self.padding*2
        y = self.padding*8
        for i in range(len(self.classes)):
            xa = x + ((self.classes[i].hor_space-1)/2)*space
            self.classes[i].draw(self.screen, xa, y)
            self.classes[i].x = xa
            self.classes[i].y = y
            x += self.classes[i].hor_space*space
        x = self.padding*2
        y += self.size*2
        for i in range(len(self.subClasses)):
            xa = x + ((self.subClasses[i].hor_space-1)/2)*space
            self.subClasses[i].draw(self.screen, xa, y)
            self.subClasses[i].x = xa
            self.subClasses[i].y = y
            x += self.subClasses[i].hor_space*space
        x = self.padding*2
        y += self.size*2
        x_max = x + (self.habilities_per_row-1)*space
        for i in range(len(self.habilities)):
            xa = x + ((self.habilities[i].hor_space-1)/2)*space
            if xa > x_max:
                x = self.padding*2
                y += self.size*2
                xa = x + ((self.habilities[i].hor_space-1)/2)*space
            self.habilities[i].draw(self.screen, xa, y)
            self.habilities[i].x = xa
            self.habilities[i].y = y
            x += self.habilities[i].hor_space*space
    
    def draw_lines(self):
        for i in range(len(self.classes)):
            for j in range(len(self.subClasses)):
                if self.subClasses[j].father == self.classes[i].id:
                    pg.draw.line(self.screen, (255,255,255), (self.classes[i].x+self.size/2, self.classes[i].y+self.size), (self.subClasses[j].x+self.size/2, self.subClasses[j].y), 1)
        for i in range(len(self.subClasses)):
            for j in range(len(self.habilities)):
                if self.habilities[j].father == self.subClasses[i].id:
                    pg.draw.line(self.screen, (255,255,255), (self.subClasses[i].x+self.size/2, self.subClasses[i].y+self.size), (self.habilities[j].x+self.size/2, self.habilities[j].y), 1)
        
        for i in range(len(self.habilities)):
            for j in range(len(self.habilities)):
                if self.habilities[j].father == self.habilities[i].id:
                    pg.draw.line(self.screen, (255,255,255), (self.habilities[i].x+self.size/2, self.habilities[i].y+self.size), (self.habilities[j].x+self.size/2, self.habilities[j].y), 1)

    def draw_coins(self):
        # desenha moedas no canto direito inferior
        text = self.font.render("Recursos: "+str(int(self.constants.player_coins)), True, (255,255,255))
        self.screen.blit(text, (self.constants.width - text.get_width() - self.padding, self.constants.height - text.get_height() - self.padding))

    class hability:
        def __init__(self,id , name, description, cost, father, size, hor_space):
            self.id = id
            self.name = name
            self.description = description
            self.cost = cost
            self.father = father
            self.size = size
            # self.icon_0 = pg.image.load('assets/icons/habilityTree/' + name + '_0.png')
            # self.icon_0 = pg.transform.scale(self.icon_0, (size, size))
            # self.icon_1 = pg.image.load('assets/icons/habilityTree/' + name + '_1.png')
            # self.icon_1 = pg.transform.scale(self.icon_1, (size, size))
            self.icon_0 = pg.image.load('assets/icons/habilityTree/' + 'accuracy' + '_0.png')
            self.icon_0 = pg.transform.scale(self.icon_0, (size, size))
            self.icon_1 = pg.image.load('assets/icons/habilityTree/' + 'accuracy' + '_1.png')
            self.icon_1 = pg.transform.scale(self.icon_1, (size, size))
            self.status = 0
            self.selected = False
            self.hor_space = hor_space
            self.x = 0
            self.y = 0

        def draw(self, screen, x, y):
            if self.status == 0:
                # desenhar fundo cinza do icone circular
                pg.draw.circle(screen, (30, 30, 30), (x + self.size//2, y + self.size//2), self.size//2+self.size//10)
                screen.blit(self.icon_0, (x, y))
            elif self.status == 1:
                # desenhar fundo cinza do icone circular
                pg.draw.circle(screen, (150, 150, 150), (x + self.size//2, y + self.size//2), self.size//2+self.size//10)
                screen.blit(self.icon_0, (x, y))
            elif self.status == 2:
                # desenhar fundo cinza do icone circular
                pg.draw.circle(screen, (150, 150, 150), (x + self.size//2, y + self.size//2), self.size//2+self.size//10)
                screen.blit(self.icon_1, (x, y))
            
            if self.selected:
                # desenhar circulo vermelho
                pg.draw.circle(screen, (255, 0, 0), (x + self.size//2, y + self.size//2), self.size//2 + self.size//10, self.size//20)
            else:
                # desenhar circulo branco
                pg.draw.circle(screen, (255, 255, 255), (x + self.size//2, y + self.size//2), self.size//2 + self.size//10, self.size//20)
    