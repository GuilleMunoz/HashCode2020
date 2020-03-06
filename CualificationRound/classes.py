
class Library:

    def __init__(self ,library_id, signup_process, books_per_day, books):
        self.library_id = library_id
        self.signup_process =  signup_process
        self.books_per_day = books_per_day
        self.books = self.sort_by_value(books)

    def sort_by_value(self, books):
        return dict(sorted(books.items(), key = lambda kv:(kv[1], kv[0]), reverse = True))

    def get_score(self, total_time, current_time, scanned_books):

        scanning_days = total_time - current_time - self.signup_process

        if scanning_days <= 0:
            return -1

        delete = [key for key in self.books if key in scanned_books]

        for key in delete:
            del self.books[key]

        total_score = sum(list(self.books.values())[:scanning_days*self.books_per_day])

        delete = [key for key in list(self.books.keys())[scanning_days*self.books_per_day + 1:]]

        for key in delete:
            del self.books[key]

        return total_score/self.signup_process

    def set_scanned_books(self, scanned_books):

        scanned_books.update(self.books.keys())

    def __str__(self):
        self.books.keys()
