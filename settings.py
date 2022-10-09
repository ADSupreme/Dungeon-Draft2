# game setup
WIDTH = 1280
HEIGTH = 720
FPS = 60
TILESIZE = 64

Player_val = 1
difficulty_rating = 1
level_loaded = 1
# time_stop = False

# ui
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = '../graphics/font/joystix.ttf'
UI_FONT_SIZE = 18

# general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

# ui colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

# upgrade menu
TEXT_COLOR_SELECTED = '#111111'
BAR_COLOR = '#EEEEEE'
BAR_COLOR_SELECTED = '#111111'
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE'

# weapons
weapon_data = {
    'fists': {'cooldown': 0, 'damage': 5, 'graphic': '../graphics/weapons/fists/full.png'},
    'sword': {'cooldown': 100, 'damage': 15, 'graphic': '../graphics/weapons/sword/full.png'},
    'lance': {'cooldown': 400, 'damage': 30, 'graphic': '../graphics/weapons/lance/full.png'},
    'axe': {'cooldown': 300, 'damage': 20, 'graphic': '../graphics/weapons/axe/full.png'},
    'rapier': {'cooldown': 50, 'damage': 8, 'graphic': '../graphics/weapons/rapier/full.png'},
    'sai': {'cooldown': 80, 'damage': 10, 'graphic': '../graphics/weapons/sai/full.png'}}

# magic
magic_data = {
    'flame': {'strength': 5, 'cost': 20, 'graphic': '../graphics/particles/flame/fire.png'},
    'heal': {'strength': 20, 'cost': 10, 'graphic': '../graphics/particles/heal/heal.png'}}

