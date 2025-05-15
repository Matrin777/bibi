from models.ganre import get_all_genres, get_genre_by_id
from models.ganre import Ganre

def menu_genres():
    while True:
        print("\n=== Жанры ===")
        print("1. Показать все жанры")
        print("2. Добавить жанр")
        print("3. Удалить жанр")
        print("4. Изменить жанр")
        print("0. Назад")
        choice = input("Выберите действие: ")

        if choice == "1":
            genres = get_all_genres()
            print("\nСписок жанров:")
            for g in genres:
                print(f"{g.codeganre} - {g.name}")
        elif choice == "2":
            name = input("Название жанра: ").strip()
            new_genre = Ganre(name=name)
            new_genre.save()
            print("Жанр добавлен.")
        elif choice == "3":
            code = input("Введите код жанра для удаления: ").strip()
            genre = get_genre_by_id(code)
            if genre:
                genre.delete()
                print("Жанр удален.")
            else:
                print("Жанр не найден.")
        elif choice == "4":
            code = input("Введите код жанра для редактирования: ").strip()
            genre = get_genre_by_id(code)
            if genre:
                new_name = input(f"Новое название ({genre.name}): ").strip()
                if new_name:
                    genre.name = new_name
                    genre.save()
                    print("Жанр обновлен.")
                else:
                    print("Название не изменено.")
            else:
                print("Жанр не найден.")
        elif choice == "0":
            break
        else:
            print("Неверный выбор.")