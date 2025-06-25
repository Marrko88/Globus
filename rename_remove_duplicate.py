import pandas as pd

def change_files(file_path):
    delete_duplicates_inn(file_path)
    append_columns(file_path)

def delete_duplicates_inn(path_file):
    # Загрузите Excel-файл в DataFrame
    df = pd.read_excel(path_file)

    # Проверьте, есть ли колонка "ИНН"
    if "ИНН получателя" not in df.columns:
        print("Колонка 'ИНН получателя' не найдена.")
    else:
        # Удалите строки с повторяющимися значениями ИНН, оставив только первое вхождение
        df_unique = df.drop_duplicates(subset="ИНН получателя", keep="first")

        # Сохраните результат обратно в файл (можно указать новый файл)
        df_unique.to_excel(path_file, index=False)
        print("Строки с повторяющимися ИНН удалены. Файл сохранен.")

def append_columns(path_file):
    # Новые названия колонок
    new_columns = ["Сумма поставок в рублях млн. ₽", "Сумма поставок в млн. $", "Общий вес брутто в кг", "Общий вес нетто кг"]

    # Чтение файла Excel
    df = pd.read_excel(path_file)

    # Добавляем новые колонки с пустыми значениями (NaN)
    for col in new_columns:
        if col not in df.columns:
            df[col] = pd.NA  # Создаем новую колонку с пустыми значениями

    # Сохраняем результат в тот же файл Excel
    df.to_excel(path_file, index=False)
    print(f"Результат сохранен в файл: {path_file}")


