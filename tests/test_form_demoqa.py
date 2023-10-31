from qa_guru_python_8_12.pages.registration_page import RegistrationPage


def test_form_demoqa():
    registration_page = RegistrationPage()
    registration_page.open()

    (
        registration_page
        .fill_first_name('Test_Name')
        .fill_last_name('Test_Last_Name')
        .fill_email('test@gmail.com')
        .choose_gender('1')
        .fill_mobile_number('8800555353')
        .fill_date_of_birth('2000', 'December', '11')
        .fill_subjects('Computer Science')
        .choose_hobbies('1')
        .upload_picture('foto.jpg')
        .fill_current_address('Test_Adress, 9')
        .select_state('NCR')
        .select_city('Delhi')
        .submit_form()
    )

    registration_page.should_have_registered_user_with(
        'Test_Name Test_Last_Name',
        'test@gmail.com',
        'Male',
        '8800555353',
        '11 December,2000',
        'Computer Science',
        'Sports',
        'foto.jpg',
        'Test_Adress, 9',
        'NCR Delhi'
    )