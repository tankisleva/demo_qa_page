from selene import have, command
from selene.support.shared import browser
from framework.model.controls import dropdown, datepicker, radiobutton
from framework.model.controls.datepicker import DataPicker
from framework.model.controls.dropdown import DropDown
from framework.model.controls.radiobutton import RadioButton
from framework.model.controls.checkbox import Checkbox
from framework.model.data.user import User
from framework.utils import path_to_file
from framework.utils.path_to_file import Path
from framework.utils.scroll import Scroll


class PracticePage:

    def fill_data(self, user: User):
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('#userEmail').type(user.email)
        radio = RadioButton('[name=gender]')
        radio.select_gender(user.gender)
        browser.element('#userNumber').type(user.phone)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click()
        month = DataPicker('.react-datepicker__month-select')
        month.select_date(user.birthday_month)
        browser.element('.react-datepicker__year-select').click()
        year = DataPicker('.react-datepicker__year-select')
        year.select_date(user.birthday_year)
        browser.element(f'.react-datepicker__day--0{user.birthday_day}').click()
        browser.element('#subjectsInput').type(user.subject).press_enter()
        scroll = Scroll('#currentAddress')
        scroll.scroll_to()
        browser.element('#currentAddress').type(user.address)
        checkBox = Checkbox('[for^=hobbies-checkbox]')
        checkBox.check_hobby(user.hobby)
        path = Path('#uploadPicture')
        path.attach_file(user.image)
        state = DropDown('#state')
        city = DropDown('#city')
        state.select(by_text=user.state)
        city.select(by_text=user.city)
        return self

    def open(self):
        browser.open("https://demoqa.com/automation-practice-form")
        return self

    def remove_ad(self):
        ads = browser.all('[id^=google_ads_][id$=container__]')
        if ads.should(have.size_less_than_or_equal(3)):
            ads.perform(command.js.remove)
        return self

    def submit(self):
        browser.element('#submit').press_enter()
        return self


    def assert_fields(self, user: User):
        browser.element('.table').all('td').even.should(have.texts(
            f'{user.first_name} {user.last_name}',
            user.email,
            user.gender,
            user.phone,
            f'{user.birthday_day} {user.birthday_month},{user.birthday_year}',
            user.subject,
            user.hobby,
            user.image,
            user.address,
            f'{user.state} {user.city}'
        ))
        return self
