def sed(arg1, arg2, filename1, filename2):
    arg1 = str(arg1)
    arg2 = str(arg2)
    try:
        file1 = open(filename1, 'r')  # БЕЗ кавычек!
        file2 = open(filename2, 'w')  # БЕЗ кавычек!
        try:
            for line in file1:
                new_line = line.replace(arg1, arg2)  # замена В СТРОКЕ либо измененная, либо та же самая
                file2.write(new_line)  # записываем результат (замененный или исходный)
        except:
            print('Что-то пошло не так при чтении и записи файлов.')                
    except:
        print('Что-то пошло не так при открытии файлов.')
    finally:
        try:
            file1.close()
            file2.close()
        except:
            print('Что-то пошло не так при закрытии файлов.')