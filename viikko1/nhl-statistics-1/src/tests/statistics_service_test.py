import unittest
from statistics_service import StatisticsService, SortBy
from player import Player


class PlayerReaderStub:
    def get_players(self):
        players = [
            Player("Niko Nopea", "LOL", 2, 7),
            Player("Hemuli Huono", "PHI", 0, 0),
            Player("Pirjo Paras", "KOK", 12, 21),
            Player("Maukka Mainio", "PHI", 4, 4),
            Player("Sale syöttäjä", "COL", 0, 5),
        ]
        return players


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        reader = PlayerReaderStub()
        self.service = StatisticsService(reader)
        # self.sort_by = SortBy()

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

    def test_top_points(self):
        find_top = self.service.top(2, SortBy.POINTS)
        correct_top = [
            Player("Pirjo Paras", "KOK", 12, 21),
            Player("Niko Nopea", "LOL", 2, 7),
            Player("Maukka Mainio", "PHI", 4, 4),
        ]

        print("Löydettyjen pisteet")
        [print(player.points) for player in find_top]
        print("Oikeat pisteet")
        [print(player.points) for player in correct_top]

        find_top = [str(player) for player in find_top]
        correct_top = [str(player) for player in correct_top]
        self.assertEqual(find_top, correct_top)

    def test_top_default(self):
        find_top = self.service.top(2)
        correct_top = [
            Player("Pirjo Paras", "KOK", 12, 21),
            Player("Niko Nopea", "LOL", 2, 7),
            Player("Maukka Mainio", "PHI", 4, 4),
        ]

        print("Löydettyjen pisteet")
        [print(player.points) for player in find_top]
        print("Oikeat pisteet")
        [print(player.points) for player in correct_top]

        find_top = [str(player) for player in find_top]
        correct_top = [str(player) for player in correct_top]

        self.assertEqual(find_top, correct_top)

    def test_top_goals(self):
        find_top = self.service.top(2, SortBy.GOALS)
        correct_top = [
            self.service._players[2],
            self.service._players[3],
            self.service._players[0],
        ]
        self.assertEqual(find_top, correct_top)

    def test_top_assists(self):
        find_top = self.service.top(2, SortBy.ASSISTS)
        correct_top = [
            self.service._players[2],
            self.service._players[0],
            self.service._players[4],
        ]
        self.assertEqual(find_top, correct_top)
