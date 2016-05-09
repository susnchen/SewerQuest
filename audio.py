import pygame

class Audio:
    def __init__(self,sound):
        self.length = sound.get_length()
        self.replayCounter = self.length
        self.sound = sound
        self.muteState = 0

    def update(self,fps):
        self.replayCounter += 1/fps

        if self.replayCounter >= self.length:
            self.sound.stop()
            self.sound.play()
            self.replayCounter = 0
            print("audio played")

    def mute(self):
        if self.muteState == 1:
            self.sound.play()
            self.muteState = 0

        elif self.muteState == 0:
            self.sound.stop()
            self.muteState = 1

        self.replayCounter = 0