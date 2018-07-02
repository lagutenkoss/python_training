
def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="Group name", header="Group header", footer="Group footer"))
    app.session.logout()