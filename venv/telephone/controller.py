from database import *   #импорт из файла database
from view import *       #импорт из файла view

def main():
    while True:
        num = input_num() #вызываем функцию из view
        if num == 1:
            name = input_name()
            write_name(name)
            print("Записано\n")

        if num == 2:
            a == input_found()
            print(read_found(a))

main()