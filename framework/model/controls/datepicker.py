from selene import have
from selene.support.shared import browser


class DataPicker:

    def __init__(self, selector):
        self.selector = selector

    def select_date(self, value):
        browser.element(self.selector).all('option').element_by(have.exact_text(value)).click()
