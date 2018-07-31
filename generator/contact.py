from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], 'n:f:', ['number of contacts', 'file'])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = 'data/contacts.json'

for o, a in opts:
    if o == '-n':
        n = int(a)
    elif o == '-f':
        f = a


def random_string(prefix, maxlen):
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
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', f)

with open(file, 'w') as out:
    jsonpickle.set_encoder_options('json', indent=2)
    out.write(jsonpickle.encode(testdata))