from model.group import Group


def test_edit_first_group(app):
    app.group.edit_first_group(Group(name="edit group name", header="edit group header", footer="edit group footer"))
