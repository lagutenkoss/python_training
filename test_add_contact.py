# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application_contact
from application import Application_empty_contact


@pytest.fixture
def app(request):
    fixture = Application_contact()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")

    app.create_contact(Contact( first_name="First name", middle_name="Middle name", last_name="Last name", title="Title", company="Company", adress="adress", telephone="Telephone",
                            mobile="Mobile", work="Work", fax="Fax", e_mail="E-mail", mailtwo="E-mail2", mailthree="E-mail3", homepage="Homepage", adress2="adress2",
                            homeadress="Homeadress", notestwo="notes2", ayear="1995", byear="1995"))
    app.logout()


@pytest.fixture
def app(request):
    fixture = Application_empty_contact()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(first_name="", middle_name="", last_name="", title="", company="", adress="",
                                        telephone="",
                                        mobile="", work="", fax="", e_mail="", mailtwo="", mailthree="", homepage="",
                                        adress2="",
                                        homeadress="", notestwo="", ayear="", byear=""))
    app.logout()




