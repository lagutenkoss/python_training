from sys import maxsize


class Contact:

    def __init__(self, first_name=None, middle_name=None, last_name=None, title=None, company=None, adress=None, telephone=None, mobile=None, workphone=None,
                 fax=None, e_mail=None, mailtwo=None, mailthree=None, homepage=None, adress2=None, homeadress=None, notestwo=None, byear=None, ayear=None, id=None):
        self.first_name=first_name
        self.middle_name=middle_name
        self.last_name=last_name
        self.title=title
        self.company=company
        self.adress=adress
        self.telephone=telephone
        self.mobile=mobile
        self.work=workphone
        self.fax=fax
        self.e_mail=e_mail
        self.mailtwo=mailtwo
        self.mailthree=mailthree
        self.homepage=homepage
        self.adress2=adress2
        self.homeadress=homeadress
        self.notestwo=notestwo
        self.byear=byear
        self.ayear=ayear
        self.id=id

    def __repr__(self):
        return '%s:%s' % (self.id, self.first_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
