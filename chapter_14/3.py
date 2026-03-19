import os
import hashlib

def calculate_md5(file_path):  # Исправил название
    hasher = hashlib.md5()
    try:
        with open(file_path, 'rb') as f:
            while True:  # Добавил цикл
                chunk = f.read(4096)
                if not chunk:
                    break
                hasher.update(chunk)
        return hasher.hexdigest()  # Добавил возврат хэша
    except (IOError, OSError):
        return None

def find_duplicates(dirname):  # Переименовал finaly
    duplicates = {}
    
    for current_dir, dirs, files in os.walk(dirname):
        for file in files:
            if os.path.splitext(file)[1] == ".mp3":
                path = os.path.join(current_dir, file)
                file_hash = calculate_md5(path)  # Правильное название
                
                if file_hash:
                    if file_hash in duplicates:
                        duplicates[file_hash].append(path)
                    else:
                        duplicates[file_hash] = [path]
    
    return duplicates

# Использование:
result = find_duplicates("/путь/к/папке")

# Вывод результатов:
for file_hash, paths in result.items():
    if len(paths) > 1:
        print(f"Найдены дубликаты ({len(paths)} файлов):")
        for path in paths:
            print(f"  {path}")