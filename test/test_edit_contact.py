from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")

    app.contact.edit_first_contact(Contact(first_name="edit first name", middle_name="edit middle name", last_name="edit last name", title="edit title", company="edit company", adress="edit adress", telephone="edit telephone",
                                     mobile="edit mobile", work="edit work", fax="edit fax", e_mail="edit e-mail", mailtwo="edit e-mail2", mailthree="edit e-mail3", homepage="edit homepage", adress2="edit adress2",
                                     homeadress="edit home adress", notestwo="edit notes2", ayear="2000", byear="2000"))
    app.session.logout()
