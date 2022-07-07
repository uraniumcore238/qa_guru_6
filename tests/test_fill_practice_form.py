from pathlib import Path
from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss
import tests
from controls.checkbox_actions import CheckboxActions
from controls.feel_value import FeelValue
from advertisement_helper import remove_advertisement
from controls.table_checking import TableChecking


class TestFillPracticeForm:

    def test_fill_practice_form(self):

        file: str = Path(tests.__file__).parent.parent.joinpath('resources/image.png')
        browser.open('/automation-practice-form')
        s('.main-header').should(have.exact_text('Practice Form'))
        s('#firstName').type('Vasya')
        s('#lastName').type('Terkin')
        s('#userEmail').type('example@gmail.com')
        FeelValue.type_data_in_input_field('subjectsContainer', 'Eng')
        FeelValue.select_date_in_selector('dateOfBirth', 'March', '1988', '15')
        CheckboxActions.choose_checkbox_by_value('Male')
        remove_advertisement.remove_advertisement()
        s('#userNumber').type('9999999999')
        CheckboxActions.choose_checkbox_by_value('1')
        CheckboxActions.choose_checkbox_by_value('2')
        CheckboxActions.choose_checkbox_by_value('3')
        s('#uploadPicture').type(file)
        s('#currentAddress').type('Current address')
        FeelValue.type_data_in_input_field('state', 'Rajasthan')
        FeelValue.choose_data_in_selector('city', 'Jaipur')
        s('#submit').click()

        # // assertions
        TableChecking.check_results(self, 'modal-header', 'Thanks for submitting the form')
        TableChecking.check_results(self, 'table td', 'Student Name', 'Vasya Terkin', 'Student Email',
                                    'example@gmail.com', 'Gender', 'Male', 'Mobile', '9999999999',
                                    'Date of Birth', '15 March,1988', 'Subjects', 'English', 'Hobbies',
                                    'Sports, Reading, Music', 'Picture', 'image.png', 'Address',
                                    'Current address', 'State and City', 'Rajasthan Jaipur')
