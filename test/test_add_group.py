# -*- coding: utf-8 -*-
from model.group import Group
# import pytest
# from data.add_group import testdata
# from data.groups import constant as testdata

# полный перебор
# testdata = [
#    Group(name=name, header=header, footer=footer)
#    for name in ['', random_string('name', 10)]
#    for header in ['', random_string('header', 20)]
#    for footer in ['', random_string('footer', 20)]
#]


def test_add_group_with_db(app, db, json_groups, check_ui):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), Group.id_or_max)


# @pytest.mark.parametrize('group', testdata, ids=[repr(x) for x in testdata])
'''def test_add_group(app, json_groups):
    group = json_groups
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)'''




