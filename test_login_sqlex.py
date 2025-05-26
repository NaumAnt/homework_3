from selene import browser, be, have, by


def test_login_sqlex(setup_browser):
    browser.open('https://sql-ex.ru/')
    browser.element('[name="login"]').should(be.blank).type('Anton111111')
    browser.element('[name="psw"]').should(be.blank).click().type('123321Anton')
    browser.element('[name="subm1"]').click()


def test_not_find(setup_browser):
    browser.open('https://sql-ex.ru/')
    browser.element('[name="login"]').should(be.blank).type('Anton111111')
    browser.element('[name="psw"]').should(be.blank).click().type('123321Anton')
    browser.element('[name="subm1"]').click()
    browser.element('html').should(have.text('Anton22222222'))
