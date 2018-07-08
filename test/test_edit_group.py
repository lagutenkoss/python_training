from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group name", header="Group header", footer="Group footer"))
    app.group.edit_first_group(Group(name="edit group name", header="edit group header", footer="edit group footer"))

