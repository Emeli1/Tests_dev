from unittest import TestCase

from votes import vote
from quadratic_equation import solution
from secretary import get_name, get_directory, add_data

class TestVotes(TestCase):
    def test_votes(self):
        for i, (votes, expected) in enumerate((
                ([1, 1, 1, 2, 3], 1),
                ([1, 2, 3, 2, 2], 2),
        )):
            with self.subTest(i):
                result = vote(votes)
                self.assertEqual(expected, result)

class TestQuadratic(TestCase):
    def test_quadratic(self):
        for i, (a, b, c, expected) in enumerate((
                (1, 8, 15, (-3.0, -5.0)),
                (1, -13, 12, (12.0, 1.0)),
                (-4, 28, -49, 3.5),
                (1, 1, 1, 'корней нет'),
        )):
            with self.subTest(i):
                result = solution(a, b, c)
                self.assertEqual(expected, result)

class TestSecretary(TestCase):
    def test_get_name(self):
        for i, (number, expected) in enumerate((
                ('10006', 'Аристарх Павлов'),
                ('101', 'Документ не найден'),
                ('311 020203', 'Документ не найден'),
        )):
            with self.subTest(i):
                result = get_name(number)
                self.assertEqual(expected, result)

    def test_get_directory(self):
        for i, (doc_number, expected) in enumerate((
                ('11-2', '1'),
                ('311 020203', 'Полки с таким документом не найдено'),
                ('311 020204', 'Полки с таким документом не найдено')
        )):
            with self.subTest(i):
                result = get_directory(doc_number)
                self.assertEqual(expected, result)

    def test_add_data(self):
        for i, (a, b, c, d, expected) in enumerate((
                ('international passport', '311 020205', 'Александр Пушкин', 3, 'Данные добавлены на имя Александр Пушкин'),
                ('invoice', '322 020203', 'Сергей Есенин', 5, 'Данные добавлены на имя Сергей Есенин')
        )):
            with self.subTest(i):
                result = add_data(a, b, c, d)
                self.assertEqual(expected, result)


