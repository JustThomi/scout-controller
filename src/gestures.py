import pygame

# 4, 8, 12, 16, 20

class Gestures:
    def __init__(self, nodes):
        self.nodes = nodes
        
        self.finger_tips = {
            "thumb" = self.nodes[4],
            "index" = self.nodes[8],
            "middle" = self.nodes[12],
            "ring" = self.nodes[16],
            "pinky" = self.nodes[20],
        }
    
    def monitor_gestures(self, rects):
        if finger_tips["thumb"].colliderect(finger_tips["index"]):
            thumb_action()
        if finger_tips["thumb"].colliderect(finger_tips["middle"]):
            middle_action()
        if finger_tips["thumb"].colliderect(finger_tips["ring"]):
            ring_action()
        if finger_tips["thumb"].colliderect(finger_tips["pinky"]):
            pinky_action()    

    def thumb_action(self):
        print("Index collision")
    
    def middle_action(self):
        print("Middle collision")
    
    def ring_action(self):
        print("Ring collision")
    
    def pinky_action(self):
        print("Pinky collision")
    
