import time

from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome(executable_path='driver/chromedriver')

driver.get('https://fipi.ru/ege/otkrytyy-bank-zadaniy-ege#!/tab/173765699-6')
time.sleep(3)
driver.execute_script("window.scrollTo(0, 200)")
driver.find_element(By.XPATH,
                    '//a[@href="http://ege.fipi.ru/os11/xmodules/qprint/openlogin.php?proj=CA9D848A31849ED149D382C32A7A2BE4"]').click()
time.sleep(3)
if len(driver.window_handles) > 1:
    driver.switch_to.window(driver.window_handles[1])
driver.find_element(By.XPATH, '//a[text()="Клетка как биологическая система"]').click()

# def numiration(num):
#     return driver.find_element_by_xpath(
#         f'//td[text()="Клетка как биологическая система (904)"]/../../tr/td//span[{num}]')


for i in range(2, 92):
    questions = []
    items = driver.find_elements(By.XPATH, '//table/tbody/tr/td/table//td[@valign="top"]/div/p[@class="MsoNormal"]')

    for question in items:
        if question.text.replace(" ", '') != "":
            questions.append(question.text)
    words_list = []
    for answer in questions:
        count = 0
        words = driver.find_elements(By.XPATH, f'//p[text()="{questions[count]}"]/../../../../tr/td/table/tbody/tr/td')

        for word in words:
            if word.text.strip() in ["1)", "2)", "3)", "4)", "5)", "6)"]:
                words_list.append(word.text)
            elif word.text.replace(" ", "") != "":
                words_list.append(word.text)

        print(questions[count])
        for ipa in words_list:
            print(ipa + '\n')
        count += 1

        words_list.clear()

    questions.clear()

    time.sleep(2)
    questions.clear()
    driver.find_element_by_xpath(
        f'//td[text()="Клетка как биологическая система (904)"]/../../tr/td//span[{i}]').click()
    time.sleep(5)
