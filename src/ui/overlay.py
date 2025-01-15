import pygame
import ui.settings as settings

# WORSE UI solution I ever made :)))
class Overlay:
    def __init__(self, window):
        self.window = window

        self.title_font = pygame.font.SysFont('Arial', 64)
        self.small_font = pygame.font.SysFont('Arial', 32)

        self.size = (400, 600)
        self.bg_color = (60, 60, 60)
        self.rect = pygame.Rect((0, 0), self.size)

        # Setup Buttons
        self.button_rect = pygame.Rect((50, 200), (30, 30))
        self.true_color = (20, 0, 200)
        self.false_color = (255, 255, 255)
    

    def handle_buttons(self):
        for event in pygame.event.get():
            # Should not be necessary but somethimes its not working right
            # Probably bc this is a mid solution
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.button_rect.collidepoint(event.pos):
                    settings.two_hands = not settings.two_hands
    
    def update(self):
        self.handle_buttons()

    def render(self):
        # background
        pygame.draw.rect(self.window, self.bg_color, self.rect)

        # text
        self.window.blit(self.title_font.render("Settings", True, (255, 255, 255)), (50, 50))
        self.window.blit(self.small_font.render("Two Hands", True, (255, 255, 255)), (100, 200))

        # buttons
        if settings.two_hands:
            pygame.draw.rect(self.window, self.true_color, self.button_rect)
        else:
            pygame.draw.rect(self.window, self.false_color, self.button_rect)