from selenium import webdriver

class WebDriver:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://coinalyze.net/binance-coin/technical-analysis/')

    def refresh_page(self):
        self.driver.refresh()

    def get_current_price(self):
        price = float(self.driver.find_element('xpath', '/html/body/div/div[2]/div/div[3]/div[1]/div[1]/table/tbody/tr[2]/td').get_attribute('innerHTML'))
        return price

# This class is only written
# for webdriver construction
# and inheritance to other 
# child indicator classes.