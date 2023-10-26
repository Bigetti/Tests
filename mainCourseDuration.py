# Условие задачи
# Напишите код, который создаст список курсов courses_list, где каждый курс — словарь с названием курса, длительностью и преподавателями. После этого выведите названия самого короткого и самого длинного курсов.

# Обратите внимание на то, что могут встретиться курсы одинаковой длительности. Корректно обработайте эти случаи.


courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля",
           "Frontend-разработчик с нуля"]
mentors = [
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
     "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
     "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
     "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
     "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков",
     "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
     "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков",
     "Роман Гордиенко"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
     "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]
durations = [14, 20, 12, 20]


# Допишите код, который генерирует словарь-курс с тремя ключами: "title", "mentors", "duration"




#____________________________________

def create_courses_dict(courses, mentors, durations):

    # В этот список будут добавляться словари-курсы
    courses_list = []

    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {'title': course, 'mentor': mentor, 'duration': duration}
        courses_list.append(course_dict)
    # print(courses_list)
    # print()
    return  courses_list

# Найдите самое маленькое и самое большое значение длительности курса
# Подсказка: используйте функции min и max для списка durations
def min_max_courses_duration(durations):
    min_d = min(durations)
    max_d = max(durations)
    print(min_d,max_d)
    # print()
    return min_d, max_d

# Как видите, в duration встречаются одинаковые длительности курса. Допишите код, который это учитывает
# Подсказка 1: найдите индексы, по которым в списке durations встречается самое маленькое и самое большое значение
# Подсказка 2: не забудьте, что индекс можно удобно получить функцией enumerate
def min_max_duration_courses_index(durations, min_d, max_d):

    minis = []
    maxes = []

    for i, duration in enumerate(durations):
        if duration == max_d:
            maxes.append(i)
        elif duration == min_d:
            minis.append(i)
    print(minis)
    print(maxes)
    return minis, maxes

# Соберите все названия самых коротких и самых длинных курсов
# Так как курсов с одной длительностью может быть больше одного,
# создайте список названий самых коротких (courses_min) и самых длинных (courses_max) курсов


def min_max_duration_courses_list(minis, maxes, courses_list, min_d, max_d):
    courses_min = []
    for i in minis:
        if 0 <= i < len(courses_list):

            course = courses_list[i]
            title = course['title']
            courses_min.append(title)

    courses_max = []
    for i in maxes:
        if 0 <= i < len(courses_list):

            course = courses_list[i]
            title = course['title']
            courses_max.append(title)

      # Получить названия самых коротких курсов
    shortest_courses = [courses[i] for i in minis]

    # Получить названия самых длинных курсов
    longest_courses = [courses[i] for i in maxes]

    # Вывести названия на печать
    print(f'Самый короткий курс(ы): {", ".join(shortest_courses)} - {min_d} месяца(ев)')
    print(f'Самый длинный курс(ы): {", ".join(longest_courses)} - {max_d} месяца(ев)')

    return courses_min, courses_max  # Возвращаем кортеж из двух списков
    # print("Shortest courses", courses_min)
    # print("Longest coursese", courses_max)
    # print()


    # for id in minis:
    # 	courses_min.append(courses_list[...][...]) # Допишите код, который берёт по id нужный курс из courses_list и получает название курса из ключа "title"
    # for id in maxes:
    # 	courses_max.append(...) # По аналогии допишите такой же код для курсов максимальной длительности

    # Допишите конструкцию вывода результата. Можете использовать string.join()


if __name__ == "__main__":
    courses_list = create_courses_dict(courses, mentors, durations)
    min_d, max_d = min_max_courses_duration(durations)
    minis, maxes = min_max_duration_courses_index(durations, min_d, max_d)
    min_max_duration_courses_list(minis, maxes, courses_list, min_d, max_d)


