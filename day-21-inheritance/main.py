class Animal:
    #
    # def __init__(self):
    #     "Creating an animal..."

    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):

    # def __init__(self):
    #     super()

    def breathe(self):
        super()
        super().breathe()
        print("Cause I'm a fish")


a = Animal()
# a.breathe()

f = Fish()

f.breathe()