from selene.support.shared import browser
from selene import command


class Scroll:

    def __init__(self, selector):
        self.selector = selector

    def scroll_to(self):
        browser.element(self.selector).perform(command.js.scroll_into_view)