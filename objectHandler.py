from random import choices, randrange
from spriteObject import AnimatedSprite, SpriteObject
from enemies import *

class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.enemies_list = []
        self.enemies_sprite_path = 'Recursos/Inimigos/'
        self.static_sprite_path = 'Recursos/static_sprites/'
        self.anim_sprite_path = 'Recursos/animated_sprites/'
        add_sprite = self.add_sprite
        add_enemy = self.add_enemy
        self.enemies_positions = {}

        # spawn npc
        # self.enemies = 20  # npc count
        self.enemy_types = [SoldierNPC, CacoDemonNPC]
        self.weights = [70, 30]
        # self.restricted_area = {(i, j) for i in range(10) for j in range(10)}
        # self.spawn_npc()

        # sprite map
        # add_sprite(AnimatedSprite(game))
        # add_sprite(SpriteObject(game))
        # add_sprite(AnimatedSprite(game, pos=(1.5, 1.5)))
        # add_sprite(AnimatedSprite(game, pos=(1.5, 7.5)))
        # add_sprite(AnimatedSprite(game, pos=(5.5, 3.25)))
        # add_sprite(AnimatedSprite(game, pos=(5.5, 4.75)))
        # add_sprite(AnimatedSprite(game, pos=(7.5, 2.5)))
        # add_sprite(AnimatedSprite(game, pos=(7.5, 5.5)))
        # add_sprite(AnimatedSprite(game, pos=(14.5, 1.5)))
        # add_sprite(AnimatedSprite(game, pos=(14.5, 4.5)))
        # add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(14.5, 5.5)))
        # add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(14.5, 7.5)))
        # add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(12.5, 7.5)))
        # add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(9.5, 7.5)))
        # add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(14.5, 12.5)))
        # add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(9.5, 20.5)))
        # add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(10.5, 20.5)))
        # add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(3.5, 14.5)))
        # add_sprite(AnimatedSprite(game, path=self.anim_sprite_path + 'red_light/0.png', pos=(3.5, 18.5)))
        # add_sprite(AnimatedSprite(game, pos=(14.5, 24.5)))
        # add_sprite(AnimatedSprite(game, pos=(14.5, 30.5)))
        # add_sprite(AnimatedSprite(game, pos=(1.5, 30.5)))
        # add_sprite(AnimatedSprite(game, pos=(1.5, 24.5)))

        # npc map
        
        # add_npc(SoldierNPC(game, pos=(13.5, 6.5)))
        # add_npc(SoldierNPC(game, pos=(2.0, 20.0)))
        # add_npc(SoldierNPC(game, pos=(4.0, 29.0)))
        # add_npc(CacoDemonNPC(game, pos=(5.5, 14.5)))
        # add_npc(CacoDemonNPC(game, pos=(5.5, 16.5)))
        # add_npc(CyberDemonNPC(game, pos=(14.5, 25.5)))

    # def spawn_npc(self):
    #     for i in range(self.enemies):
    #             npc = choices(self.npc_types, self.weights)[0]
    #             pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
    #             while (pos in self.game.map.world_map) or (pos in self.restricted_area):
    #                 pos = x, y = randrange(self.game.map.cols), randrange(self.game.map.rows)
    #             self.add_npc(npc(self.game, pos=(x + 0.5, y + 0.5)))

    def spawn_enemies(self, number):
        for i in range(number):
            enemy = choices(self.enemy_types, self.weights)[0]
            x, y = randrange(self.game.constants.map_height), randrange(self.game.constants.map_width)
            while (x, y) not in self.game.gameMap.map_inversed:
                x, y = randrange(self.game.constants.map_height), randrange(self.game.constants.map_width)

            self.add_enemy(enemy(self.game, pos=(x + 0.5, y + 0.5)))

            
    # def check_win(self):
    #     if not len(self.npc_positions):
    #         self.game.object_renderer.win()
    #         pg.display.flip()
    #         pg.time.delay(1500)
    #         self.game.new_game()

    def update(self):
        self.enemy_positions = {enemy.map_pos for enemy in self.enemies_list if enemy.alive}
        [sprite.update() for sprite in self.sprite_list]
        [enemy.update() for enemy in self.enemies_list]
        # self.check_win()
    
    def remove_enemies(self):
        self.enemies_list = []

    def add_enemy(self, enemy):
        self.enemies_list.append(enemy)

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)