import random


class Generator:
    def __init__(self):
        pass
    def generateShortLink(self):
        shortLink = random.randint(1000,9999)
        return shortLink

    # def getMainLink(self,shortLink):
    #
    #     return mainLink
