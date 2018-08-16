import re
from random import randrange
from model.contact import Contact


def test_phones_on_home_page(app):
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert clear(contact_from_home_page.last_name) == clear(contact_from_edit_page.last_name)
    assert clear(contact_from_home_page.first_name) == clear(contact_from_edit_page.first_name)
    assert clear(contact_from_home_page.adress) == clear(contact_from_edit_page.adress)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def test_phones_on_home_page_with_db(app, db):
    contact_from_home_page = app.contact.get_contact_list()
    list_home_page = sorted(contact_from_home_page, key=Contact.id_or_max)
    contacts_db = db.get_contact_list()
    list_db = sorted(contacts_db, key=Contact.id_or_max)
    assert len(list_db) == len(list_home_page)
    for i in range(0, len(contacts_db)):
        assert list_db[i].id == list_home_page[i].id
        assert list_db[i].last_name == list_home_page[i].last_name
        assert list_db[i].first_name == list_home_page[i].first_name
        assert list_db[i].adress == list_home_page[i].adress
        assert merge_phones_like_on_home_page(list_db[i]) == list_home_page[i].all_phones_from_home_page
        assert merge_emails_like_on_home_page(list_db[i]) == list_home_page[i].all_emails_from_home_page


def test_phones_on_contact_view_page(app):
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_from_view_page = app.contact.get_contact_from_view_page(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_view_page.telephone == contact_from_edit_page.telephone
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.homeadress == contact_from_edit_page.homeadress


def clear(s):
    return re.sub('[() /-]', '',  s)


def merge_phones_like_on_home_page(contact_phones):
    return '\n'.join(filter(lambda x: x !='',
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact_phones.telephone, contact_phones.mobile, contact_phones.workphone, contact_phones.homeadress]))))


def merge_emails_like_on_home_page(contact_emails):
    return '\n'.join(filter(lambda x: x != '',
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact_emails.e_mail, contact_emails.mailtwo, contact_emails.mailthree]))))


