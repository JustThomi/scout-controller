import pygame

# 4, 8, 12, 16, 20


class Gestures:
    def __init__(self, nodes):
        self.nodes = nodes

        self.finger_tips = {
            "thumb": self.nodes[4],
            "index": self.nodes[8],
            "middle": self.nodes[12],
            "ring": self.nodes[16],
            "pinky": self.nodes[20],
        }

    def monitor_gestures(self):
        if self.finger_tips["thumb"].colliderect(self.finger_tips["index"]):
            self.thumb_action()
        elif self.finger_tips["thumb"].colliderect(self.finger_tips["middle"]):
            self.middle_action()
        elif self.finger_tips["thumb"].colliderect(self.finger_tips["ring"]):
            self.ring_action()
        elif self.finger_tips["thumb"].colliderect(self.finger_tips["pinky"]):
            self.pinky_action()

    def thumb_action(self):
        print("Index collision")

    def middle_action(self):
        print("Middle collision")

    def ring_action(self):
        print("Ring collision")

    def pinky_action(self):
        print("Pinky collision")
