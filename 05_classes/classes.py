


class Player:
    def __init__(self, name):
        self.name = name
        self.roll = None
        self.wins = 0


class Roll:
    def __init__(self, name, cn_defeat, defeated_by):
        self.name = name
        self.cn_defeat = cn_defeat
        self.defeated_by = defeated_by

    def can_defeat(self, roll):
        if roll.name == self.cn_defeat:
            return 'Win'
        elif roll.name == self.defeated_by:
            return 'Lose'
        else:
            return 'Tie'