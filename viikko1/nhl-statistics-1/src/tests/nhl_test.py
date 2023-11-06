import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search(self):
        player = self.stats.search("Kurri")
        self.assertEqual(player.name, "Kurri")

    def test_search_not_in_players(self):
        player = self.stats.search("Hurri")
        self.assertEqual(player, None)

    def test_team(self):
        team = self.stats.team("PIT")
        self.assertEqual(1, len(team))

    def test_top_points_length(self):
        players = self.stats.top(2, SortBy.POINTS)
        self.assertEqual(2, len(players))

    def test_top_goals_length(self):
        players = self.stats.top(3, SortBy.GOALS)
        self.assertEqual(3, len(players))

    def test_top_assists_length(self):
        players = self.stats.top(3, SortBy.ASSISTS)
        self.assertEqual(3, len(players))

    def test_top_points(self):
        players = self.stats.top(3, SortBy.POINTS)
        best_points = players[0]
        self.assertEqual(best_points.name, "Gretzky")

    def test_top_goals(self):
        players = self.stats.top(3, SortBy.GOALS)
        second_best_goals = players[1]
        self.assertEqual(second_best_goals.name, "Yzerman")

    def test_top_assists(self):
        players = self.stats.top(3, SortBy.ASSISTS)
        third_best_assists = players[2]
        self.assertEqual(third_best_assists.name, "Lemieux")
