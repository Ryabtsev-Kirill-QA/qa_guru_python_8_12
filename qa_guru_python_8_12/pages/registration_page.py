from selene import browser, have, be, by
from qa_guru_python_8_12 import picture


class RegistrationPage:

    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')

    def open(self):
        browser.open('/automation-practice-form')
        browser.element('#fixedban').execute_script('element.remove()')
        browser.element('footer').execute_script('element.remove()')
        browser.should(have.title('DEMOQA'))
        browser.element('.main-header').should(have.text('Practice Form'))

    def fill_first_name(self, value):
        self.first_name.type(value)
        return self

    def fill_last_name(self, value):
        self.last_name.type(value)
        return self

    def fill_email(self, value):
        self.email.type(value)
        return self

    def choose_gender(self, checkbox_position):
        browser.all('.custom-control-input').should(be.disabled)
        browser.element(f'#gender-radio-{checkbox_position}').double_click()
        browser.element(f'#gender-radio-{checkbox_position}').should(be.enabled)
        return self

    def fill_mobile_number(self, value):
        browser.element('#userNumber').type(value)
        return self

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click().element(by.text(month)).click()
        browser.element('.react-datepicker__year-select').click().element(by.text(year)).click()
        browser.element(f'.react-datepicker__day--0{day}').click()
        return self

    def fill_subjects(self, value):
        browser.element('#subjectsInput').should(be.blank).type(value).press_enter()
        return self

    def choose_hobbies(self, checkbox_position):
        browser.element(f'[for="hobbies-checkbox-{checkbox_position}"]').click()
        return self

    def upload_picture(self, file):
        browser.element('#uploadPicture').set_value(picture.path(file))
        return self

    def fill_current_address(self, value):
        browser.element('#currentAddress').type(value)
        return self

    def select_state(self, value):
        browser.element('#react-select-3-input').type(value).press_enter()
        return self

    def select_city(self, value):
        browser.element('#react-select-4-input').type('Delhi').press_enter()
        return self

    def submit_form(self):
        browser.element('#submit').press_enter()
        return self

    def should_have_registered_user_with(self, full_name, email, gender, mobile_number, day_of_birth, subjects, hobbies,
                                         picture, current_address,
                                         state_and_city):
        browser.element('.modal-header').should(have.text('Thanks for submitting the form'))
        browser.element('.table-responsive').all('tr td:nth-child(2)').should(have.texts(
            full_name,
            email,
            gender,
            mobile_number,
            day_of_birth,
            subjects,
            hobbies,
            picture,
            current_address,
            state_and_city))
        browser.element('#closeLargeModal').press_enter()