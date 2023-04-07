from typing import List

from utils import singleton
from idao import PlayerIDAO
from entities import Player
from .with_connection_meta import WithConnectionMeta


@singleton
class PlayerDAO(PlayerIDAO, metaclass=WithConnectionMeta):
    def select_all(self, cursor) -> List[Player]:
        stmt = 'SELECT * FROM player'
        cursor.execute(stmt)
        players = [Player(*row) for row in cursor.fetchall()]
        return players

    def find_by_id(self, cursor, player_id: int) -> Player:
        stmt = f'SELECT * FROM player WHERE id = %s'
        cursor.execute(stmt, (player_id,))
        result = cursor.fetchall()
        if result:
            return Player(*result[0])

    def insert(self, cursor, players: List[Player]):
        for player in players:
            stmt = f'INSERT INTO player VALUES {player.attributes}'
            cursor.execute(stmt)

    def update(self, cursor, players: List[Player]):
        stmt = 'UPDATE player SET user_id = %s, ' + \
                                  'balance_id = %s, ' + \
                             'WHERE id = %s'
        for player in players:
            cursor.execute(stmt, (*player.attributes[1:], player.id))

    def delete(self, cursor, players: List[Player]):
        for player in players:
            stmt = f'DELETE FROM player WHERE id = {player.id}'
            cursor.execute(stmt)