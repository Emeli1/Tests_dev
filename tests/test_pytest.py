import pytest

from votes import vote
from quadratic_equation import solution
from secretary import get_name, get_directory, add_data

@pytest.mark.parametrize(
    'votes, expected',
    (
            ([1, 1, 1, 2, 3], 1),
            ([1, 2, 3, 2, 2], 2),
     )
)
def test_votes(votes, expected):
    assert vote(votes) == expected


def generate_data_quadratic():
    yield 1, 8, 15, (-3.0, -5.0)
    yield 1, -13, 12, (12.0, 1.0)
    yield -4, 28, -49, 3.5
    yield 1, 1, 1, 'корней нет'

@pytest.mark.parametrize('a, b, c, expected', generate_data_quadratic())
def test_quadratic_equation(a, b, c, expected):
    assert solution(a, b, c) == expected


def generate_get_name():
    yield '10006', 'Аристарх Павлов'
    yield '101', 'Документ не найден'
    yield '311 020203', 'Документ не найден'

@pytest.mark.parametrize('number, expected', generate_get_name())
def test_get_name(number, expected):
    assert get_name(number) == expected


def generate_get_directory():
    yield '11-2', '1'
    yield '311 020203', 'Полки с таким документом не найдено'
    yield '311 020204', 'Полки с таким документом не найдено'

@pytest.mark.parametrize('doc_number, expected', generate_get_directory())
def test_get_directory(doc_number, expected):
    assert get_directory(doc_number) == expected


def generate_add_data():
    yield 'international passport', '311 020205', 'Александр Пушкин', 3, 'Данные добавлены на имя Александр Пушкин'
    yield 'invoice', '322 020203', 'Сергей Есенин', 5, 'Данные добавлены на имя Сергей Есенин'

@pytest.mark.parametrize('a, b, c, d, expected', generate_add_data())
def test_add_data(a, b, c, d, expected):
    assert add_data(a, b, c, d) == expected



