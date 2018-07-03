from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="modify group name", header="modify group header", footer="modify group footer"))
    app.session.logout()