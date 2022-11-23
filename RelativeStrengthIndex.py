from WebDriver import WebDriver as wd

def extract_data(driver, xpath):
    value = float(driver.find_element('xpath', xpath).get_attribute('innerHTML'))
    return value

class RelativeStrengthIndex(wd):
    
    # Receive RSI data in different timeframes

    def get_rsi_value_5m(self):
        value = extract_data(self.driver, '/html/body/div/div[2]/div/div[3]/div[2]/table/tbody/tr[16]/td[2]/span[1]')
        return value

    def get_rsi_value_15m(self):
        value = extract_data(self.driver, '/html/body/div/div[2]/div/div[3]/div[2]/table/tbody/tr[16]/td[3]/span[1]')
        return value

    def get_rsi_value_1h(self):
        value = extract_data(self.driver, '/html/body/div/div[2]/div/div[3]/div[2]/table/tbody/tr[16]/td[4]/span[1]')
        return value

    def get_rsi_value_2h(self):
        value = extract_data(self.driver, '/html/body/div/div[2]/div/div[3]/div[2]/table/tbody/tr[16]/td[5]/span[1]')
        return value

    def get_rsi_value_4h(self):
        value = extract_data(self.driver, '/html/body/div/div[2]/div/div[3]/div[2]/table/tbody/tr[16]/td[6]/span[1]')
        return value

    def get_rsi_value_6h(self):
        value = extract_data(self.driver, '/html/body/div/div[2]/div/div[3]/div[2]/table/tbody/tr[16]/td[7]/span[1]')
        return value

    def get_rsi_value_1d(self):
        value = extract_data(self.driver, '/html/body/div/div[2]/div/div[3]/div[2]/table/tbody/tr[16]/td[8]/span[1]')
        return value