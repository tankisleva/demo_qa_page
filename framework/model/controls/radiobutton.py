from selene import have
from selene.support.shared import browser


class RadioButton:

    def __init__(self, selector):
        self.selector = selector

    def select_gender(self, value):
        browser.all(self.selector).element_by(have.value(value)).element('..').click()