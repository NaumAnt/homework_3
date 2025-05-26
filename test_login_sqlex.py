from selene import browser, be, have, by


def test_login_sqlex(setup_browser):
    browser.open('https://sql-ex.ru/')
    browser.element('[name="login"]').should(be.blank).type('Anton111111')
    browser.element('[name="psw"]').should(be.blank).click().type('123321Anton')
    browser.element('[name="subm1"]').click()


def test_not_find(setup_browser):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('fksdfbksdbksbsdkfbsdkfkq2fqwf').press_enter()
    browser.element('[class="card-section"]').should(have.text('По запросу fksdfbksdbksbsdkfbsdkfkq2fqwf ничего не найдено.'))
