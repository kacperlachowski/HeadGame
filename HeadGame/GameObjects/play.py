from time import time


class Play:
    level = 1
    time_on_level = 5
    time_level = None
    time_game = None
    times_level_up = [2.2, 2, 1.8, 1.6, 1.4, 1.2, 1, .8, .6, .4]

    def __init__(self):
        self.time_game = time()
        self.time_level = time()

    def increment_level(self):
        if self.level < 10:
            self.level += 1

    def get_time_on_create_rival(self):
        return self.times_level_up[self.level - 1]

    def get_text_level(self):
        return "Poziom: {}".format(self.level)

    def get_time_game_in_last_around(self):
        return str(time() - self.time_game)[:5]

    def clear_game(self):
        self.level = 1
        self.time_game = time()
        self.time_level = time()
