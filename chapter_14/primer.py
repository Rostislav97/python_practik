import os
#Изначальная функция
def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)


walk('python')




def new_walk(dirname):
    for current_dir, dirs, files in os.walk(dirname):
        for file in files:  # проходим по каждому файлу в текущей папке
            path = os.path.join(current_dir, file)
            print(path)

# Проверка
new_walk('.')