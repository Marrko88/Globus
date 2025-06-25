import tkinter as tk
from tkinter import filedialog

# Глобальные переменные для хранения выбранных значений
selected_value = None  # Здесь будет храниться значение из словаря
selected_file_path = None  # Путь к выбранному файлу

# Словарь для связи текстов (options) и значений (values)
value_map = {
        "Весь 2025 год": '//*[@id="datepicker"]/ul/li[1]/a',
        "Последние 12 месяцев": '//*[@id="datepicker"]/ul/li[2]/a',
        "Весь 2024 год": '//*[@id="datepicker"]/ul/li[3]/a',
        "Весь 2023 год": '//*[@id="datepicker"]/ul/li[4]/a',
        "Весь 2024+2025 год": '//*[@id="datepicker"]/ul/li[5]/a',
        "Весь 2023+2024+2025 год": '//*[@id="datepicker"]/ul/li[6]/a',
        "Весь доступный период": '//*[@id="datepicker"]/ul/li[7]/a',
    }

# Функция для выбора файла
def select_file():
    global selected_file_path
    filetypes = (("Excel files", "*.xlsx"), ("All files", "*.*"))
    filename = filedialog.askopenfilename(title="Выберите файл", filetypes=filetypes)
    if filename:
        selected_file_path = filename
        label_file.config(text=f"Выбранный файл: {filename}")
    else:
        label_file.config(text="Файл не выбран")

# Функция для обработки выбора
def submit_selection():
    global selected_value
    # Получаем значение из словаря по выбранному ключу
    selected_key = dropdown_var.get()
    if selected_key not in value_map:
        print("Ошибка: Выберите элемент из списка.")
        return
    selected_value = value_map[selected_key]  # Передаем значение, а не ключ
    if not selected_file_path:
        print("Ошибка: Выберите файл .xlsx.")
        return
    root.destroy()  # Полностью закрываем форму

# Функция для запуска формы
def run_form():
    global root, dropdown_var, label_file

    # Создаем главное окно
    root = tk.Tk()
    root.title("Форма с одиночным выбором и выбором файла")
    root.geometry("500x300")

    # Данные для выпадающего списка (тексты, которые видит пользователь)
    options = list(value_map.keys())

    # Переменная для хранения выбранного текста
    dropdown_var = tk.StringVar(root)
    dropdown_var.set("Выберите опцию")  # Устанавливаем значение по умолчанию

    # Метка для выпадающего списка
    label_dropdown = tk.Label(root, text="Выберите элемент из списка:")
    label_dropdown.pack(anchor="w", padx=10, pady=(10, 0))

    # Выпадающий список (OptionMenu)
    dropdown = tk.OptionMenu(root, dropdown_var, *options)
    dropdown.pack(pady=(0, 10))

    # Метка для выбора файла
    label_file = tk.Label(root, text="Файл не выбран", font=("Arial", 12))
    label_file.pack(pady=(10, 0))

    # Кнопка для выбора файла
    button_select_file = tk.Button(
        root,
        text="Выбрать файл (.xlsx)",
        command=select_file,
        bg="lightblue",
        fg="black"
    )
    button_select_file.pack(pady=(0, 10))

    # Кнопка для подтверждения выбора
    button_submit = tk.Button(
        root,
        text="Подтвердить",
        command=submit_selection,
        bg="lightgreen",
        fg="black"
    )
    button_submit.pack(pady=10)

    # Запуск главного цикла обработки событий
    root.mainloop()

# Функция для получения выбранных значений
def get_selected_values():
    return selected_value, selected_file_path