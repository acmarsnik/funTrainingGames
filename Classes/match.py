try:
    from Classes.gameLevel import GameLevel
    from Classes.gameType import GameType

    class Match:
        def __init__(self):
            self.id = None
            self.date = None
            self.season_ID = None
            self.gameType = GameType()
            self.gameLevel = GameLevel()

except Exception as e:
    print(e)