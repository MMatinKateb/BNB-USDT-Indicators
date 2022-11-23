from WebDriver import WebDriver as wd

def validate_upward(driver, xpath):
    status = driver.find_element('xpath', xpath).get_attribute('innerHTML')
    if status == '⋀':
        return True
    return False

def validate_downward(driver, xpath):
    status = driver.find_element('xpath', xpath).get_attribute('innerHTML')
    if status == '⋁':
        return True
    return False

class MovingAverage(wd):
    
    # Upward Validation ------------------------------------------------------------------------------------------------

    def mvg_is_upward_5m(self):
        status = validate_upward(self.driver, '/html/body/div/div[2]/div/div[3]/div[2]/table/tbody/tr[2]/td[2]/span[2]')
        return status

    def mvg_is_upward_15m(self):
        status = validate_upward(self.driver, '/html/body/div/div[2]/div/div[3]/div[2]/table/tbody/tr[2]/td[3]/span[2]')
        return status

    def mvg_is_upward_1h(self):
        status = validate_upward(self.driver, '/html/body/div/div[2]/div/div[3]/div[2]/table/tbody/tr[2]/td[4]/span[2]')
        return status

    def mvg_is_upward_2h(self):
        status = validate_upward(self.driver, '/html/body/div/div[2]/div/div[3]/div[2]/table/tbody/tr[2]/td[5]/span[2]')
        return status

    def mvg_is_upward_4h(self):
        status = validate_upward(self.driver, '/html/body/div/div[2]/div/div[3]/div[2]/table/tbody/tr[2]/td[6]/span[2]')
        return status

    def mvg_is_upward_6h(self):
        status = validate_upward(self.driver, '/html/body/div/div[2]/div/div[3]/div[2]/table/tbody/tr[2]/td[7]/span[2]')
        return status
    
    def mvg_is_upward_1d(self):
        status = validate_upward(self.driver, '/html/body/div/div[2]/div/div[3]/div[2]/table/tbody/tr[2]/td[8]/span[2]')
        return status

    # Downward Validation ----------------------------------------------------------------------------------------------

    def mvg_is_downward_5m(self):
        status = validate_downward(self.driver, '/html/body/div/div[2]/div/div[3]/div[2]/table/tbody/tr[2]/td[2]/span[2]')
        return status

    def mvg_is_downward_15m(self):
        status = validate_downward(self.driver, '/html/body/div/div[2]/div/div[3]/div[2]/table/tbody/tr[2]/td[3]/span[2]')
        return status

    def mvg_is_downward_1h(self):
        status = validate_downward(self.driver, '/html/body/div/div[2]/div/div[3]/div[2]/table/tbody/tr[2]/td[4]/span[2]')
        return status

    def mvg_is_downward_2h(self):
        status = validate_downward(self.driver, '/html/body/div/div[2]/div/div[3]/div[2]/table/tbody/tr[2]/td[5]/span[2]')
        return status

    def mvg_is_downward_4h(self):
        status = validate_downward(self.driver, '/html/body/div/div[2]/div/div[3]/div[2]/table/tbody/tr[2]/td[6]/span[2]')
        return status

    def mvg_is_downward_6h(self):
        status = validate_downward(self.driver, '/html/body/div/div[2]/div/div[3]/div[2]/table/tbody/tr[2]/td[7]/span[2]')
        return status
    
    def mvg_is_downward_1d(self):
        status = validate_downward(self.driver, '/html/body/div/div[2]/div/div[3]/div[2]/table/tbody/tr[2]/td[8]/span[2]')
        return status