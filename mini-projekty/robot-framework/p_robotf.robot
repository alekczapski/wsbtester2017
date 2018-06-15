*** Settings ***
Library    Selenium2Library


*** Variables ***

${BTN LOGIN}    //button[@data-test="navigation-menu-signin"]
${BTN REG}    //*[@id="login-modal"]/form/div/p/button
${FIELD NAME}    //input[@data-test="registrationmodal-first-name-input"]
${FIELD SURNAME}    //input[@data-test="registrationmodal-last-name-input"]
${FIELD GENDER}    //label[@for="register-gender-male"]
${FIELD TELNUM}    //input[@data-test="booking-register-phone"]
${FIELD EMAIL}    //input[@data-test="booking-register-email"]
${FIELD PASS}    //input[@data-test="booking-register-password"]
${FIELD COUNTRY}    //input[@data-test="booking-register-country"]
${CHECKBOX PRIVACY POLICY}    //*[@id="registration-privacy-policy-checkbox"]

*** Test Cases ***

Test rejestracji nowego uzytkownika
    [Documentation]    Rejestracja nowego uzytkownika uzywajac niepoprawnego adresu e-mail
    Uruchom przegladarke Firefox i wejdz na 'https://wizzair.com/pl-pl#/'
    Kliknij 'ZALOGUJ SIE'
    Kliknij 'REJESTRACJA'
    Wpisz imie - 'Al'
    Wpisz nazwisko - 'Czz'
    Wybierz plec - 'mezczyzna'
    Wprowadz nr telefonu - '49551234567'
    Wprowadz niepoprawny e-mail - 'aaaca_gmail.pl'
    Wprowadz haslo - 'qwerty1'
    Wybierz obywatelstwo - 'Polska'
    Zaznacz checkbox - 'Akceptuje Informacje o polityce prywatnosci'
    Strona zawiera tekst - 'Nieprawidłowy adres e-mail'
    Zamknij przegladarke


*** Keywords ***

Uruchom przegladarke ${BROWSER} i wejdz na '${URL}'
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window


Kliknij 'ZALOGUJ SIE'
    Click Button    ${BTN LOGIN}


Kliknij 'REJESTRACJA'
    Click Button    ${BTN REG}


Wpisz imie - '${NAME}'
    Input Text    ${FIELD NAME}    ${NAME}


Wpisz nazwisko - '${SURNAME}'
    Input Text    ${FIELD SURNAME}    ${SURNAME}


Wybierz plec - 'mezczyzna'
    Click Element    ${FIELD GENDER}


Wprowadz nr telefonu - '${TELNUM}'
    Input Text    ${FIELD TELNUM}    ${TELNUM}


Wprowadz niepoprawny e-mail - '${EMAIL}'
    Input Text    ${FIELD EMAIL}    ${EMAIL}


Wprowadz haslo - '${PASS}'
    Input Text    ${FIELD PASS}    ${PASS}


Wybierz obywatelstwo - '${COUNTRY}'
    Input Text    ${FIELD COUNTRY}    ${COUNTRY}


Zaznacz checkbox - 'Akceptuje Informacje o polityce prywatnosci'
    Select Checkbox    ${CHECKBOX PRIVACY POLICY}


Strona zawiera tekst - '${TEXT}'
    Page Should Contain    ${TEXT}
    Capture Page Screenshot


Zamknij przegladarke
    Close Browser

