import string

# Создание файла test_file.txt с примерным содержимым
with open('test_file.txt', 'w', encoding='utf-8') as file:
    file.write(
        "It's a text for task Найти везде,\n Используйте его для самопроверки.\n Успехов в решении задачи!\n "
        "text text text\n"
    )

class WordsFinder:
    def __init__(self, *file_names):
        # Преобразуем входные данные в список файлов
        self.file_names = [file.strip() for file in file_names[0].split(',')]

    def get_all_words(self):
        all_words = {}

        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    text = file.read().lower()
                    text = text.translate(str.maketrans('', '', string.punctuation))
                    words = text.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"Файл {file_name} не найден.")
            except Exception as e:
                print(f"Произошла ошибка при чтении файла {file_name}: {e}")

        return all_words

    def find(self, word):
        word = word.lower()
        results = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            if word in words:
                results[file_name] = words.index(word) + 1

        return results

    def count(self, word):
        word = word.lower()
        results = {}
        all_words = self.get_all_words()

        for file_name, words in all_words.items():
            count = words.count(word)
            if count > 0:
                results[file_name] = count

        return results

# Использование класса WordsFinder
finder2 = WordsFinder('test_file.txt')

# Получение всех слов из файлов
print(finder2.get_all_words())

# Поиск позиции слова 'text'
print(finder2.find('text'))

# Подсчет количества слов 'text'
print(finder2.count('text'))