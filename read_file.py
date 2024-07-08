from pprint import pprint


with open('1.txt', 'r', encoding='utf-8') as file_1:
    read_file_1 = file_1.readlines()
    long = len(read_file_1)
    ready_file_1 = list()
    for i in range(long):
        count_str = [f'Строка номер {i + 1} файла номер 1']
        ready_file_1.extend(count_str)


with open('2.txt', 'r', encoding='utf-8') as file_2:
    read_file_2 = file_2.readlines()
    long = len(read_file_2)
    ready_file_2 = list()
    for i in range(long):
        count_str = [f'Строка номер {i + 1} файла номер 2']
        ready_file_2.extend(count_str)


with open('3.txt', 'r', encoding='utf-8') as file_3:
    read_file_3 = file_3.readlines()
    long = len(read_file_3)
    ready_file_3 = list()
    for i in range(long):
        count_str = [f'Строка номер {i + 1} файла номер 3']
        ready_file_3.extend(count_str)


the_final_file = list()
the_final_file.append(ready_file_1)
the_final_file.append(ready_file_2)
the_final_file.append(ready_file_3)
the_final_file.sort(key=len)
my_string = '\n'.join(str(element) for element in the_final_file)

with open('file.txt', 'w', encoding='utf-8') as file:
    file.write(my_string)
