from lib_my import *

def authorize(login, passw, driver):
    url = 'https://glbs.io'
    driver.get(url)
    driver.maximize_window()
    log = (By.ID, 'email')
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(log)).send_keys(login)
    password = (By.ID, 'password')
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(password)).send_keys(passw)
    enter = (By.XPATH, '//*[@id="signin"]/div[4]/button')
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(enter)).click()
    time.sleep(10)


