class Bird:
    def sound(self):
        print("Bird Sound")

class Sparrow(Bird):

    def sound(self):
        print("Chirp Chirp")


sparrow = Sparrow()
sparrow.sound()
