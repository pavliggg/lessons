import hashlib
import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hashlib.sha256(password.encode()).hexdigest()  # Хэширование пароля
        self.age = age


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration  # Продолжительность в секундах
        self.time_now = 0  # Текущая секунда воспроизведения
        self.adult_mode = adult_mode  # Ограничение по возрасту


class UrTube:
    def __init__(self):
        self.users = []  # Список пользователей
        self.videos = []  # Список видео
        self.current_user = None  # Текущий пользователь

    def log_in(self, nickname, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                print(f"Пользователь {nickname} вошел в систему.")
                return
        print("Неверный логин или пароль.")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует.")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f"Пользователь {nickname} зарегистрирован и вошел в систему.")

    def log_out(self):
        self.current_user = None
        print("Вы вышли из системы.")

    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)
                print(f"Видео '{video.title}' добавлено.")
            else:
                print(f"Видео '{video.title}' уже существует.")

    def get_videos(self, search_term):
        return [video.title for video in self.videos if search_term.lower() in video.title.lower()]

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео.")
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу.")
                    return

                print(f"Начинаем просмотр видео '{video.title}'")
                while video.time_now < video.duration:
                    print(f"Просмотр: {video.time_now} сек.")
                    time.sleep(1)  # Имитация воспроизведения
                    video.time_now += 1
                print("Конец видео")
                video.time_now = 0  # Сброс времени просмотра
                return

        print("Видео не найдено.")


# Пример использования
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))  # ['Лучший язык программирования 2024 года']
print(ur.get_videos('ПРОГ'))  # ['Лучший язык программирования 2024 года']

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')  # Войдите в аккаунт, чтобы смотреть видео
ur.register('vasya_pupkin', 'lolkekcheburek', 13)  # Регистрация
ur.watch_video('Для чего девушкам парень программист?')  # Вам нет 18 лет, пожалуйста покиньте страницу
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)  # Регистрация
ur.watch_video('Для чего девушкам парень программист?')  # Начинаем просмотр видео

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)  # Пользователь vasya_pupkin уже существует.
print(ur.current_user)  # <__main__.User object at ...>

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')  # Видео не найдено.