from model.contact import Contact
from random import randrange


def test_edit_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="First name", middle_name="Middle name", last_name="Last name", title="Title", company="Company", adress="adress", telephone="Telephone",
                                   mobile="Mobile", workphone="Work", fax="Fax", e_mail="E-mail", mailtwo="E-mail2", mailthree="E-mail3", homepage="Homepage", adress2="adress2",
                                   homeadress="Homeadress", notestwo="notes2", ayear="1995", byear="1995"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(first_name="edit first name", middle_name="edit middle name", last_name="edit last name", title="edit title", company="edit company", adress="edit adress", telephone="edit telephone",
                      mobile="edit mobile", workphone="edit work", fax="edit fax", e_mail="edit e-mail", mailtwo="edit e-mail2", mailthree="edit e-mail3", homepage="edit homepage", adress2="edit adress2",
                      homeadress="edit home adress", notestwo="edit notes2", ayear="2000", byear="2000")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


