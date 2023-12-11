class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def is_tie(self, p1_score, p2_score):
        match (p1_score):
            case 0:
                return "Love-All"
            case 1:
                return "Fifteen-All"
            case 2:
                return "Thirty-All"
            case _:
                return "Deuce"

    def is_win_or_advantage(self, minus_result):
         #minus_result = self.m_score1 - self.m_score2
         if minus_result == 1:
             return "Advantage player1"
         if minus_result == -1:
             return "Advantage player2"
         if minus_result >=2:
             return "Win for player1"
         else:
             return "Win for player2"

    def score_into_string(self, p1_score, p2_score):
        match (p1_score):
            case 0:
                score = "Love"
            case 1:
                score = "Fifteen"
            case 2:
                score = "Thirty"
            case 3:
                score = "Forty"

        score = score + "-"

        match (p2_score):
            case 0:
                return score + "Love"
            case 1:
                return score + "Fifteen"
            case 2:
                return score + "Thirty"
            case 3:
                return score + "Forty"


    def get_score(self):
        score = ""
        #0=Love, 1=FIFTEEN, 2=THIRTY, 3=FORTY, 4=WIN, 4,4=DEUCE

        if self.m_score1 == self.m_score2:
            return self.is_tie(self.m_score1, self.m_score2) #tie

        elif self.m_score1 >= 4 or self.m_score2 >= 4: #win or advantage
            return self.is_win_or_advantage(self.m_score1-self.m_score2)

        else: #if not tie and no advantage/win, what is the score
            return self.score_into_string(self.m_score1, self.m_score2)
