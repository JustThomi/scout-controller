import pygame
import cv2
from hand_detector import HandDetector

# Fingertip node ids
# 4, 8, 12, 16, 20


class App:
    def __init__(self):
        self.width = 600
        self.height = 600

        self.run = True
        self.fps = 60
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((self.width, self.height))
        self.font = pygame.font.SysFont('Monocraft', 12)

        self.detector = HandDetector()
        self.cap = cv2.VideoCapture(0)

        self.nodes = []
        self.init_nodes()

    def init_nodes(self):
        for i in range(21):
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
            except:
                print("Capture failed")

            self.render()
        pygame.quit()

    def render(self):
        self.window.fill("black")
        for index, n in enumerate(self.nodes):
            pygame.draw.rect(self.window, (255, 255, 255), n)

            self.window.blit(self.font.render(
                str(index), True, (20, 0, 20)), n)

        pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption('Hand Tracker Visualizer')

    app = App()
    app.update()
