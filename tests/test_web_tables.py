from selene.support.conditions import have, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss


class TestFillWebTables:

    def test_web_tables(self):

        browser.open('/webtables')
        s('.main-header').should(have.exact_text('Web Tables'))

        ss('.action-buttons').should(have.size(3))
        s('#addNewRecordButton').click()
        s('.modal-content').should(be.visible)
        s("#firstName").type('Myname')
        s('#lastName').type('Mylastname')
        s('#userEmail').type('mylastname@google.com')
        s('#age').type('11')
        s('#salary').type('6000')
        s('#department').type('Mydepartment')
        s('#submit').click()
        ss('.action-buttons').should(have.size(4))
        s('#edit-record-2').click()
        s('.modal-content').should(be.visible)
        s("#firstName").clear().type('Newname')
        s('#lastName').clear().type('Newlastname')
        s('#userEmail').clear().type('new@google.com')
        s('#age').clear().type('15')
        s('#salary').clear().type('7000')
        s('#department').clear().type('Newdepartment')
        s('#submit').click()
        ss('.action-buttons').should(have.size(4))

        # assertions
        ss(".rt-tr-group").element(1).ss('.rt-td').element(0).should(have.exact_text('Newname'))
        ss(".rt-tr-group").element(1).ss('.rt-td').element(1).should(have.exact_text('Newlastname'))
        ss(".rt-tr-group").element(1).ss('.rt-td').element(2).should(have.exact_text('15'))
        ss(".rt-tr-group").element(1).ss('.rt-td').element(3).should(have.exact_text('new@google.com'))
        ss(".rt-tr-group").element(1).ss('.rt-td').element(4).should(have.exact_text('7000'))
        ss(".rt-tr-group").element(1).ss('.rt-td').element(5).should(have.exact_text('Newdepartment'))

        s('#delete-record-3').click()
        ss('.action-buttons').should(have.size(3))
