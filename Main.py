import tkinter as tk

def open_menu():
    # Открываем новое окно для меню блюд
    menu_window = tk.Toplevel(root)
    menu_window.title("Меню блюд")

    # Создаем список блюд
    dishes = [
        "Чебурек",
        "Яичница с сосиской",
        "Гамбургер",
        "Кофе",
        "Чай черный (зеленый)",
        "Цезарь",
        "Пельмени",
        "Ролтон",
        "Овощи на пару",
        "Картошка с котлетой",
    ]

    # Отображаем блюда на новой странице
    for i, dish in enumerate(dishes, start=1):
        dish_label = tk.Label(menu_window, text=f"{i}. {dish}")
        dish_label.pack()

    # Добавляем кнопку для перехода к изменению цен
    price_button = tk.Button(menu_window, text="Изменить цены", command=open_price_page)
    price_button.pack()

    # Действия при нажатии кнопки "Меню"
    pass

def employees_clicked():
    # Действия при нажатии кнопки "Сотрудники"
    pass

def dealers_clicked():
    # Действия при нажатии кнопки "Дилеры"
    pass

def inventory_clicked():
    # Действия при нажатии кнопки "Инвентаризация"
    pass

def accounting_clicked():
    # Действия при нажатии кнопки "Бухгалтерия"
    pass

def support_clicked():
    # Действия при нажатии кнопки "Поддержка"
    pass

def logistics_clicked():
    # Действия при нажатии кнопки "Логистика"
    pass

def expiry_clicked():
    # Действия при нажатии кнопки "Срок годности"
    pass

# Создаем главное окно
root = tk.Tk()
root.title("Главное меню")

# Создаем кнопки
menu_button = tk.Button(root, text="Меню", command=open_menu)
employees_button = tk.Button(root, text="Сотрудники", command=employees_clicked)
dealers_button = tk.Button(root, text="Дилеры", command=dealers_clicked)
inventory_button = tk.Button(root, text="Инвентаризация", command=inventory_clicked)
accounting_button = tk.Button(root, text="Бухгалтерия", command=accounting_clicked)
support_button = tk.Button(root, text="Поддержка", command=support_clicked)
logistics_button = tk.Button(root, text="Логистика", command=logistics_clicked)
expiry_button = tk.Button(root, text="Срок годности", command=expiry_clicked)

# Располагаем кнопки на главном окне
menu_button.grid(row=0, column=0)
employees_button.grid(row=0, column=1)
dealers_button.grid(row=0, column=2)
inventory_button.grid(row=0, column=3)
accounting_button.grid(row=1, column=0)
support_button.grid(row=1, column=1)
logistics_button.grid(row=1, column=2)
expiry_button.grid(row=1, column=3)
import tkinter as tk


def open_price_page():
    # Открываем новое окно для изменения цен
    price_window = tk.Toplevel(root)
    price_window.title("Изменение цен")

    # Добавляем функциональность для изменения цен
    # (вы можете добавить текстовые поля и кнопки для изменения цен)

def open_add_dish_page():
    # Открываем новое окно для добавления блюда
    add_dish_window = tk.Toplevel(root)
    add_dish_window.title("Добавить блюдо")

    # Добавляем функциональность для добавления блюда
    # (вы можете добавить текстовые поля и кнопки для добавления блюда)

def open_approval_page():
    # Открываем новое окно для блюд на рассмотрении
    approval_window = tk.Toplevel(root)
    approval_window.title("Блюда на рассмотрении")

    # Добавляем функциональность для управления блюдами на рассмотрении
    # (вы можете добавить таблицу с блюдами и возможность одобрения или отказа)

def open_support_page():
    # Открываем новое окно для поддержки
    support_window = tk.Toplevel(root)
    support_window.title("Поддержка")

    # Добавляем информацию для поддержки и номер телефона
    support_label = tk.Label(support_window, text="Для вопросов по качеству работы, пожалуйста, звоните по номеру: 89108549212")
    support_label.pack()

def open_recipes_page():
    # Открываем сайт с рецептами
    import webbrowser
    webbrowser.open("https://eda.ru/recepty")

# Создаем главное окно

# Запускаем главный цикл приложения
root.mainloop()

# Запускаем главный цикл приложения
root.mainloop()
