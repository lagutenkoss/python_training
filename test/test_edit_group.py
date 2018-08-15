from model.group import Group
from random import randrange
import random


'''def test_edit_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group name", header="Group header", footer="Group footer"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="edit group name", header="edit group header", footer="edit group footer")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
'''

def test_edit_some_group_with_db(db, app, check_ui):
    if (len(db.get_group_list())) == 0:
        app.group.create(Group(name="Group name", header="Group header", footer="Group footer"))
    old_groups = db.get_group_list()
    grouppa = random.choice(old_groups)
    group = Group(name="edit group name", header="edit group header", footer="edit group footer")
    app.group.edit_group_by_id(grouppa.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), Group.id_or_max)