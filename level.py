import pygame.sprite
from enemy import Enemy
from player import Player
from settings import *
from support import *
from tile import Tile
from ui import UI
from weapon import Weapon
from particles import AnimationPlayer
from magic import MagicPlayer
from upgrade import Upgrade
from escape import Escape
import settings
from tkinter import *
import tkinter


class Level:
    def __init__(self):

        # get the display surface
        self.exit_page = None
        self.display_surface = pygame.display.get_surface()
        self.game_paused = False
        self.escape_true = False

        # sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()

        # Attack Sprites
        self.current_attack = None
        self.attack_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()

        self.is_boss = False
        self.is_dead_now = False

        global boundary
        global walls
        global floor
        global decorations
        global mobs

        if settings.level_loaded == 1:
            boundary = "../map/Maze_Wall_Blocks .csv"
            walls = '../map/Maze_Wall_Blocks .csv'
            floor = '../map/Maze_Walls.csv'
            decorations = '../map/Maze_Decorations .csv'
            mobs = '../map/Maze_Entity.csv'
        if settings.level_loaded == 2:
            boundary = "none"
            walls = "none"
            floor = "none"
            decorations = "none"
            mobs = "none"
            # self.boundary = import_csv_layout()
            # self.walls = import_csv_layout('../map/Maze_Walls.csv')
            # self.floor = import_csv_layout('../map/Maze_Floor .csv')
            # self.decorations = import_csv_layout('../map/Maze_Decorations .csv')
            # self.mobs = import_csv_layout('../map/Maze_Entity.csv')

        # sprite setup
        self.create_map()

        # user interface
        self.ui = UI()
        self.upgrade = Upgrade(self.player)
        # self.escape = Escape(self.player)
        self.escape = Escape(self.player)

        # particles
        self.animation_player = AnimationPlayer()
        self.magic_player = MagicPlayer(self.animation_player)

    def create_map(self):
        layouts = {
            'boundary': import_csv_layout(boundary),
            'walls': import_csv_layout(walls),
            'floor': import_csv_layout(floor),
            'decorations': import_csv_layout(decorations),
            'entities': import_csv_layout(mobs),
        }
        graphics = {
            'floor': import_folder('../graphics/Floor'),
            'walls': import_folder('../graphics/walls'),
            'decorations': import_folder('../graphics/Static_Decorations')
        }

        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boundary':
                            Tile((x, y), [self.obstacle_sprites], 'invisible')
                        if style == 'decorations':
                            surf_2 = graphics['decorations'][int(col)]
                            Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'decorations', surf_2)
                        if style == 'entities':
                            if col == '0':
                                self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites, self.create_attack, self.destroy_attack, self.create_Magic)
                            else:
                                if col == '1':
                                    monster_name = 'chort'
                                    self.is_boss = True
                                if col == '2': monster_name = 'goblin'
                                if col == '3': monster_name = 'ice_zombie'
                                if col == '4': monster_name = 'imp'
                                if col == '5': monster_name = 'lizard_female'
                                if col == '6': monster_name = 'lizard_male'
                                if col == '7': monster_name = 'masked_orc'
                                if col == '8': monster_name = 'necromancer'
                                if col == '9': monster_name = 'orc_shaman'
                                if col == '10': monster_name = 'skeleton'
                                if col == '11': monster_name = 'spirit'
                                if col == '12': monster_name = 'swampy'
                                if col == '13': monster_name = 'zombie'
                                if col == '14': monster_name = 'muddy'
                                if col == '15': monster_name = 'orc_warrior'
                                if col == '16': monster_name = 'wogol'
                                if col == '17': monster_name = 'big_demon'
                                if col == '18': monster_name = 'big_zombie'
                                if col == '19': monster_name = 'ogre'

                                Enemy(monster_name, (x, y), [self.visible_sprites, self.attackable_sprites, self.enemy_sprites], self.obstacle_sprites, self.damage_player,
                                      self.trigger_death_particles,
                                      self.add_exp, self.is_boss, self.is_dead)

    # self.player = Player((256,256),[self.visible_sprites] , self.obstacle_sprites, self.create_attack,self.destroy_attack, self.create_Magic)

    def create_attack(self):
        self.current_attack = Weapon(self.player, [self.visible_sprites, self.attack_sprites])

    def create_Magic(self, style, strength, cost):
        if style == 'heal':
            self.magic_player.heal(self.player, strength, cost, [self.visible_sprites])
        if style == "flame":
            self.magic_player.flame(self.player, cost, [self.visible_sprites, self.attack_sprites])

    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def player_attack_logic(self):
        if self.attack_sprites:
            for attack_sprite in self.attack_sprites:
                collision_sprites = pygame.sprite.spritecollide(attack_sprite, self.attackable_sprites, False)
                if collision_sprites:
                    for target_sprite in collision_sprites:
                        target_sprite.get_damage(self.player, attack_sprite.sprite_type)

    def damage_player(self, amount, attack_type):
        if self.player.vulnerable:
            self.player.health -= amount
            self.player.vulnerable = False
            self.player.hurt_time = pygame.time.get_ticks()
            self.animation_player.create_particles(attack_type, self.player.rect.center, [self.visible_sprites])

    def trigger_death_particles(self, pos, particle_type):
        self.animation_player.create_particles(particle_type, pos, self.visible_sprites)

    def add_exp(self, amount):
        self.player.exp += amount

    def is_dead(self, val):
        self.is_dead_now = val

    def toggle_menu(self):
        if self.escape_true:
            self.escape_true = not self.escape_true
        self.game_paused = not self.game_paused

    def toggle_escape(self):
        if self.game_paused:
            self.game_paused = not self.game_paused
        self.escape_true = not self.escape_true

    def run(self):

        self.visible_sprites.custom_draw(self.player)
        self.ui.display(self.player)
        if self.game_paused:
            self.upgrade.display()
        elif self.escape_true:
            self.escape.display()
        else:

            self.visible_sprites.update()
            self.visible_sprites.enemy_update(self.player, self.enemy_sprites)
            self.player_attack_logic()


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        # general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        # creating the floor
        self.floor_surf = pygame.image.load('../map/Maze.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft=(0, 0))

    def custom_draw(self, player):
        # getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # drawing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)

        # for sprite in self.sprites():
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

    def enemy_update(self, player, enemy_sprite_group):
        # enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'enemy']
        for enemy in enemy_sprite_group:
            enemy.enemy_updates(player)
