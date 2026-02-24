test_add_new_book_add_two_books - проверка успешного добавления книги в словарь методом add_new_book
test_add_new_book_incorrect_name_book_not_added - проверка неуспешного добавления книги в словарь методом add_new_book, когда название некорректной длины
test_add_new_book_repeated_name_book_not_added- проверка неуспешного добавления книги в словарь методом add_new_book, когда книга с указанным названием уже есть в списке
test_add_new_book_add_book_empty_genre - проверка, что метод add_new_book добавляет в словарь книгу с пустым жанром
test_set_book_genre_genre_set_successfully - проверка успешной установки жанра книги методом set_book_genre
test_set_book_genre_incorrect_genre_not_set	- проверка неуспешной установки жанра книги методом set_book_genre, когда указанный жанр не входит в список genre
test_set_book_genre_uknown_book_genre_not_set - проверка неуспешной установки жанра книги методом set_book_genre, когда книги с указанным названием нет в словаре books_genre
test_get_books_with_specific_genre_return_rigth_books - проверка успешного получения книг с указанным жанром методом get_books_with_specific_genre
test_get_books_for_children - проверка успешного получения списка книг, которые подходят детям, методом get_books_for_children
test_add_book_in_favorites_book_added - проверка успешного добавления книги в избранное методом add_book_in_favorites
test_add_book_in_favorites_book_uknown_book_not_added - проверка неуспешного добавления книги в избранное методом add_book_in_favorites, когда книги с указанным названием нет в словаре books_genre
test_add_book_in_favorites_book_repeated_name_book_not_added - проверка неуспешного добавления книги в избранное методом add_book_in_favorites, когда книга с указанным названием уже есть в списке
test_delete_book_from_favorites_book_deleted - проверка успешного удаления книги из избранного методом delete_book_from_favorites
test_get_list_of_favorites_books_return_right_list - проверка успешного получения списка избранных книг методом get_list_of_favorites_books
test_get_books_genre_return_right_dictionary - проверка успешного получения словаря books_genre методом get_books_genre
test_get_book_genre_return_right_genre - проверка успешного получения жанра книги по названию методом get_book_genre
