from selene import browser, be, have

def test_google_search():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('sqlex').press_enter()
    browser.element('html').should(have.text('Об этой странице'))