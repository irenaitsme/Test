# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

# создание окна, переход к сайту Яндекс
driver = webdriver.Chrome()
driver.get("https://ya.ru/")
# ввод в поле инпута текста "котики"
driver.find_element(By.CSS_SELECTOR, "#text").send_keys("котики")

# нажатие кнопки Найти
driver.find_element(By.XPATH, "/html/body/main/div[2]/form/div[3]/button").click()

# нажатие кнопки Видео
driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/nav/div[1]/a[3]").click()

# переход на следующую вкладку
driver.switch_to.window(driver.window_handles[1])

# наведение мыши на карточку видео
card = driver.find_element(By.XPATH, "/html/body/div[4]/div/main/div[2]/div/div[1]/section/ul/li[1]/div/div/div[1]/video")
ActionChains(driver).move_to_element(card).perform()

# сравнение побайтово двух скриншотов с интервалом в 1 сек
driver.save_screenshot("src1.png")
time.sleep(1)
driver.save_screenshot("src2.png")
assert (open("src1.png", "rb")).read() != (open("src2.png", "rb")).read(), "Это не видео!"

# закрытие окна
driver.close()
print("Вроде работает...")


