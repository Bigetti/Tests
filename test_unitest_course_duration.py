import unittest
from mainCourseDuration import create_courses_dict, min_max_courses_duration, min_max_duration_courses_index, min_max_duration_courses_list


class test_unitest_course_duration(unittest.TestCase):


    def setUp(self):
        self.courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля",
                        "Frontend-разработчик с нуля"]
        self.mentors = [
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
        self.durations = [14, 20, 12, 20]


    def test_create_courses_dict(self):

        expected = [
            {'title': 'Java-разработчик с нуля',
             'mentor': ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков",
                        "Илья Сухачев",
                        "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев",
                        "Никита Шумский",
                        "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов",
                        "Евгений Грязнов",
                        "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"], 'duration': 14},
            {'title': 'Fullstack-разработчик на Python',
             'mentor': ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов",
                        "Кирилл Табельский",
                        "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко",
                        "Алена Батицкая", "Денис Ежков",
                        "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
             'duration': 20},
            {'title': 'Python-разработчик с нуля',
             'mentor': ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский",
                        "Александр Ульянцев",
                        "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина",
                        "Азамат Искаков",
                        "Роман Гордиенко"], 'duration': 12},
            {'title': 'Frontend-разработчик с нуля',
             'mentor': ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен",
                        "Александр Фитискин",
                        "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин",
                        "Михаил Ларченко"], 'duration': 20}
        ]


        result = create_courses_dict(self.courses, self.mentors, self.durations)
        self.assertEqual(result, expected)


    def test_min_max_courses_duration(self):
        min_d, max_d = min_max_courses_duration(self.durations)
        self.assertEqual(min_d, 12)
        self.assertEqual(max_d, 20)

    def test_min_max_duration_courses_index(self):
        minis, maxes = min_max_duration_courses_index(self.durations, 12, 20)
        self.assertEqual(minis, [2])
        self.assertEqual(maxes, [1, 3])

    def test_min_max_duration_courses_list(self):
        courses_list = create_courses_dict(self.courses, self.mentors, self.durations)
        min_d, max_d = min_max_courses_duration(self.durations)  # Получаем min_d и max_d
        minis, maxes = min_max_duration_courses_index(self.durations, min_d, max_d)
        min_courses, max_courses = min_max_duration_courses_list(minis, maxes, courses_list, min_d, max_d)  # Передаем min_d и max_d
        self.assertEqual(min_courses, ['Python-разработчик с нуля'])

if __name__ == '__main__':
    unittest.main()