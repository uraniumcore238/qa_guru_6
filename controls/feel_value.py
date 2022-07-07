from selene.core import command
from selene.support.conditions import have
from selene.support.shared.jquery_style import ss, s


class FeelValue:

    @staticmethod
    def type_data_in_input_field(id_selector: str, text: str):
        s(f'#{id_selector} input').perform(command.js.scroll_into_view).type(text).press_tab()

    @staticmethod
    def choose_data_in_selector(id_container_selector: str, text: str):
        s(f'#{id_container_selector}').perform(command.js.scroll_into_view).click()
        s("//div[contains(@class, '-menu')]").ss("//div[contains(@id, 'react-select')]")\
            .element_by(have.text(f'{text}')).click()


    @staticmethod
    def select_date_in_selector(id_container_selector: str, month: str, year: str, day: str):
        s(f'#{id_container_selector} input').perform(command.js.scroll_into_view).click()
        s(".react-datepicker__month-select").ss('option').element_by(have.text(f'{month}')).click()
        s(".react-datepicker__year-select").ss('option').element_by(have.text(f'{year}')).click()
        ss(".react-datepicker__day").element_by(have.exact_text(day)).click()
