from qa_guru_python_8_12.data import users
from qa_guru_python_8_12.pages.registration_page import RegistrationPage


def test_form_demoqa():
    registration_page = RegistrationPage()
    student = users.student

    registration_page.open()
    registration_page.register(student)
    registration_page.should_have_registered(student)
