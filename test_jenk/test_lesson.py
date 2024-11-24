import time

import allure
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from selene import Config, by, be
from selenium import webdriver
import pytest

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')  # Открыть в максимальном размере

# Инициализируем драйвер с заданными опциями
driver = webdriver.Chrome(options=options)

# Привязываем драйвер к browser
browser.config.driver = driver


def test_br():
    browser.open("https://github.com")
    s('//*[@data-target="qbsearch-input.inputButtonText"]').click()
    s('//input[@id="query-builder-test"]').send_keys("eroshenkoam/allure-example")
    s('//input[@id="query-builder-test"]').submit()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step("Открываем таб Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие Issue с номером 76"):
        s(by.partial_text("#76")).should(be.visible)

test_br()
