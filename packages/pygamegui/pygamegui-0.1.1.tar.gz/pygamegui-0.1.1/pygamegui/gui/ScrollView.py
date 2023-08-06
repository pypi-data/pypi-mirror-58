# -*- codig: utf-8 -*-
# author: Ethosa

import pygame
from .LinearLayout import LinearLayout


class ScrollView(LinearLayout):
    def __init__(self, width=100, height=100,
                 background_color=(255, 255, 255, 255)):
        """View constructor

        Keyword Arguments:
            width {number} -- view width (default: {100})
            height {number} -- view height (default: {100})
            background_color {tuple} -- backgrond color (default: {(255, 255, 255, 255)})
        """
        LinearLayout.__init__(self, width, height, background_color)

    def handle_event(self):
        super().handle_event()
        if self.is_collide_rounded(pygame.mouse.get_pos()):
            for event in pygame.event.get():
                print(event)
                if event.type == 1027:
                    self.background.scroll(0, event.y)
