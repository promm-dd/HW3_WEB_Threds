import os #для работы с файловой системой 
import shutil #для копиров файлов и директорий 
from pathlib import Path #для работ с путями к директ 
from concurrent.futures import ThreadPoolExecutor #модуль для управл многопоточностью позволяет запускать функции в неск потоках одновременно
def copy_file(file_path, target_dir):
    try:
        file_extension = Path(file_path).suffix.lstrip('.').lower() or 'no_extension' #определ расшир файла, если его нет использ no_extension
        target_subdir = os.path.join(target_dir, file_extension)#соединяем путь к целевой директории() с названием поддиректории основанной на расшир файла 
        os.makedirs(target_subdir, exist_ok=True) #созд поддиректорию, если она не существует 
        shutil.copy2(file_path, target_subdir ) #copy2- копирует все что делает copy, + метаданные файла (время )и тд 
        print(f"copied: {file_path} -> {target_subdir}")
    except Exception as e:
        print(f"error copy {file_path}: {e}")
#функц сбора файлов 
def collect_files(source_dir):
    try:
        files = []
        for root, dirs, filenames in os.walk(source_dir): #root -текущ директория,  dirs- список директорий, filenames- список файлов в дир
            for filename in filenames: #перебираем файлы в текущ директор
                files.append(os.path.join(root, filename))#добавл полный путь файла в список 
        return files
    except Exception as e:
        print(f"error {e}")
        return []

def main(source_dir, target_dir, max_workers=4):
    files = collect_files(source_dir)
    os.makedirs(target_dir, exist_ok=True) #созд поддиректорию, если она не существует 
    with ThreadPoolExecutor(max_workers=max_workers) as executor: #создаем пул потоков max_workers задает кол-во одновременно работ потоков 
        for file_path in files:
            executor.submit(copy_file, file_path, target_dir) #отравляем задачу (копир файлов) в пул потоков 
    print("Executed")
    
if __name__ == '__main__':
    source_dir = input("enter main path dir:").strip()
    target_dir= input("enter target path dir:").strip()
    max_threads= int(input("threads:"))
    main(source_dir, target_dir, max_threads)

    
    