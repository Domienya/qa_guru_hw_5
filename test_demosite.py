from selene import browser, have

import os
os.environ['WDM_SSL_VERIFY'] = '0'

def test_student_registration_form():

    browser.open('/automation-practice-form')
    browser.execute_script('document.querySelector("#fixedban")?.remove()')
    browser.execute_script('document.querySelector("footer")?.remove()')
    browser.element('#firstName').type('Danya')
    browser.element('#lastName').type('Frolov')
    browser.element('#userEmail').type('danya_f@example.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('1234567890')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').element('[value="2"]').click()
    browser.element('.react-datepicker__year-select').element('[value="1996"]').click()
    browser.element('.react-datepicker__day--007:not(.react-datepicker__day--outside-month)').click()
    browser.element('#subjectsInput').type('arts').press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('img.png'))
    browser.element('#currentAddress').type('Moscow')
    browser.element('#state').click()
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#city').click()
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element('#submit').press_enter()

    browser.element('.modal-content').should(have.text('Danya Frolov'))
    browser.element('.modal-content').should(have.text('danya_f@example.com'))
    browser.element('.modal-content').should(have.text('Male'))
    browser.element('.modal-content').should(have.text('1234567890'))
    browser.element('.modal-content').should(have.text('07 March,1996'))
    browser.element('.modal-content').should(have.text('Arts'))
    browser.element('.modal-content').should(have.text('Reading'))
    browser.element('.modal-content').should(have.text('img.png'))
    browser.element('.modal-content').should(have.text('Moscow'))
    browser.element('.modal-content').should(have.text('NCR Delhi'))
