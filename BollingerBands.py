from WebDriver import WebDriver as wd

def extract_value(driver, xpath):
    value = float(driver.find_element('xpath', xpath).get_attribute('innerHTML'))
    return value

class BollingerBands(wd):

    # Receive Upper Value

    def get_upper_value_5m(self):
        value = extract_value(self.driver, '/html/body/div/div[2]/div/div[3]/div[2]/table/tbody/tr[20]/td[2]/span[1]/text()[1]')
        return value

    def get_upper_value_15m(self):
        value = extract_value(self.driver, '/html/body/div/div[2]/div/div[3]/div[2]/table/tbody/tr[20]/td[3]/span[1]/text()[1]')
        return value

    def get_upper_value_1h(self):
        value = extract_value(self.driver, '/html/body/div/div[2]/div/div[3]/div[2]/table/tbody/tr[20]/td[4]/span[1]/text()[1]')
        return value

    def get_upper_value_2h(self):
        value = extract_value(self.driver, '/html/body/div/div[2]/div/div[3]/div[2]/table/tbody/tr[20]/td[5]/span[1]/text()[1]')
        return value

    def get_upper_value_4h(self):
        value = extract_value(self.driver, '/html/body/div/div[2]/div/div[3]/div[2]/table/tbody/tr[20]/td[6]/span[1]/text()[1]')
        return value

    def get_upper_value_6h(self):
        value = extract_value(self.driver, '/html/body/div/div[2]/div/div[3]/div[2]/table/tbody/tr[20]/td[7]/span[1]/text()[1]')
        return value

    def get_upper_value_1d(self):
        value = extract_value(self.driver, '/html/body/div/div[2]/div/div[3]/div[2]/table/tbody/tr[20]/td[8]/span[1]/text()[1]')
        return value

    # Receive Lower Value

    def get_lower_value_5m(self):
        value = extract_value(self.driver, '/html/body/div/div[2]/div/div[3]/div[2]/table/tbody/tr[20]/td[2]/span[1]/text()[2]')
        return value

    def get_lower_value_15m(self):
        value = extract_value(self.driver, '/html/body/div/div[2]/div/div[3]/div[2]/table/tbody/tr[20]/td[3]/span[1]/text()[2]')
        return value

    def get_lower_value_1h(self):
        value = extract_value(self.driver, '/html/body/div/div[2]/div/div[3]/div[2]/table/tbody/tr[20]/td[4]/span[1]/text()[2]')
        return value

    def get_lower_value_2h(self):
        value = extract_value(self.driver, '/html/body/div/div[2]/div/div[3]/div[2]/table/tbody/tr[20]/td[5]/span[1]/text()[2]')
        return value

    def get_lower_value_4h(self):
        value = extract_value(self.driver, '/html/body/div/div[2]/div/div[3]/div[2]/table/tbody/tr[20]/td[6]/span[1]/text()[2]')
        return value

    def get_lower_value_6h(self):
        value = extract_value(self.driver, '/html/body/div/div[2]/div/div[3]/div[2]/table/tbody/tr[20]/td[7]/span[1]/text()[2]')
        return value

    def get_lower_value_1d(self):
        value = extract_value(self.driver, '/html/body/div/div[2]/div/div[3]/div[2]/table/tbody/tr[20]/td[8]/span[1]/text()[2]')
        return value