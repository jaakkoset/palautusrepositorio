import unittest
from statistics_service import StatisticsService
from player import Player


class PlayerReaderStub:
    def get_players(self):
        players = [
            Player("Niko Nopea", "LOL", 2, 4),
            Player("Hemuli Huono", "PHI", 0, 0),
            Player("Pirjo Paras", "KOK", 12, 21),
            Player("Maukka Mainio", "PHI", 5, 9),
        ]
        return players


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        reader = PlayerReaderStub()
        self.service = StatisticsService(reader)

    def test_search_hit(self):
        result = self.service.search("Pirjo Paras")
        compare = Player("Pirjo Paras", "KOK", 12, 21)
        self.assertEqual(str(result), str(compare))

    def test_search_no_hit(self):
        result = self.service.search("Olio Olematon")
        self.assertEqual(result, None)

    def test_team(self):
        find_team = self.service.team("PHI")
        correct_team = [
            self.service._players[1],
            self.service._players[3],
        ]
        self.assertEqual(find_team, correct_team)

    def test_top(self):
        find_top = self.service.top(2)
        correct_top = [
            self.service._players[2],
            self.service._players[3],
            self.service._players[0],
        ]
        self.assertEqual(find_top, correct_top)
