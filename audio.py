
# by Susan Chen and Samantha Lam
# May 20, 2016
# Submitted to ICS3U1, Mr. Cope

# audio.py
# contains the audio class will contain a sound file that will be able to loop itself and able to mute and unmute the sound

# input: pygame sound and fps as an int
# output: music

class Audio:
    def __init__(self,sound):
        #length of the sound in seconds
        self.sound = sound
        self.length = sound.get_length()

        #replayCounter will be used to count up by the seconds and is set to the length so it plays the first time the update function is called
        #muteState is 0, because it is not muted
        self.replayCounter = sound.get_length()
        self.muteState = 0

    #updates the progress of the sound given fps
    def update(self,fps):
        #since this function will be called every frame, the amount of time that passed since the last time it was called would be 1/fps
        self.replayCounter += 1/fps

        #if the counter surpasses the length of the sound, replay the sound
        if self.replayCounter >= self.length:
            self.sound.stop()
            self.sound.play()
            self.replayCounter = 0

    #function that will mute or unmute the sound 
    def mute(self):
        #if the sound is muted, play the sound
        if self.muteState == 1:
            self.sound.play()
            self.muteState = 0

        #if the sound is not muted, stop the sound
        elif self.muteState == 0:
            self.sound.stop()
            self.muteState = 1

        #restart the counter
        self.replayCounter = 0