from selene.support.conditions import have
from selene.support.shared.jquery_style import s, ss


class TableChecking:

    @staticmethod
    def check_results(self, table_locator, *text):
        ss(f'.{table_locator}').should(have.texts(text))
