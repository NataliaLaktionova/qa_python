from main import BooksCollector
class TestBooksCollector:
    def test_add_new_book_add_duplicate_books(self):
        collector = BooksCollector()
        book_name = 'Игра престолов'
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        books = collector.get_books_genre()
        assert len(books) == 1
    def test_set_book_genre_existing_book(self):
        collector = BooksCollector()
        book_name = '1984'
        collector.add_new_book(book_name)
        genre = 'Фантастика'
        collector.set_book_genre(book_name, genre)
        book_genre = collector.get_book_genre(book_name)
        assert book_genre == genre
    def test_get_book_genre_existing_book(self):
        collector = BooksCollector()
        book_name = 'Мизери'
        collector.add_new_book(book_name)
        genre = 'Ужасы'
        collector.set_book_genre(book_name, genre)
        book_genre = collector.get_book_genre(book_name)
        assert book_genre == genre
    def test_get_books_with_specific_genre_three_books_1_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.add_new_book('Гарри Поттер и философский камень')
        collector.add_new_book('1984')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        collector.set_book_genre('Гарри Поттер и философский камень', 'Фантастика')
        collector.set_book_genre('1984', 'Фантастика')
        assert (collector.get_books_with_specific_genre('Фантастика') ==
                ['Властелин колец', 'Гарри Поттер и философский камень', '1984'])
    def test_get_books_genre_add_two_book_genre_not_set(self):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.add_new_book('Онегин')
        assert collector.get_books_genre() == {'Мастер и Маргарита': '', 'Онегин': ''}
    def test_get_books_genre_add_two_book_genre_set(self):
        collector = BooksCollector()
        collector.add_new_book('Властелин колец')
        collector.set_book_genre('Властелин колец', 'Фантастика')
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')
        assert collector.get_books_genre() == {'Властелин колец': 'Фантастика', '1984': 'Фантастика'}

    import pytest
    @pytest.mark.parametrize(
        'book,genre',
        [
            ['Душа', 'Мультфильмы'],
            ['Один дома', 'Комедии'],
            ['История Игрушек', 'Мультфильмы']
        ]
    )
    def test_get_books_for_children_add_three_book_and_child_genres(self, book, genre):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.get_books_for_children() == [book]
    def test_add_book_in_favourites_add_one_favourite_book(self):
        collector = BooksCollector()
        collector.add_new_book('Маленький принц')
        collector.add_book_in_favorites('Маленький принц')
        assert collector.get_list_of_favorites_books() == ['Маленький принц']
    def test_add_book_to_favorites_duplicate_favourite_book(self):
        collector = BooksCollector()
        collector.add_new_book('Маленький принц')
        collector.add_book_in_favorites('Маленький принц')
        collector.add_book_in_favorites('Маленький принц')
        assert collector.get_list_of_favorites_books() == ['Маленький принц']
    def test_delete_book_from_favourites_books_delete_added_book(self):
        collector = BooksCollector()
        collector.add_new_book('Великий Гэтсби')
        collector.add_book_in_favorites('Великий Гэтсби')
        collector.delete_book_from_favorites('Великий Гэтсби')
        assert 'Великий Гэтсби' not in collector.get_list_of_favorites_books()
    @pytest.mark.parametrize(
        'book',
        ['Великий Гэтсби', 'Мастер и Маргарита', 'Властелин колец']
    )
    def test_add_to_favorites_and_get_list_of_favorites_books(self, book):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        favorites_books = collector.get_list_of_favorites_books()
        assert book in favorites_books
