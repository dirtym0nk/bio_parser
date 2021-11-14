import time

from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome(executable_path='driver/chromedriver')
f = open('bioinf.txt', 'w')
driver.get('https://fipi.ru/ege/otkrytyy-bank-zadaniy-ege#!/tab/173765699-6')
time.sleep(3)
driver.execute_script("window.scrollTo(0, 200)")
driver.find_element(By.XPATH,
                    '//a[@href="http://ege.fipi.ru/os11/xmodules/qprint/openlogin.php?proj=CA9D848A31849ED149D382C32A7A2BE4"]').click()
time.sleep(3)
if len(driver.window_handles) > 1:
    driver.switch_to.window(driver.window_handles[1])
driver.find_element(By.XPATH, '//a[text()="Клетка как биологическая система"]').click()

for i in range(2, 92):
    questions = []
    items = driver.find_elements(By.XPATH, '//table/tbody/tr/td/table//td[@valign="top"]/div/p[@class="MsoNormal"]')

    for question in items:
        if question.text.replace(" ", '') != "":
            questions.append(question.text)

    def ansewers_return(num):
        for answer in questions:
            words = driver.find_elements(By.XPATH, f'//p[text()="{questions[num]}"]/../../../../tr/td/table/tbody/tr/td')
            list_words = [item.text for item in words if item.text.strip() in ["1)", "2)", "3)", "4)", "5)", "6)"] or item.text.replace(" ", "") != ""]
            return list_words

    for asq in range(len(questions)):
        f.write(questions[asq] + "\n")
        for word in ansewers_return(asq):
            count = 1
            if word.strip() != '' and word.strip() not in ["1)", "2)", "3)", "4)", "5)", "6)"]:
                f.write(str(count) + ")" + word.strip() + "\n")
            count += 1
        f.write(" " + "\n")




    questions.clear()
    time.sleep(2)
    driver.find_element_by_xpath(
        f'//td[text()="Клетка как биологическая система (904)"]/../../tr/td//span[{i}]').click()
    time.sleep(4)
