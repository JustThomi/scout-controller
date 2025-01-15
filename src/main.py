import pygame
import cv2
import ui.settings as settings

from ui.overlay import Overlay
from hand_detector import HandDetector
from gestures import Gestures


class App:
    def __init__(self):
        self.width = 1000
        self.height = 600

        self.run = True
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((self.width, self.height))
        self.font = pygame.font.SysFont('Arial', 12)

        self.overlay = Overlay(self.window)

        self.detector = HandDetector()
        self.cap = cv2.VideoCapture(0)

        self.finger_tips_hand_one = [4, 8, 12, 16, 20]
        self.finger_tips_hand_two = [25, 29, 33, 37, 41]

        self.nodes = []
        self.init_nodes()

        self.gestures = Gestures(self.nodes)

    def init_nodes(self):
        # for i in range(21):
        for i in range(42):
            if i in self.finger_tips_hand_one or i in self.finger_tips_hand_two:
                node = pygame.Rect(self.width / 2, self.width / 2, 30, 30)
            else:
                node = pygame.Rect(self.width / 2, self.width / 2, 20, 20)
            self.nodes.append(node)

    def update(self):
        while self.run:
            self.clock.tick(self.fps)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            success, img = self.cap.read()

            try:
                coordonates = self.detector.get_landmarks(img)
                for index, coords in enumerate(coordonates):
                    self.nodes[index].x = abs(coords[0] - self.width)
                    self.nodes[index].y = coords[1]

                self.gestures.monitor_gestures()
            except:
                print("Hand Capture Failed")

            self.overlay.update()
            self.render()
        pygame.quit()

    def render(self):
        self.window.fill((24, 24, 24))

        for index, n in enumerate(self.nodes):
            if not settings.two_hands and index >= 21:
                break

            pygame.draw.rect(self.window, (255, 255, 255), n)

            self.window.blit(self.font.render(
                str(index), True, (20, 0, 20)), n)

        self.overlay.render()
        pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('Hand Tracker Visualizer')

    app = App()
    app.update()

# in case I forget to open py venv (linux)
# source .venv/bin/activate