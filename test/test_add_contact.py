# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + ' '*10
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(first_name="", middle_name="", last_name="", title="", company="", adress="", adress2="",
    telephone="", mobile="", workphone="", fax="", e_mail="", mailtwo="", mailthree="", homepage="",
    homeadress="", notestwo="", ayear="", byear="")] + [
    Contact(first_name=random_string('first_name', 10), middle_name=random_string('middle_name', 10),
    last_name=random_string('last_name', 10), title=random_string('title', 15), company=random_string('company', 15),
    adress=random_string('adress', 25),telephone=random_string('telephone', 11), mobile=random_string('mobile', 11),
    workphone=random_string('workphone', 11), fax=random_string('fax', 11), e_mail=random_string('e_mail', 18),
    mailtwo=random_string('mailtwo', 18), mailthree=random_string('mailthree', 18),
    homepage=random_string('homepage', 15), adress2=random_string('adress2', 25),
    homeadress=random_string('homeadress', 25), notestwo=random_string('notestwo', 20),
    ayear=random_string('ayear', 4), byear=random_string('byear', 4))
    for i in range(5)
]


@pytest.mark.parametrize('contact', testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_empty(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)





