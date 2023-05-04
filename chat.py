from src import function


class questions:

    def __init__(self):
        self.questions = {}

    def add_question(self, questions):
        self.questions = function.add_question()
        return self.questions

class Game(questions):
    c = {}
    quest = {}
    def __init__(self, bals = 0, corr = 0, incorr = 0):
        super().__init__()
        self.quest = questions()
        self.c = self.quest.add_question(self.quest )
        self.bals, self.corr, self.incorr = function.quest_random(self.c)



bals = Game()
print(f'Конец игры вы заработали\n{bals.bals} баллов\n{bals.corr} правильных ответов\n{bals.incorr} неправильных ответов')