from selene.support.shared import browser
import os


class Path:

    def __init__(self, selector):
        self.selector = selector

    def attach_file(self, file):
        currentDir = os.path.dirname(os.path.abspath(__file__))
        res_dir = os.path.join(currentDir, 'resourses')
        test_file = os.path.join(res_dir, file)
        browser.element(self.selector).send_keys(test_file)
