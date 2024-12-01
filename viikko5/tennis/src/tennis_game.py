class TennisGame:
    LOVE = 0
    FIFTEEN = 1
    THIRTY = 2
    FORTY = 3

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):

        if self.player1_score == self.player2_score:
            score = self.draw()

        elif self.player1_score >= 4 or self.player2_score >= 4:
            score = self.more_than_three_points()

        else:
            score = ""
            score += self.less_than_four_points(self.player1_score)
            score += "-"
            score += self.less_than_four_points(self.player2_score)

        return score

    def draw(self):
        if self.player1_score == self.LOVE:
            score = "Love-All"
        elif self.player1_score == self.FIFTEEN:
            score = "Fifteen-All"
        elif self.player1_score == self.THIRTY:
            score = "Thirty-All"
        else:
            score = "Deuce"

        return score

    def more_than_three_points(self):
        minus_result = self.player1_score - self. player2_score

        if minus_result == 1:
            score = "Advantage player1"
        elif minus_result == -1:
            score = "Advantage player2"
        elif minus_result >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"

        return score

    def less_than_four_points(self, player_score):
        if player_score == self.LOVE:
            score = "Love"
        elif player_score == self.FIFTEEN:
            score = "Fifteen"
        elif player_score == self.THIRTY:
            score = "Thirty"
        else:
            score = "Forty"

        return score
