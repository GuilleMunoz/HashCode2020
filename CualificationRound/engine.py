from CualificationRound.classes import Library


file_n = str()
libraries = list()
scanned_books = set()
solution = list()
total_time = 0
current_time = 0

def read(file_name):
    global total_time
    global libraries
    global file_n

    file_n = file_name

    with open(file_name + '.txt') as file:
        total_time = int(file.readline().split(' ')[2])

        scores = list(map(int, file.readline().split(' ')))

        i = 0

        while True:

            library_id = i
            line = file.readline()

            if not line:
                break

            signup_process, books_per_day = list(map(int, line.split(' ')[1:]))

            books = dict()
            for book in list(map(int, file.readline().split(' '))):
                books[book] = scores[book]

            libraries.append(Library(library_id, signup_process, books_per_day, books))

            i += 1

def get_best():

    global total_time
    global current_time
    global libraries

    max_i = 0;
    max_value = libraries[0].get_score(total_time, current_time, scanned_books)

    for i in range(1, len(libraries)):
        score = libraries[i].get_score(total_time, current_time, scanned_books)
        if score > max_value:
            max_value = score
            max_i = i

    return max_i


def get_solution():

    global solution
    global libraries
    global current_time
    global total_time
    global file_n

    while True:
        if len(libraries) == 0 or total_time <= current_time:
            print('fin')
            break

        max_i = get_best()
        current_time += libraries[max_i].signup_process

        if total_time <= current_time:
            print('fin')
            break


        print(end='\r')
        print('processing %s : ' % file_n, 100*current_time/total_time, '%', end=' ')


        libraries[max_i].set_scanned_books(scanned_books)
        solution.append(libraries[max_i])
        del libraries[max_i]


def write_solution(file_name):

    global solution

    with open(file_name + '_sol.txt', 'w') as file:
        file.write(str(len(solution)) + '\n')

        score = 0

        for library in solution:
            file.write(str(library.library_id) + ' ' + str(len(library.books.keys())) + '\n')
            file.write(' '.join(list(map(str ,library.books.keys()))) + '\n')
            score += sum(library.books.values())


    print(score)

if __name__ == '__main__':
    #'b_read_on''f_libraries_of_the_world''d_tough_choices''c_incunabula''e_so_many_books'
    file_name = 'a_example'
    read(file_name)
    get_solution()
    write_solution(file_name)