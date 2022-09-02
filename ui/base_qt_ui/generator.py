# для работы с установленной ОС, а также файловой системой ПК
import os
# для работы с регулярными выражениями
import re

def generation_ui_py(path: str):
    # получили список всех файлов в каталоге
    files = os.listdir(path)
    ui_list = []


    # регулярное выражение по нахождению файлов с расширением ui
    # r - чтобы вывести содержимое иначе получим ссылку; "." Один любой символ, кроме новой строки; "*" 0 и более вхождений шаблона слева; "\." означает точку
    pattern = re.compile(r'.*\.ui')

    # пробежались по директории и если есть ui добавили имя в список
    for i in files:
        if pattern.match(i):
            ui_list.append(i)

    # проходимся по всем названиям в списке ui и применяем команду конвертации
    for i in ui_list:
        # получили путь ui файла
        file_path = os.path.join(path, i)
        # получаем имя файла(получили имя ui файла и удалили последний элемент - расширение ui)
        file_name = file_path.split(os.sep)[-1].removesuffix('.ui')

        # команда конвертации
        cmd = f' pyside6-uic {file_path} > {path}{os.sep}{file_name}.py'

        os.popen(cmd)

if __name__=='__main__':
    # передали в функцию каталог, где лежит фаил генерации
    generation_ui_py(os.path.dirname((os.path.abspath(__file__))))