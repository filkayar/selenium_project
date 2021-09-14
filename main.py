from selenium import webdriver

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
        pass


def main():
    driver = webdriver.Chrome('drivers/chromedriver.exe')
    parcer = ParserOne(driver, 'python')
    parcer.parce()

if __name__ == "__main__":
    main()

