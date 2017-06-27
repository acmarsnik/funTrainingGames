from datetime import datetime
from pony.orm import *


db = Database()


class User(db.Entity):
    _table_ = 'Table_User'
    id = PrimaryKey(int, auto=True)
    username = Required(str, unique=True)
    user_ID = Set('User_Match')


class Match(db.Entity):
    _table_ = 'Table_Match'
    id = PrimaryKey(int, auto=True)
    date = Required(datetime)
    season_ID = Required('Season')
    match_ID = Set('User_Match')


class GameType(db.Entity):
    _table_ = 'Game'
    id = PrimaryKey(int, auto=True)
    description = Optional(LongStr)
    gameType_Id = Set('GameType_GameLevel')


class GameLevel(db.Entity):
    _table_ = 'Table_GameLevel'
    id = PrimaryKey(int, auto=True)
    description = Required(LongStr)
    gameLevel_ID = Set('GameType_GameLevel', cascade_delete=True)


class GameType_GameLevel(db.Entity):
    _table_ = 'Table_GameType_GameLevel'
    id = PrimaryKey(int, auto=True)
    gameLevel_ID = Required(GameLevel)
    gameType_ID = Required(GameType)
    gameType_GameLevel_ID = Set('Season')


class Season(db.Entity):
    _table_ = 'Table_Season'
    id = Required(unicode)
    gameType_GameLevel_ID = Required(GameType_GameLevel)
    season_ID = Set(Match)


class User_Match(db.Entity):
    _table_ = 'Table_UserMatch'
    id = PrimaryKey(int, auto=True)
    user_ID = Required(User)
    match_ID = Required(Match)
    homeTeam = Required(bool)
    score = Required(int)


db.bind("sqlite", "database.sqlite", create_db=True)
db.generate_mapping(create_tables=True)