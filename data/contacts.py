from model.contact import Contact
# import random
# import string


testdata = [
    Contact(first_name="first_name1", middle_name="middle_name1", last_name="last_name1", title="title1",
            company="company1", adress="adress1", adress2="adress21", telephone="telephone1",
            mobile="mobile1", workphone="workphone1", fax="fax1", e_mail="e_mail1", mailtwo="mailtwo1",
            mailthree="mailthree", homepage="homepage1", homeadress="homeadress1", notestwo="notestwo1",
            ayear="1111", byear="1111"),
    Contact(first_name="first_name2", middle_name="middle_name2", last_name="last_name2", title="title2",
            company="company2", adress="adress2", adress2="adress22", telephone="telephone2",
            mobile="mobile2", workphone="workphone2", fax="fax2", e_mail="e_mail2", mailtwo="mailtwo2",
            mailthree="mailthree", homepage="homepage2", homeadress="homeadress2", notestwo="notestwo2",
            ayear="2222", byear="2222")
]


'''def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + ' '*10
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(first_name="", middle_name="", last_name="", title="", company="", adress="", adress2="",
    telephone="", mobile="", workphone="", fax="", e_mail="", mailtwo="", mailthree="", homepage="",
    homeadress="", notestwo="", ayear="", byear="")] + [
    Contact(first_name=random_string('first_name', 10), middle_name=random_string('middle_name', 10),
    last_name=random_string('last_name', 10), title=random_string('title', 15), company=random_string('company', 15),
    adress=random_string('adress', 25),telephone=random_string('telephone', 11), mobile=random_string('mobile', 11),
    workphone=random_string('workphone', 11), fax=random_string('fax', 11), e_mail=random_string('e_mail', 18),
    mailtwo=random_string('mailtwo', 18), mailthree=random_string('mailthree', 18),
    homepage=random_string('homepage', 15), adress2=random_string('adress2', 25),
    homeadress=random_string('homeadress', 25), notestwo=random_string('notestwo', 20),
    ayear=random_string('ayear', 4), byear=random_string('byear', 4))
    for i in range(5)
]'''

