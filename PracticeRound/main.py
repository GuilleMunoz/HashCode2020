import sys

def read(file_name):
    with open(file_name + '.in') as file:
        max_num_slices, num_dif_types_pizza = file.readline().split(' ')
        return int(max_num_slices), int(num_dif_types_pizza), file.readline().split(' ')


def write(file_name, ret):
    with open(file_name + '_sol.txt', 'w') as file:
        file.write(str(len(ret)) + '\n')
        for slices in ret:
            file.write(str(slices) + ' ')

def chose_slices(max_num_slices, num_dif_types_pizza, types_pizza):

    ret = list()

    while True:
        while True:
            num_slices = int(types_pizza.pop())
            num_dif_types_pizza -= 1

            if num_slices <= max_num_slices:
                ret.insert(0, num_dif_types_pizza)
                max_num_slices -= num_slices
                break
            elif len(types_pizza) == 0:
                break
        if num_dif_types_pizza == 0 or len(types_pizza) == 0:
            break

    return ret

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        max_num_slices, num_dif_types_pizza, types_pizza = read(arg)
        write(arg, chose_slices(max_num_slices, num_dif_types_pizza, types_pizza))