


def test_valid_login(home_page):
    login_page = home_page.click_form_authentication()
    login_page.enter_username("tomsmith")
    login_page.enter_password("SuperSecretPassword!")
    secure_area = login_page.click_login()

    alert_text = secure_area.get_alert_text()
    assert 'You logged into a secure area!' in alert_text
