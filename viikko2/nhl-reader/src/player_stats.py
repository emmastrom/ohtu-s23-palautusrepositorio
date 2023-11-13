class PlayerStats:
    def __init__(self, reader):
        self._players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        new_players = []
        for player in self._players:
            if player.nationality == nationality:
                new_players.append(player)
        new_players.sort(key=lambda x: x.points, reverse=True)

        return new_players
