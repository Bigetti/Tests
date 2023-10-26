courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python",
           "Frontend-разработчик с нуля"]

mentors = [
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
     "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков",
     "Роман Гордиенко"],
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
     "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
     "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
     "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
     "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков",
     "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
     "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]

# Добавьте в список всех преподавателей со всех курсов
def add_all_teachers_all_courses (mentors):
    all_list = []
    for m in mentors:
        for teacher in m:
            if teacher not in all_list:
                all_list.append(teacher)
    return (all_list)
# print(all_list)

# Сделайте список all_names_list, состоящий только из имён, и заполните его
def just_all_names (all_list):

    all_names_list = []
    for mentor in all_list:
        name = mentor.split()[0]  # Получаем первый элемент (имя)
        all_names_list.append(name)
    return (all_names_list)
    # print(all_names_list)


# Сделайте так, чтобы остались только уникальные имена (без повторений) - допишите ниже ваш код
def unique_names_set_make (all_names_list):

    unique_names = set(all_names_list)
    return unique_names
    # print(unique_names)


# Теперь необходимо отсортировать имена в алфавитном порядке. Подсказка: используйте sorted() для списка
# Допишите код ниже
def sorted_unique_names_list(unique_names):
    all_names_sorted = sorted(list(unique_names))
    # print(all_names_sorted)
    # Допишите конструкцию вывода результата. Можете использовать string.join()
    # Результат будет в all_names_sorted
    result = (', ').join(all_names_sorted)
    # print()
    # print()
    #print(f'Уникальные имена преподавателей: {result}')
    return result



if __name__ == "__main__":
    all_list = add_all_teachers_all_courses(mentors)
    all_names_list = just_all_names(all_list)
    unique_names = unique_names_set_make(all_names_list)
    result = sorted_unique_names_list(unique_names)
    print (result)
