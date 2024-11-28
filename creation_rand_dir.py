import os #для работы с файловой системой 
import random
import string #для генерации случайных строк
def random_name(length=7):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length)) #все англ буквы + все цифры / выбирает случайно длинну символов из строки (буквы +цифры)/джоин обьединяет выбран символы  в строку 
def random_extension(): 
        extensions=['jpg', 'png', 'svg', 'jpeg', 'bmp', 'gif']
        return random.choice(extensions)
def create_random_dir(base_path): # Функция для создания структуры директорий с файлами
    main_dirs = [random_name() for _ in range(3) ] #[ ]- указывают что результат цикла будет сохранен в виде списка  
    for main_dir in main_dirs:
        main_dir_path= os.path.join(base_path, main_dir)
        os.makedirs(main_dir_path, exist_ok=True) # Объединяет путь к базовой папке (base_path) с именем новой папки (main_dir) в правильный формат пути для ОС
   #Вложенные директории внутри каждой основной директории
        sub_dirs= [random_name() for _ in range(2)]# Генерируем 3 случайных имени подпапок
        for sub_dir in sub_dirs:
            sub_dir_path = os.path.join(main_dir_path, sub_dir)
            os.makedirs(sub_dir_path, exist_ok=True )# Создаем подпапку
            #3 уровень вложенных директорий 
            sub_sub_dirs= [random_name() for _ in range(1)]# Генерируем 3 случайных имени подпапок
            for sub_sub_dir in sub_sub_dirs:
                sub_sub_dir_path = os.path.join(sub_dir_path, sub_sub_dir)
                os.makedirs(sub_sub_dir_path, exist_ok=True )# 
                for _ in range(3):
                    file_name =f"{random_name()}.{random_extension()}" # Генерируем случайное имя файла с расширением
                    file_path = os.path.join(sub_sub_dir_path, file_name)
                    with open(file_path, 'w') as file:
                        #file.write(f"{file_name}\nWhat do you know about random? ")
                        pass
                    print(f"created: {file_path}")
                    
        
if __name__ == '__main__':
    base_directory= os.path.join(os.getcwd(), "random_folders") # Создаём базовую папку в текущей директории
    os.makedirs(base_directory, exist_ok=True) #cоздаём базовую директорию если её нет
    create_random_dir(base_directory)
    print(f"folders created in {base_directory}")





    