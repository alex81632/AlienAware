from random import choices, randrange, choice
from spriteObject import AnimatedSprite, SpriteObject
from enemies import *
from potion import Potion

class ObjectHandler:
    '''classe que gerencia os objetos do jogo'''
    def __init__(self, game):
        '''inicializa o objeto'''
        self.game = game
        self.sprite_list = []
        self.enemies_list = []
        self.potion_list = []
        self.enemies_sprite_path = 'Recursos/Inimigos/'
        self.static_sprite_path = 'Recursos/static_sprites/'
        self.anim_sprite_path = 'Recursos/animated_sprites/'
        self.enemies_positions = {}
        self.potions_positions = {}
        self.enemy_types = [SoldierNPC, CacoDemonNPC]
        self.weights = [70, 30]

        self.spawn_portal()
        self.spaw_initial_objects()
        
        
        # self.add_sprite(AnimatedSprite(game, pos=(2.5, 6.8)))

        # npc map
        
        # add_npc(SoldierNPC(game, pos=(13.5, 6.5)))
        # add_npc(CacoDemonNPC(game, pos=(5.5, 14.5)))
        # add_npc(CyberDemonNPC(game, pos=(14.5, 25.5)))


    def spaw_initial_objects(self):
        '''spawna os objetos iniciais do mapa'''
        self.add_sprite(AnimatedSprite(self.game, path=self.anim_sprite_path + 'computer/comp_0.png', pos=(2.5, 6.8)))
        self.add_sprite(AnimatedSprite(self.game, path=self.anim_sprite_path + 'vendingMachine/vm_0.png', pos=(4.5, 6.8)))

    def spawn_portal(self):
        '''spawna o portal de saida do mapa'''
        h = self.game.constants.map_height
        w = self.game.constants.map_width
        x = w/2
        y = h - 0.5
        self.add_sprite(AnimatedSprite(self.game, path=self.anim_sprite_path + 'portal/ezgif-frame-001.png', pos=(x, y), scale=1.1, shift=-0.05, animation_time=60))


    def spawn_enemies(self, number):
        '''spawna inimigos aleatorios no mapa'''
        for i in range(number):
            enemy = choices(self.enemy_types, self.weights)[0]
            x, y = choice(list(self.game.gameMap.map_inversed.keys()))
            while y<10:
                x, y = choice(list(self.game.gameMap.map_inversed.keys()))
            self.add_enemy(enemy(self.game, pos=(x + 0.5, y + 0.5)))
    
    def spawn_potions(self, number):
        '''spawna poções aleatorias no mapa'''
        for i in range(number):
            x, y = choice(list(self.game.gameMap.map_inversed.keys()))

            self.add_potion(Potion(self.game, path = 'Recursos\static_sprites\potion.png', pos=(x + 0.5, y + 0.5), scale=0.5, shift=0.8))

            
    # def check_win(self):
    #     if not len(self.npc_positions):
    #         self.game.object_renderer.win()
    #         pg.display.flip()
    #         pg.time.delay(1500)
    #         self.game.new_game()

    def update(self):
        '''atualiza os objetos do jogo'''
        self.enemy_positions = {enemy.map_pos for enemy in self.enemies_list if enemy.alive}
        [sprite.update() for sprite in self.sprite_list]
        [potion.update() for potion in self.potion_list]
        [enemy.update() for enemy in self.enemies_list]
        # self.check_win()
    
    def remove_enemies(self):
        '''remove todos os inimigos do mapa'''
        self.enemies_list = []

    def remove_potion(self, x, y):
        '''remove uma poção do mapa'''
        for i in range(len(self.potion_list)):
            if self.potion_list[i].x == x and self.potion_list[i].y == y:
                remove = i
        self.potion_list.pop(remove)

    def remove_all_potions(self):
        '''remove todas as poções do mapa'''
        self.potion_list = []

    def add_enemy(self, enemy):
        '''adiciona um inimigo ao mapa'''
        self.enemies_list.append(enemy)

    def add_sprite(self, sprite):
        '''adiciona um sprite ao mapa'''
        self.sprite_list.append(sprite)

    def remove_sprite(self, sprite):
        '''remove um sprite do mapa'''
        self.sprite_list.remove(sprite)
    
    def remove_all_sprites(self):
        '''remove todos os sprites do mapa'''
        self.sprite_list = []

    def add_potion(self, potion):
        '''adiciona uma poção ao mapa'''
        self.potion_list.append(potion)