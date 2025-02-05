from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers import retrieve_phone_code

# Defining the page class, locators and method in the class
class UrbanRoutesPage:
    # Addresses
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    # Tariff and call button
    SUPPORTIVE_PLAN_CARD = (By.XPATH, '//div[contains(text(), "Supportive")]')
    ACTIVE_PLAN_CARD = (By.XPATH, '//div[@class="tcard active"]//div[@class="tcard-title"]')
    CALL_TAXI_BUTTON = (By.XPATH, '//button[contains(text(), "Call a taxi")]')
     # Phone number
    PHONE_NUMBER_LOCATOR = (By.CLASS_NAME, 'np-text')
    PHONE_NUMBER_INPUT = (By.ID, 'phone')
    SMS_CODE_INPUT = (By.ID, 'code')


     # Credit card
    CASH_LOCATOR = (By.CLASS_NAME, 'pp-value-text')
    PAYMENT_CARD_OPTION_LOCATOR = (By.CLASS_NAME, 'pp-plus')
    CARD_INPUT = (By.ID, 'number')
    CODE_INPUT = (By.XPATH, '//input[@class="card-input" and @id="code"]')
    Link_BUTTON = (By.XPATH, '//button[contains(text(), "Link")]')
    CLOSE_BUTTON = (By.CSS_SELECTOR, '.payment-picker.open .close-button.section-close')
     # Message for the driver
    COMMENT_FOR_DRIVER =(By.ID, 'comment')
      # Blanket & handkerchiefs order
    BLANKET_HANDKERCHIEF_TOGGLE_LOCATOR = (By.CLASS_NAME, 'switch')
    BLANKET_HANDKERCHIEF_CHECKBOX = (By.CLASS_NAME, 'switch-input')
      # Ice cream
    ICE_CREAM_QUANTITY = (By.CLASS_NAME, 'counter-value')
    ICE_CREAM_PLUS = (By.CLASS_NAME, 'counter-plus')
      # Ordering taxi
    ORDER_TAXI_BUTTON = (By.CLASS_NAME, 'smart-button-main')
    CAR_MODAL_WINDOW = (By.CLASS_NAME, 'order-header-title')


    def __init__(self, driver):
        self.driver = driver # Initialize class attributes


    def set_from(self, from_address):
        from_field = self.driver.find_element(*self.FROM_LOCATOR)
        from_field.send_keys(from_address)

    def set_to(self, to_address):
        to_field = self.driver.find_element(*self.TO_LOCATOR)
        to_field.send_keys(to_address)


    def get_from(self):
        return self.driver.find_element(*self.FROM_LOCATOR).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.TO_LOCATOR).get_property('value')

    def click_call_taxi_button(self):
       WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(self.CALL_TAXI_BUTTON))
       call_taxi_button = self.driver.find_element(*self.CALL_TAXI_BUTTON)
       call_taxi_button.click()

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)
        self.click_call_taxi_button()

    def select_supportive_plan(self):
        select_supportive_plan_button = self.driver.find_element(*self.SUPPORTIVE_PLAN_CARD)
        select_supportive_plan_button.click()

    def get_current_supportive_plan(self):
        return self.driver.find_element(*self.ACTIVE_PLAN_CARD).text

    def click_phone_number(self):
        phone_number = self.driver.find_element(*self.PHONE_NUMBER_LOCATOR)
        phone_number.click()

    def enter_phone_number(self, phone_number):
        phone_number_field = self.driver.find_element(*self.PHONE_NUMBER_INPUT)
        phone_number_field.send_keys(phone_number)
        phone_number_field.send_keys(Keys.RETURN)   # Submit the phone number

    def enter_sms_code(self):
        sms_code_field = self.driver.find_element(*self.SMS_CODE_INPUT)
        sms_code_field.send_keys(retrieve_phone_code(self.driver))
        sms_code_field.send_keys(Keys.RETURN)  # Submit the SMS code

    def get_phone_number(self):
        return self.driver.find_element(*self.PHONE_NUMBER_LOCATOR).get_property('textContent')


    def click_cash_option(self):
        cash_option = self.driver.find_element(*self.CASH_LOCATOR)
        cash_option.click()

    def click_payment_card_option(self):
        payment_card_option = self.driver.find_element(*self.PAYMENT_CARD_OPTION_LOCATOR)
        payment_card_option.click()

    def enter_card_input(self, card_number):
        card_input = self.driver.find_element(*self.CARD_INPUT)
        card_input.send_keys(card_number)
           #Submit the card number

    def enter_code_input(self, code_number):
        code_input = self.driver.find_element(*self.CODE_INPUT)
        code_input.send_keys(code_number)
        code_input.send_keys(Keys.TAB)  #Submit the code number

    def click_link_button(self):
        link_button = self.driver.find_element(*self.Link_BUTTON)
        link_button.click()
        close_button = self.driver.find_element(*self.CLOSE_BUTTON)
        close_button.click()
    def get_adding_credit_card(self):
        return self.driver.find_element(*self.CASH_LOCATOR).get_property('textContent')

    def enter_driver_comment(self, comment):
        self.driver.find_element(*self.COMMENT_FOR_DRIVER).send_keys(comment)
        return self.driver.find_element(*self.COMMENT_FOR_DRIVER).get_attribute('value')

    def click_blanket_and_handkerchiefs_toggle(self):
        self.driver.find_element(*self.BLANKET_HANDKERCHIEF_TOGGLE_LOCATOR).click()

    def get_blanket_and_handkerchiefs_checkbox(self):
        return self.driver.find_element(*self.BLANKET_HANDKERCHIEF_CHECKBOX).get_property('checked')

    def order_ice_creams(self, quantity):
        for i in range(quantity):
            self.driver.find_element(*self.ICE_CREAM_PLUS).click()

    def get_ice_cream(self):
        return self.driver.find_element(*self.ICE_CREAM_QUANTITY).get_property('textContent')

    def click_order_taxi_button(self):
        self.driver.find_element(*self.ORDER_TAXI_BUTTON).click()

    def get_car_modal(self):
        return self.driver.find_element(*self.CAR_MODAL_WINDOW).get_property('textContent')














