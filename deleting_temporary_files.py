import os
import shutil

# Список директорий для поиска временных файлов
temp_directories = [
     '/private/var/folders',
    '~/Library/Caches',
    '~/Library/Logs',
    '~/Downloads',
    '~/Desktop'
]

# Список расширений файлов, подлежащих удалению 
extensions = [
    '.log',
    '.cache',
    '.tmp',
    '.dmg',
    '.pkg'
]

for directory in temp_directories:
    for dirpath, dirnames, filenames in os.walk(os.path.expanduser(directory)):
        for filename in filenames:
            # Проверяет, значится ли расширение файла в списке тех, что подлежат удалению 
            if os.path.splitext(filename)[1].lower() in extensions:
                filepath = os.path.join(dirpath, filename)
                try:
                    if os.path.isfile(filepath):
                        os.remove(filepath)
                    elif os.path.isdir(filepath):
                        shutil.rmtree(filepath)
                    print(f"Removed {filepath}")
                except Exception as e:
                    print(f"Error deleting {filepath}: {e}")
                    
    # Удаление скриншотов из директории Desktop
    if directory == '~/Desktop':
        desktop_path = os.path.expanduser(directory)  # expand ~ to home directory
        screenshot_files = [f for f in os.listdir(desktop_path) if f.startswith('Screenshot')]
        for file in screenshot_files:
            filepath = os.path.join(desktop_path, file)
            try:
                os.remove(filepath)
                print(f"Removed {filepath}")
            except Exception as e:
                print(f"Error deleting {filepath}: {e}")