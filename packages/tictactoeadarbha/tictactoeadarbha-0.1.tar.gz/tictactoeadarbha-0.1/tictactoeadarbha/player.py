class Player:
    '''Template of a player class for creating a new player'''

    def __init__(self, name, marker):
        '''name - Unique name of the player
        marker - Unique marker for this player. Select from X/-'''
        self.name = name
        self.marker = marker

    def __repr__(self):
        return "Player name: {} \nMarker: {}".format(self.name, self.marker)


    