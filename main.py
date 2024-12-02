import tkinter as tk
from tkinter import ttk

# Данные заявок (глобальный массив для примера)
data = [
    (1, "2023-06-06", "Компьютер", "DEXP Aquilon 0286", "Перестал работать", "В процессе ремонта"),
    (2, "2023-05-05", "Компьютер", "DEXP Atlas H388", "Перестал работать", "В процессе ремонта"),
    (3, "2022-07-07", "Ноутбук", "MSI GF76 Katana", "Выключается", "Готова к выдаче"),
]

# Главная функция
def main_window():
    root = tk.Tk()
    root.title("Учет заявок")
    root.geometry("800x600")

    # Заголовок
    title_label = tk.Label(root, text="Список заявок", font=("Arial", 16))
    title_label.pack(pady=10)

    # Таблица
    columns = ("ID", "Дата", "Тип оргтехники", "Модель", "Описание", "Статус")
    global table
    table = ttk.Treeview(root, columns=columns, show="headings")

    for col in columns:
        table.heading(col, text=col)
        table.column(col, anchor="center")

    for row in data:
        table.insert("", tk.END, values=row)

    table.pack(fill="both", expand=True, padx=10, pady=10)

    # Кнопки
    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=10)

    add_btn = tk.Button(btn_frame, text="Добавить заявку", command=lambda: add_request_window())
    edit_btn = tk.Button(btn_frame, text="Редактировать заявку", command=lambda: edit_request_window())
    delete_btn = tk.Button(btn_frame, text="Удалить заявку", command=delete_request)

    add_btn.pack(side="left", padx=5)
    edit_btn.pack(side="left", padx=5)
    delete_btn.pack(side="left", padx=5)

    root.mainloop()

# Окно добавления заявки
def add_request_window():
    add_window = tk.Toplevel()
    add_window.title("Добавить заявку")
    add_window.geometry("400x400")

    # Поля ввода данных
    tk.Label(add_window, text="Дата").pack(pady=5)
    date_entry = tk.Entry(add_window)
    date_entry.pack(pady=5)

    tk.Label(add_window, text="Тип оргтехники").pack(pady=5)
    type_entry = tk.Entry(add_window)
    type_entry.pack(pady=5)

    tk.Label(add_window, text="Модель").pack(pady=5)
    model_entry = tk.Entry(add_window)
    model_entry.pack(pady=5)

    tk.Label(add_window, text="Описание проблемы").pack(pady=5)
    problem_entry = tk.Entry(add_window)
    problem_entry.pack(pady=5)

    tk.Label(add_window, text="Статус").pack(pady=5)
    status_entry = tk.Entry(add_window)
    status_entry.pack(pady=5)

    tk.Label(add_window, text="ID клиента").pack(pady=5)
    client_id_entry = tk.Entry(add_window)
    client_id_entry.pack(pady=5)

    # Кнопка сохранения
    def save_new_request():
        new_request = (
            len(data) + 1,
            date_entry.get(),
            type_entry.get(),
            model_entry.get(),
            problem_entry.get(),
            status_entry.get(),
            client_id_entry.get()
        )
        data.append(new_request)
        table.insert("", tk.END, values=new_request)
        add_window.destroy()

    tk.Button(add_window, text="Сохранить", command=save_new_request).pack(pady=10)

# Заглушки для редактирования и удаления
def edit_request_window():
    print("Открытие окна редактирования заявки")

def delete_request():
    print("Удаление выбранной заявки")

# Запуск приложения
main_window()
