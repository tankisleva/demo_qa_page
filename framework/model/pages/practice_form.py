from selene import have
from selene.support.shared import browser
from framework.model.controls import dropdown, datepicker, radiobutton, checkbox
from framework.model.data.user import User
from framework.utils import path_to_file
from framework.utils.scroll import scroll_to


class PracticePage:

    def fill_data(self, user: User):
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('#userEmail').type(user.email)
        radiobutton.gender('[name=gender]', user.gender)
        browser.element('#userNumber').type(user.phone)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click()
        datepicker.selectDate('.react-datepicker__month-select', user.birthday_month)
        browser.element('.react-datepicker__year-select').click()
        datepicker.selectDate('.react-datepicker__year-select', user.birthday_year)
        browser.element(f'.react-datepicker__day--0{user.birthday_day}').click()
        browser.element('#subjectsInput').type(user.subject).press_enter()
        scroll_to('#currentAddress')
        browser.element('#currentAddress').type(user.address)
        checkbox.checkHobby('[for^=hobbies-checkbox]', user.hobby)
        path_to_file.create_path('#uploadPicture', user.image)
        dropdown.select('#state', by_text=user.state)
        dropdown.select('#city', by_text=user.city)
        return self

    def open(self):
        browser.open('/automation-practice-form')
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
