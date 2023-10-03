import tkinter as tk
import sqlite3

def open_menu():
    # Открываем новое окно для меню блюд
    menu_window = tk.Toplevel(root)
    menu_window.title("Меню блюд")

    # Создаем подключение к базе данных
    conn = sqlite3.connect('menu.db')
    c = conn.cursor()

    # Создаем таблицу, если она еще не существует
    c.execute('''CREATE TABLE IF NOT EXISTS dishes
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)''')

    # Получаем блюда из базы данных
    c.execute("SELECT name FROM dishes")
    dishes = c.fetchall()

    # Отображаем блюда на новой странице
    for i, dish in enumerate(dishes, start=1):
        dish_label = tk.Label(menu_window, text=f"{i}. {dish[0]}")
        dish_label.pack()

    # Закрываем соединение с базой данных
    conn.close()

def add_dish():
    # Открываем новое окно для добавления блюда
    add_dish_window = tk.Toplevel(root)
    add_dish_window.title("Добавить блюдо")

    def save_dish():
        # Получаем введенное название блюда
        dish_name = dish_entry.get()

        # Создаем подключение к базе данных
        conn = sqlite3.connect('menu.db')
        c = conn.cursor()

        # Добавляем блюдо в базу данных
        c.execute("INSERT INTO dishes (name) VALUES (?)", (dish_name,))
        conn.commit()

        # Закрываем соединение с базой данных
        conn.close()

        # Закрываем окно добавления блюда
        add_dish_window.destroy()

    # Создаем текстовое поле для ввода названия блюда
    dish_entry = tk.Entry(add_dish_window)
    dish_entry.pack()

    # Создаем кнопку для сохранения блюда
    save_button = tk.Button(add_dish_window, text="Сохранить", command=save_dish)
    save_button.pack()

# Создаем главное окно
root = tk.Tk()
root.title("Главное меню")

# Создаем кнопки
menu_button = tk.Button(root, text="Меню", command=open_menu)
add_dish_button = tk.Button(root, text="Добавить блюдо", command=add_dish)

# Располагаем кнопки на главном окне
menu_button.pack()
add_dish_button.pack()

# Запускаем главный цикл приложения
root.mainloop()