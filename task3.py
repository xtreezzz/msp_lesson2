

# Импортируем библиотеку для создания случайных чисел
import random

# Вводим глобальные переменные для подсчета суммы баллов всей школы и количества учеников
school_pupil_count = 0
school_scores_sum = 0


# Генерим случайную оценку в диапазоне от 1 до 5
def create_random_score():
    return random.randint(1, 5)


def create_scores_for_class(current_class):
    # Генерим количество учеников в классе в диапозоне от 10 до 35
    number_of_pupil = random.randint(10, 35)

    # Наполняем класс оценками
    for i in range(number_of_pupil):
        # Вызываем функцию генерации случайной оценки
        current_class['scores'].append(create_random_score())


def generate_school_dict(school_scores):
    # Наполняем лист scores данными
    for current_class in school_scores:
        create_scores_for_class(current_class)


# Создаем лист классов, даем название
school_scores = [
    {'school_class': '1a', 'scores': []},
    {'school_class': '1b', 'scores': []},
    {'school_class': '2a', 'scores': []},
    {'school_class': '2b', 'scores': []},
    {'school_class': '3a', 'scores': []},
    {'school_class': '3b', 'scores': []},
    {'school_class': '4a', 'scores': []},
    {'school_class': '4b', 'scores': []},
    {'school_class': '5a', 'scores': []},
    {'school_class': '5b', 'scores': []},
    {'school_class': '6a', 'scores': []},
    {'school_class': '6b', 'scores': []},
    {'school_class': '7a', 'scores': []},
    {'school_class': '7b', 'scores': []},
    {'school_class': '8a', 'scores': []},
    {'school_class': '8b', 'scores': []},
    {'school_class': '9a', 'scores': []},
    {'school_class': '9b', 'scores': []},
    {'school_class': '10a', 'scores': []},
    {'school_class': '10b', 'scores': []},
    {'school_class': '11a', 'scores': []},
    {'school_class': '11b', 'scores': []}
]

generate_school_dict(school_scores)
for current_class in school_scores:
    # Считаем среднюю оценку класса
    class_average_score = sum(current_class['scores']) / len(current_class['scores'])

    # Добавляем сумму оценок класса и количество учеников в данные по школе
    school_scores_sum = school_scores_sum + sum(current_class['scores'])
    school_pupil_count = school_pupil_count + len(current_class['scores'])

    print('Средний балл класса {} (всего учеников: {}) : {:.2f} '.format(current_class['school_class'],
                                                                         len(current_class['scores']),
                                                                         class_average_score))

# После всех подсчетов вычисляем средний балл школы
school_average_score = school_scores_sum / school_pupil_count

print('Средний балл школы: {:.2f} (всего учеников: {}) '.format(school_average_score, school_pupil_count))


my_score_dic = school_scores