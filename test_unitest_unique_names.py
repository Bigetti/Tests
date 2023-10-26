import unittest
import mainUniqName

class TestUnitestUniqueName(unittest.TestCase):

    def setUp(self):
        print("method setUp")


    def testResult(self):

        actual_result = mainUniqName.sorted_unique_names_list(mainUniqName.unique_names_set_make(mainUniqName.just_all_names(mainUniqName.add_all_teachers_all_courses(mainUniqName.mentors))))

        expected = "Адилет, Азамат, Александр, Алексей, Алена, Анатолий, Анна, Антон, Вадим, Валерий, Владимир, Денис, Дмитрий, Евгений, Елена, Иван, Илья, Кирилл, Константин, Максим, Михаил, Никита, Николай, Олег, Павел, Ринат, Роман, Сергей, Татьяна, Тимур, Филипп, Эдгар, Юрий"

        self.assertEqual(expected,  actual_result)


if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestUnitestUniqueName)
    runner = unittest.TextTestRunner()
    result = runner.run(suite)