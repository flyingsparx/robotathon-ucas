from rgkit import rg

move = 0

class Robot:
    def act(self, game):
        move += 1
        if move %2 == 0:
            return ['move', (self.location[0]-1, self.location[1])]
        if move %3 == 0:
            return ['attack', (self.location[0]-1, self.location[1])]
        else:
            return ['guard']