# -*- coding: utf-8 -*-

from model.contact import Contact


def test_modify_contact_first_name(app):
    app.contact.modify_first_contact(Contact(first_name="New First name"))


def test_modify_contact_middle_name(app):
    app.contact.modify_first_contact(Contact(middle_name="New Middle name"))

