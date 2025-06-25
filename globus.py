from lib_my import *
from rename_remove_duplicate import change_files
from authorization import authorize
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from inn_validation import append_inn_in_arr, inn_validation
from form import run_form, get_selected_values



login = "rsalahutdinov@rusmarine.ru"
passw = "rusmarine1991"

run_form()
selected_item, selected_file_path = get_selected_values()
ic(selected_item)
ic(selected_file_path)
if selected_item and selected_file_path:
    with webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) as driver:
        authorize(login, passw, driver)
        change_files(selected_file_path)
        inns = append_inn_in_arr(selected_file_path)
        for el in inns:
            inn_validation(driver, el, selected_item, selected_file_path)
