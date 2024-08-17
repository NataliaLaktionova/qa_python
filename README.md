# qa_python
Покрыты 12 тестами методы BooksCollector:
1.test_add_new_book_add_duplicate_books: Проверка на то, что количество книг после добавления одной книги дважды будет равно 1.
2.test_set_book_genre_existing_book: Проверка корректной установки жанра для добавленной книги
3.test_get_book_genre_existing_book: Проверка получения валидного жанра для добавленной книги
4.test_get_books_with_specific_genre_three_books_1_genre: Проверка возврата книг для указанного жанра 'Фантастика' (несколько книг принадлежат к одному жанру)
5.test_get_books_genre_add_two_book_genre_not_set: Проверка возврата книг с их жанрами, когда жанры не были установлены.
6.test_get_books_genre_add_two_book_genre_set: Проверка возврата книг с их жанрами после установки жанров для книг.
7.test_get_books_for_children_add_three_book_and_child_genres: Проверка возврата 3 книг для детей в зависимости от их указанных жанров.
8.test_add_book_in_favourites_add_one_favourite_book: Проверка добавления 1 книги в избранное
9.test_add_book_to_favorites_duplicate_favourite_book: Проверка добавления одной и той же книги в избранное дважды не приводит к дублированию
10.test_delete_book_from_favourites_books_delete_added_book: Проверка удаления 1 книги из избранного
11.test_add_to_favorites_and_get_list_of_favorites_books: Проверка добавления книги в избранное и получение списка избранных книг (применена параметризация)
12.test_get_list_of_favorites_books_empty: Проверка возвращения пустого списка избранного при отсутствии добавленных книг в список
