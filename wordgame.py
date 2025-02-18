class Wordgame:

    def __init__(self, word: str, answers: set) -> None:
        self.word = word
        self.answers = answers
        self.players = []
        self.scores = {}

    def player_joins(self, player):
        print(f'game: {player} joins')
        self.players.append(player)
        self.scores[player] = set()

    def player_guess(self, player, guess):
        if guess in self.answers:
            self.answers.remove(guess)
            self.scores[player].add(guess)
            return f'{guess} OK! current score is {len(self.scores[player])}'
        return 'bad guess'




