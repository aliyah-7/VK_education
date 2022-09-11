import pytest


class TestList:
    # Позитивный тест - проверка длинны list
    def test_list_len(self):
        a = [3, "cat", "dog", 5, 6]
        assert len(a) == 5

    # Позитивный тест - прверка extend list
    def test_list_extend(self):
        a = [3, 4, 5, 6, 1]
        a.extend("cat")
        assert a == [3, 4, 5, 6, 1, "c", "a", "t"]

    # Позитивный тест - проверка append list
    def test_list_append(self):
        a = [3, 4, 5, 6, 1]
        a.append("cat")
        assert a == [3, 4, 5, 6, 1, "cat"]

    # Негативный тест - индексация list (выход за пределы списка)
    def test_list_neg_index_out(self):
        try:
            a = [3, 4, 5, 6, 1]
            g = a[15]
            assert g == a[15]
        except IndexError:
            pass

    # Параметризованный тест - list поиск по индексу
    @pytest.mark.parametrize("index, number", [(0, 3), (3, 9), (4, 12)])
    def test_some_index(self, index, number):
        a = [3, 4, 8, 9, 12, 16]
        assert a[index] == number

class TestTuple:
    # Позитивный тест - сложение tuple
    def test_tuple_concat(self):
        a = ('1', 1, '2', 2, '3', 3)
        b = ('4', 4, '5', 5, '8', 8)
        assert a + b == ('1', 1, '2', 2, '3', 3, '4', 4, '5', 5, '8', 8)

    # Негативный тест - индексация tuple (выход за пределы кортежа)
    def test_tuple_neg_index_out(self):
        try:
            a = ('One', 1, 'Two', 2, 'Three', 3)
            g = a[10]
            assert g == a[10]
        except IndexError:
            pass

    # Параметризованный тест - tuple работа count()
    @pytest.mark.parametrize('l, el, count', [[(1,), 1, 1], [('One', 1, 'One'), 'One', 2]])
    def test_tuple_params_count(self, l, el, count):
        a = l.count(el)
        assert a == count
