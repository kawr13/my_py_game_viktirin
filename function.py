import json
import random

def add_question():
    with open('D:\my_learn\src\questions.json', 'r') as f:
        questions = json.load(f)
    return {i + 1: q for i, q in enumerate(questions)}


def quest_random(questions):
    keys = list(questions.keys())  # создаем список ключей словаря
    random.shuffle(keys)  # перемешиваем порядок ключей

    correct_answer = 0
    incorrect_answer = 0
    balls = 0
    for key in keys:
        value = questions[key]
        if "false" in value["f"]:
            print(f'{key}: {value["q"]}')
            us_answer = input('Для выхода введите exit\nВведите ответ: ')
            if us_answer == value["a"]:
                print('Верно')
                balls += int(value["d"])
                correct_answer += 1
                value["f"] = "true"
            elif us_answer == 'exit':
                break
            else:
                incorrect_answer += 1
                print(f'Неверно, правильный ответ: {value["a"]}')
        else:
            continue
    return balls, correct_answer, incorrect_answer

