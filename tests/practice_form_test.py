from framework.model import app
from framework.model.data.user import User


def test_student_registration_form():
    user = User(first_name='Oleg',
                last_name='Malyshev',
                email='oleg@test.ru',
                gender='Male',
                phone='9177121162',
                birthday_year='1985',
                birthday_month='May',
                birthday_day=11,
                subject='English',
                hobby='Sports',
                image='img.png',
                address='My best address',
                state='NCR',
                city='Delhi')

    app.practice_page.open()
    app.practice_page.remove_ad()
    app.practice_page.fill_data(user)
    app.practice_page.submit()
    app.practice_page.assert_fields(user)




