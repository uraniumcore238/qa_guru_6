from selene.core import command
from selene.support.conditions import have
from selene.support.shared.jquery_style import ss, s


class CheckboxActions:

    @staticmethod
    def choose_checkbox_by_value(value: str):
        s(f"input[value='{value}']").element('..').click()
