# Спасибо авторам за словарь https://github.com/danakt/russian-words

import os
import subprocess
import gzip

def convert_and_compress():
    input_files = [f for f in os.listdir('.') if f.endswith('.txt') and not f.endswith('_utf-8.txt')]
    combined_filename = 'ru_lang_utf8.txt'
    try:
        # Переводим в формат utf-8 и соединяем файлы в единый
        with open(combined_filename, 'w', encoding='utf-8') as combined_out:
            for filename in input_files:
                # Наш файл читаем как есть
                if filename == 'my_word.txt':
                    with open(filename, 'r', encoding='utf-8') as f:
                        combined_out.writelines(f)
                else:
                    subprocess.run(
                        ['iconv', '-f', 'WINDOWS-1251', '-t', 'UTF-8', filename],
                        stdout=combined_out,
                        check=True
                    )

        # Создание архива .gz под wordninja
        gz_filename = combined_filename + '.gz'
        with open(combined_filename, 'rt', encoding='utf-8', errors='replace') as f_in, \
             gzip.open(gz_filename, 'wt', encoding='utf-8') as f_out:
            for line in f_in:
                f_out.write(line)

        print(f"Архив был создан успешно: {gz_filename}")

    except subprocess.CalledProcessError as e:
        print(f"Ошибка при конвертации: {e}")

if __name__ == '__main__':
    convert_and_compress()
