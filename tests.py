from main import BooksCollector
import pytest

class TestBooksCollector:
    
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('name', ['', 'Одиннадцать'*4])
    def test_add_new_book_incorrect_name_book_not_added(self, name):
        collector = BooksCollector()

        collector.add_new_book(name)

        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_repeated_name_book_not_added(self):
        collector = BooksCollector()

        collector.add_new_book('Улитка на склоне')
        collector.add_new_book('Улитка на склоне')

        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_add_book_empty_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Иду на грозу')

        assert len(collector.get_book_genre('Иду на грозу')) == 0
		
    def test_set_book_genre_genre_set_successfully(self):
        collector = BooksCollector()

        collector.add_new_book('Роркх')
        collector.set_book_genre('Роркх', 'Фантастика')

        assert collector.get_book_genre('Роркх') == 'Фантастика'

    def test_set_book_genre_incorrect_genre_not_set(self):
        collector = BooksCollector()

        collector.add_new_book('Чайковский')
        collector.set_book_genre('Чайковский', 'Биография')

        assert collector.get_book_genre('Чайковский') == ''

    def test_set_book_genre_uknown_book_genre_not_set(self):
        collector = BooksCollector()

        collector.set_book_genre('Десять негритят', 'Детективы')

        assert collector.get_book_genre('Десять негритят') == None

    def test_get_books_with_specific_genre_return_rigth_books(self):
        collector = BooksCollector()

        collector.add_new_book('Солярис')
        collector.set_book_genre('Солярис', 'Фантастика')
        collector.add_new_book('Космический десант')
        collector.set_book_genre('Космический десант', 'Фантастика')
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')

        assert len(collector.get_books_with_specific_genre('Фантастика')) == 2

    def test_get_books_for_children(self):
        collector = BooksCollector()

        collector.add_new_book('Солярис')
        collector.set_book_genre('Солярис', 'Фантастика')
        collector.add_new_book('Внутри убийцы')
        collector.set_book_genre('Внутри убийцы', 'Детективы')
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')

        assert len(collector.get_books_for_children()) == 1

    def test_add_book_in_favorites_book_added(self):
        collector = BooksCollector()

        collector.add_new_book('Случайная вакансия')
        collector.add_book_in_favorites('Случайная вакансия')

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_add_book_in_favorites_book_uknown_book_not_added(self):
        collector = BooksCollector()

        collector.add_book_in_favorites('Первое правило волшебника')

        assert len(collector.get_list_of_favorites_books()) == 0

    def test_add_book_in_favorites_book_repeated_name_book_not_added(self):
        collector = BooksCollector()

        collector.add_new_book('Пещера')
        collector.add_book_in_favorites('Пещера')
        collector.add_book_in_favorites('Пещера')

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites_book_deleted(self):
        collector = BooksCollector()

        collector.add_new_book('Ханский огонь')
        collector.add_book_in_favorites('Ханский огонь')
        collector.delete_book_from_favorites('Ханский огонь')

        assert len(collector.get_list_of_favorites_books()) == 0

    def test_get_list_of_favorites_books_return_right_list(self):
        collector = BooksCollector()

        collector.add_new_book('Колыбель для кошки')
        collector.add_book_in_favorites('Колыбель для кошки')
        collector.add_new_book('Псоглавцы')
        collector.add_book_in_favorites('Псоглавцы')
        collector.add_new_book('Воскремение')

        assert collector.get_list_of_favorites_books() == ['Колыбель для кошки', 'Псоглавцы']

    def test_get_books_genre_return_right_dictionary(self):
        collector = BooksCollector()

        collector.add_new_book('Война миров')
        collector.set_book_genre('Война миров', 'Фантастика')
        collector.add_new_book('Дюна')

        assert collector.get_books_genre() == {'Война миров': 'Фантастика', 'Дюна': ''}

    def test_get_book_genre_return_right_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Убийство в Восточном экспрессе')
        collector.set_book_genre('Убийство в Восточном экспрессе', 'Детективы')

        assert collector.get_book_genre('Убийство в Восточном экспрессе') == 'Детективы'
