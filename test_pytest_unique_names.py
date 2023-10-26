import pytest
import mainUniqName

def test_add_all_teachers_all_courses():

    actual_result = mainUniqName.sorted_unique_names_list(mainUniqName.unique_names_set_make(mainUniqName.just_all_names(mainUniqName.add_all_teachers_all_courses(mainUniqName.mentors))))

    expected = "Адилет, Азамат, Александр, Алексей, Алена, Анатолий, Анна, Антон, Вадим, Валерий, Владимир, Денис, Дмитрий, Евгений, Елена, Иван, Илья, Кирилл, Константин, Максим, Михаил, Никита, Николай, Олег, Павел, Ринат, Роман, Сергей, Татьяна, Тимур, Филипп, Эдгар, Юрий"

    assert actual_result == expected