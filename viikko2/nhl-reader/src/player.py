import requests


class Player:
    def __init__(self, dict):
        self.name = dict["name"]
        self.nationality = dict["nationality"]
        self.assists = dict["assists"]
        self.goals = dict["goals"]
        self.team = dict["team"]
        self.games = dict["games"]
        self.id = dict["id"]

    def __str__(self):
        return f"{self.name:20} {self.team}  {self.goals:2} + {self.assists:2} = {self.goals + self.assists}"


class PlayerReader:
    def __init__(self, url):
        self.response = requests.get(url).json()
        # self.players = self.get_players(url)

    def get_players(self):
        players = []
        for player_dict in self.response:
            player = Player(player_dict)
            players.append(player)
        return players


class PlayerStats:
    def __init__(self, players):
        self.players = players.get_players()

    def top_scorers_by_nationality(self, nationality):
        nationals = []
        for player in self.players:
            if player.nationality == nationality:
                nationals.append(player)

        return sorted(
            nationals, key=lambda points: points.goals + points.assists, reverse=True
        )
