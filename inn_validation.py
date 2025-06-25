from lib_my import *


def append_inn_in_arr(path_file):
    inns =[]
    # Загрузите Excel-файл в DataFrame
    df = pd.read_excel(path_file)

    # Проверьте, есть ли колонка "ИНН"
    if "ИНН получателя" not in df.columns:
        print("Колонка 'ИНН получателя' не найдена.")
    else:
        inns = df['ИНН получателя'].dropna().astype(str).tolist()
    return inns

def extract_numbers_with_spaces(value):
    # Приведение к строке и очистка от лишних символов (оставляем только цифры, точки и запятые)
    value_str = str(value).strip()
    cleaned = re.sub(r'[^\d.,]', '', value_str).replace(',', '.')
    # Удаляем последнюю точку, если она есть
    if cleaned.endswith('.'):
        cleaned = cleaned[:-1]
    return cleaned


def append_value(inn, value, column, file_path):
    try:
        print(f"[DEBUG] Обработка ИНН: {inn}, колонка: {column}")

        df = pd.read_excel(file_path)

        inn_column = "ИНН получателя"

        # Преобразование типов
        df[inn_column] = df[inn_column].astype(str)
        inn = str(inn)

        if column not in df.columns:
            df[column] = ''

        df[column] = df[column].astype(str)

        numeric_value = extract_numbers_with_spaces(value)

        # Поиск строки
        matched = df[df[inn_column] == inn]
        print(f"[DEBUG] Найдено совпадений: {len(matched)}")

        if not matched.empty:
            df.loc[df[inn_column] == inn, column] = numeric_value or ''
        else:
            print(f"[WARNING] ИНН {inn} не найден в таблице!")

        # Сохранение
        df.to_excel(file_path, index=False)

        # Принудительная запись на диск
        with open(file_path, 'r+b') as f:
            f.flush()
            os.fsync(f.fileno())

        print(f"Результат сохранён в файл: {file_path}, значение: {numeric_value}")
        return True

    except Exception as e:
        print(f"[Ошибка при сохранении] {e}")
        return False





def inn_validation(driver, inn, li, file_path):
    try:
        inn = int(inn.split('.')[0])
    except:
        inn = "00000000"
    driver.get("https://glbs.io/my/fea-ru/search/")
    period = (By.XPATH, '//*[@id="datepicker"]/button')
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(period)).click()
    li_period = (By.XPATH, li)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(li_period)).click()
    inn_locator = (By.NAME, 'G081')
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(inn_locator)).send_keys(inn)
    submitForm = (By.ID, 'submitForm')
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(submitForm)).click()

    time.sleep(2)

    try:
        supply_amount_in_rubles = driver.find_element(By.XPATH, "//*[@id='saveArea']/table[2]/tbody/tr[2]/td[1]/span[1]").text # Сумма поставок в рублях млн. ₽
        append_value(inn, supply_amount_in_rubles, "Сумма поставок в рублях млн. ₽",file_path)
        supply_amount_in_usd = driver.find_element(By.XPATH, "//*[@id='saveArea']/table[2]/tbody/tr[3]/td[1]/span[1]").text # Сумма поставок в долларах США
        append_value(inn, supply_amount_in_usd, "Сумма поставок в млн. $", file_path)
        total_weight_is_gross = driver.find_element(By.XPATH, "//*[@id='saveArea']/table[2]/tbody/tr[4]/td[1]/span[1]").text  # Общий вес брутто
        append_value(inn, total_weight_is_gross, "Общий вес брутто в кг", file_path)
        total_weight_is_netto = driver.find_element(By.XPATH, "//*[@id='saveArea']/table[2]/tbody/tr[5]/td[1]/span[1]").text # Общий вес нетто
        append_value(inn, total_weight_is_netto, "Общий вес нетто кг", file_path)
    except:
        supply_amount_in_rubles = ''  # Сумма поставок в рублях млн. ₽
        append_value(inn, supply_amount_in_rubles, "Сумма поставок в рублях млн. ₽", file_path)
        supply_amount_in_usd = ''  # Сумма поставок в долларах США
        append_value(inn, supply_amount_in_usd, "Сумма поставок в млн. $", file_path)
        total_weight_is_gross = ''  # Общий вес брутто
        append_value(inn, total_weight_is_gross, "Общий вес брутто в кг", file_path)
        total_weight_is_netto = ''  # Общий вес нетто
        append_value(inn, total_weight_is_netto, "Общий вес нетто кг", file_path)