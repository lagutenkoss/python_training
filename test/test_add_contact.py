# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")

    app.contact.create(Contact(first_name="First name", middle_name="Middle name", last_name="Last name", title="Title", company="Company", adress="adress", telephone="Telephone",
                                     mobile="Mobile", work="Work", fax="Fax", e_mail="E-mail", mailtwo="E-mail2", mailthree="E-mail3", homepage="Homepage", adress2="adress2",
                                     homeadress="Homeadress", notestwo="notes2", ayear="1995", byear="1995"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_empty(Contact(first_name="", middle_name="", last_name="", title="", company="", adress="",
                                     telephone="",
                                     mobile="", work="", fax="", e_mail="", mailtwo="", mailthree="", homepage="",
                                     adress2="",
                                     homeadress="", notestwo="", ayear="", byear=""))
    app.session.logout()