# enemy
monster_data = {
    'chort': {'health': 100 * difficulty_rating, 'exp': 100, 'damage': 20 * difficulty_rating, 'attack_type': 'slash', 'attack_sound': '../audio/attack/slash.wav', 'speed': 3, 'resistance': 3,
              'attack_radius': 80,
              'notice_radius': 360},
    'goblin': {'health': 100 * difficulty_rating, 'exp': 100, 'damage': 20 * difficulty_rating, 'attack_type': 'slash', 'attack_sound': '../audio/attack/slash.wav', 'speed': 3, 'resistance': 3,
               'attack_radius': 80,
               'notice_radius': 360},
    'ice_zombie': {'health': 100 * difficulty_rating, 'exp': 100, 'damage': 20 * difficulty_rating, 'attack_type': 'slash', 'attack_sound': '../audio/attack/slash.wav', 'speed': 3, 'resistance': 3,
                   'attack_radius': 80,
                   'notice_radius': 360},
    'imp': {'health': 100 * difficulty_rating, 'exp': 100, 'damage': 20 * difficulty_rating, 'attack_type': 'slash', 'attack_sound': '../audio/attack/slash.wav', 'speed': 3, 'resistance': 3,
            'attack_radius': 80,
            'notice_radius': 360},
    'lizard_female': {'health': 100 * difficulty_rating, 'exp': 100, 'damage': 20 * difficulty_rating, 'attack_type': 'slash', 'attack_sound': '../audio/attack/slash.wav', 'speed': 3, 'resistance': 3,
                      'attack_radius': 80,
                      'notice_radius': 360},
    'lizard_male': {'health': 100 * difficulty_rating, 'exp': 100, 'damage': 20 * difficulty_rating, 'attack_type': 'slash', 'attack_sound': '../audio/attack/slash.wav', 'speed': 3, 'resistance': 3,
                    'attack_radius': 80,
                    'notice_radius': 360},
    'squid': {'health': 100, 'exp': 100, 'damage': 20, 'attack_type': 'slash', 'attack_sound': '../audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 80, 'notice_radius': 360},
    'masked_orc': {'health': 100 * difficulty_rating, 'exp': 100, 'damage': 20 * difficulty_rating, 'attack_type': 'slash', 'attack_sound': '../audio/attack/slash.wav', 'speed': 3, 'resistance': 3,
                   'attack_radius': 80,
                   'notice_radius': 360},
    'necromancer': {'health': 300 * difficulty_rating, 'exp': 250, 'damage': 40 * difficulty_rating, 'attack_type': 'claw', 'attack_sound': '../audio/attack/claw.wav', 'speed': 5, 'resistance': 3,
                    'attack_radius': 120,
                    'notice_radius': 400},
    'spirit': {'health': 100 * difficulty_rating, 'exp': 110, 'damage': 8 * difficulty_rating, 'attack_type': 'thunder', 'attack_sound': '../audio/attack/fireball.wav', 'speed': 5, 'resistance': 3,
               'attack_radius': 60,
               'notice_radius': 350},
    'bamboo': {'health': 70 * difficulty_rating, 'exp': 120, 'damage': 6 * difficulty_rating, 'attack_type': 'leaf_attack', 'attack_sound': '../audio/attack/slash.wav', 'speed': 5, 'resistance': 3,
               'attack_radius': 50,
               'notice_radius': 300},
    'muddy': {'health': 100 * difficulty_rating, 'exp': 100, 'damage': 20 * difficulty_rating, 'attack_type': 'slash', 'attack_sound': '../audio/attack/slash.wav', 'speed': 5, 'resistance': 3,
              'attack_radius': 80,
              'notice_radius': 360},
    'orc_shaman': {'health': 100 * difficulty_rating, 'exp': 100, 'damage': 20 * difficulty_rating, 'attack_type': 'slash', 'attack_sound': '../audio/attack/slash.wav', 'speed': 5, 'resistance': 3,
                   'attack_radius': 80,
                   'notice_radius': 360},
    'skeleton': {'health': 100 * difficulty_rating, 'exp': 100, 'damage': 20 * difficulty_rating, 'attack_type': 'slash', 'attack_sound': '../audio/attack/slash.wav', 'speed': 3, 'resistance': 3,
                 'attack_radius': 80,
                 'notice_radius': 360},
    'swampy': {'health': 100 * difficulty_rating, 'exp': 100, 'damage': 20 * difficulty_rating, 'attack_type': 'slash', 'attack_sound': '../audio/attack/slash.wav', 'speed': 3, 'resistance': 3,
               'attack_radius': 80,
               'notice_radius': 360},
    'tiny_zombie': {'health': 100 * difficulty_rating, 'exp': 100, 'damage': 20 * difficulty_rating, 'attack_type': 'slash', 'attack_sound': '../audio/attack/slash.wav', 'speed': 3, 'resistance': 3,
                    'attack_radius': 80,
                    'notice_radius': 360},
    'zombie': {'health': 100 * difficulty_rating, 'exp': 100, 'damage': 20 * difficulty_rating, 'attack_type': 'slash', 'attack_sound': '../audio/attack/slash.wav', 'speed': 3, 'resistance': 3,
               'attack_radius': 80,
               'notice_radius': 360},
    'orc_warrior': {'health': 100 * difficulty_rating, 'exp': 100, 'damage': 20 * difficulty_rating, 'attack_type': 'slash', 'attack_sound': '../audio/attack/slash.wav', 'speed': 3, 'resistance': 3,
                    'attack_radius': 80,
                    'notice_radius': 360},
    'wogol': {'health': 100 * difficulty_rating, 'exp': 100, 'damage': 20 * difficulty_rating, 'attack_type': 'slash', 'attack_sound': '../audio/attack/slash.wav', 'speed': 3, 'resistance': 3,
              'attack_radius': 80,
              'notice_radius': 360},
    'big_demon': {'health': 100 * difficulty_rating, 'exp': 100, 'damage': 20 * difficulty_rating, 'attack_type': 'slash', 'attack_sound': '../audio/attack/slash.wav', 'speed': 3, 'resistance': 3,
                  'attack_radius': 80,
                  'notice_radius': 360},
    'big_zombie': {'health': 100 * difficulty_rating, 'exp': 100, 'damage': 20 * difficulty_rating, 'attack_type': 'slash', 'attack_sound': '../audio/attack/slash.wav', 'speed': 3, 'resistance': 3,
                   'attack_radius': 80,
                   'notice_radius': 360},
    'ogre': {'health': 100 * difficulty_rating, 'exp': 100, 'damage': 20 * difficulty_rating, 'attack_type': 'slash', 'attack_sound': '../audio/attack/slash.wav', 'speed': 3, 'resistance': 3,
             'attack_radius': 80,
             'notice_radius': 360},
}
