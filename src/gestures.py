import pygame
from signals.client import Client
import ui.settings as settings


class Gestures:
    def __init__(self, nodes):
        self.nodes = nodes
        self.client = Client()

        self.finger_tips_hand_one = {
            "thumb": self.nodes[4],
            "index": self.nodes[8],
            "middle": self.nodes[12],
            "ring": self.nodes[16],
            "pinky": self.nodes[20],
        }

        self.finger_tips_hand_two = {
            "thumb": self.nodes[25],
            "index": self.nodes[29],
            "middle": self.nodes[33],
            "ring": self.nodes[37],
            "pinky": self.nodes[41],
        }

    def monitor_gestures(self):
        if self.finger_tips_hand_one["thumb"].colliderect(self.finger_tips_hand_one["index"]):
            self.index_action()
        elif self.finger_tips_hand_one["thumb"].colliderect(self.finger_tips_hand_one["middle"]):
            self.middle_action()
        elif self.finger_tips_hand_one["thumb"].colliderect(self.finger_tips_hand_one["ring"]):
            self.ring_action()
        elif self.finger_tips_hand_one["thumb"].colliderect(self.finger_tips_hand_one["pinky"]):
            self.pinky_action()

        # FOR second hand, not implemented yet (no need for this...for now)
        if settings.two_hands:
            if self.finger_tips_hand_two["thumb"].colliderect(self.finger_tips_hand_two["index"]):
                pass
            elif self.finger_tips_hand_two["thumb"].colliderect(self.finger_tips_hand_two["middle"]):
                pass
            elif self.finger_tips_hand_two["thumb"].colliderect(self.finger_tips_hand_two["ring"]):
                pass
            elif self.finger_tips_hand_two["thumb"].colliderect(self.finger_tips_hand_two["pinky"]):
                pass

    def index_action(self):
        self.client.send_signal("up")
        print("Index collision")

    def middle_action(self):
        self.client.send_signal("down")
        print("Middle collision")

    def ring_action(self):
        self.client.send_signal("left")
        print("Ring collision")

    def pinky_action(self):
        self.client.send_signal("right")
        print("Pinky collision")
