import pygame
from settings import *
import sys


class Escape:
    def __init__(self, player):

        # general setup
        self.display_surface = pygame.display.get_surface()
        self.player = player
        self.attribute_nr = 1
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        # item creation
        self.height = self.display_surface.get_size()[1] * 0.3
        self.width = self.display_surface.get_size()[0] // 3
        self.create_items()

        # selection system
        self.selection_index = 0

    def create_items(self):
        self.item_list = []
        for item, index in enumerate(range(self.attribute_nr)):
            # horizontal position
            full_width = self.display_surface.get_size()[0]
            increment = full_width // self.attribute_nr
            left = (item * increment) + (increment - self.width) // 2
            # vertical position
            top = self.display_surface.get_size()[1] * 0.2
            # create the object
            item = Item(left, top, self.width, self.height, index, self.font)
            self.item_list.append(item)

    def display(self):
        for index, item in enumerate(self.item_list):
            name_1 = "Are you sure"
            cost = "you want to quit?"
            item.display(self.display_surface, self.selection_index, name_1, cost)


class Item:
    def __init__(self, l, t, w, h, index, font):
        self.rect = pygame.Rect(l, t, w, h)
        self.index = index
        self.font = font

        # button
        image = pygame.image.load('../graphics/test/start_btn.png').convert_alpha()
        scale = 0.8
        width = 100
        height = 150
        self.button_image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.button_rect = self.button_image.get_rect(midtop=self.rect.midtop + pygame.math.Vector2(0, 80))
        self.clicked = False
        self.action = None

    def display_names(self, surface, name, cost):
        color = TEXT_COLOR
        # title surf
        title_surf = self.font.render(name, False, color)
        title_rect = title_surf.get_rect(midtop=self.rect.midtop + pygame.math.Vector2(0, 20))

        # cost
        cost_surf = self.font.render(cost, False, color)
        cost_rect = cost_surf.get_rect(midtop=self.rect.midtop + pygame.math.Vector2(0, 40))

        # display
        surface.blit(title_surf, title_rect)
        surface.blit(cost_surf, cost_rect)

    def draw(self, surface):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                self.clicked = False

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button on screen
        surface.blit(self.button_image, (self.button_rect.x, self.button_rect.y))

        return action

    def display(self, surface, selection_num, name, cost):
        if self.index == selection_num:
            pygame.draw.rect(surface, UI_BG_COLOR, self.rect)
            pygame.draw.rect(surface, UI_BORDER_COLOR, self.rect, 4)
        self.display_names(surface, name, cost)
        self.action = self.draw(surface)
        if self.action:
            pygame.display.quit()



            # sys.exit()


