from model.contact import Contact


def test_add_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="First name", middle_name="Middle name", last_name="Last name", title="Title", company="Company", adress="adress", telephone="Telephone",
                                     mobile="Mobile", work="Work", fax="Fax", e_mail="E-mail", mailtwo="E-mail2", mailthree="E-mail3", homepage="Homepage", adress2="adress2",
                                     homeadress="Homeadress", notestwo="notes2", ayear="1995", byear="1995"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="edit first name", middle_name="edit middle name", last_name="edit last name", title="edit title", company="edit company", adress="edit adress", telephone="edit telephone",
                                     mobile="edit mobile", work="edit work", fax="edit fax", e_mail="edit e-mail", mailtwo="edit e-mail2", mailthree="edit e-mail3", homepage="edit homepage", adress2="edit adress2",
                                     homeadress="edit home adress", notestwo="edit notes2", ayear="2000", byear="2000")
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


