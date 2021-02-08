my_file = open('File_new.txt', 'w')
line = input('Введите текст: ')
while line:
    my_file.writelines(line)
    line = input('Введите текст: ')
    if not line:
        break

my_file.close()
