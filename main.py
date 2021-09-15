from selenium import webdriver
from model import *

class ParserOne:

    def __init__(self, driver, lang):
        self.driver=driver
        self.lang=lang

    def parce(self):
        self.go_to_page_test()
        self.parce_question()

    def go_to_page_test(self):
        self.driver.get('https://proghub.ru/tests')
        list_el = self.driver.find_elements_by_tag_name('a')

        for el in list_el:
            link = el.get_attribute('href')
            if self.lang in link:
                html_link = link.split('/')[-1]
                self.driver.get('https://proghub.ru/q/random/t/'+html_link)
                break
        
    def parce_question(self):
        quest = Question()
        self.fill_question_text(quest)
        self.fill_question_code(quest)
        self.fill_question_answer(quest)
        print(quest)

    def fill_question_text(self, quest):
        try:
            quest.text = self.driver.find_element_by_class_name('lightblack-text').text
        except:
            print('Question text missing.')
        
    def fill_question_code(self, quest):
        try:
            quest.code = self.driver.find_element_by_class_name('code').text
        except:
            pass

    def fill_question_answer(self, quest):
        answer = self.driver.find_element_by_class_name('answer_item')
        answer.click()
        try:
            answer = self.driver.find_element_by_class_name('q-answer')
            answer.click()

            all_answer = self.driver.find_elements_by_class_name('answer_item')
            for el in all_answer:
                answer = [el.text, False]
                if not ('incorrect' in el.get_attribute('class')):
                    answer[1] = True
                quest.answer.append(answer)
        except:
            print('No q-answer button')


def main():
    driver = webdriver.Chrome('drivers/chromedriver.exe')
    parcer = ParserOne(driver, 'python')
    parcer.parce()

if __name__ == "__main__":
    main()

