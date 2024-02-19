# classes/many_to_many.py

class Game:
    def __init__(self, title):
        self._title = title
        self._results = []

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if not isinstance(new_title, str) or len(new_title) == 0:
            raise ValueError("Title must be a non-empty string")
        self._title = new_title

    def results(self):
        return self._results

    def players(self):
        return list(set([result.player for result in self._results]))

    def average_score(self, player):
        scores = [result.score for result in self._results if result.player == player]
        return sum(scores) / len(scores) if scores else 0


class Player:
    all_players = []

    def __init__(self, username):
        if not isinstance(username, str) or not 2 <= len(username) <= 16:
            raise ValueError("Username must be a string of 2 to 16 characters")
        self._username = username
        self._results = []
        Player.all_players.append(self)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, new_username):
        if isinstance(new_username, str) and 2 <= len(new_username) <= 16:
            self._username = new_username

    def results(self):
        return self._results

    def games_played(self):
        return list(set([result.game for result in self._results]))

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        return len([result for result in self._results if result.game == game])

    @classmethod
    def highest_scored(cls, game):
        best_player = None
        highest_avg_score = 0
        for player in cls.all_players:
            avg_score = game.average_score(player)
            if avg_score > highest_avg_score:
                best_player = player
                highest_avg_score = avg_score
        return best_player


class Result:
    all = []

    def __init__(self, player, game, score):
        if not isinstance(score, int) or not 1 <= score <= 5000:
            raise ValueError("Score must be an integer between 1 and 5000")
        self._score = score
        self._player = player
        self._game = game
        player._results.append(self)
        game._results.append(self)
        Result.all.append(self)

    @property
    def score(self):
        return self._score

    @property
    def player(self):
        return self._player

    @property
    def game(self):
        return self._game