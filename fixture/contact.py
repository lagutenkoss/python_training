from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook.php") and len(wd.find_elements_by_link_text("Send e-Mail")) > 0):
            wd.find_element_by_link_text("home").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page_to_add()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[3]").click()
        wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").click()
        wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[3]").click()
        wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[2]").click()
        self.contact_creation()
        self.return_to_home_page()
        self.contact_cache = None

    def contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def open_contact_page_to_add(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
            wd.find_element_by_link_text("add new").click()

    def create_empty(self, contact):
        wd = self.app.wd
        self.open_contact_page_to_add()
        # fill_contact_form
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[2]").click()
        wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[2]").click()
        # contact_creation
        self.contact_creation()
        self.return_to_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("middlename", contact.middle_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.adress)
        self.change_field_value("home", contact.telephone)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.e_mail)
        self.change_field_value("email2", contact.mailtwo)
        self.change_field_value("email3", contact.mailthree)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("byear", contact.byear)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.adress2)
        self.change_field_value("phone2", contact.homeadress)
        self.change_field_value("notes", contact.notestwo)

    def edit_first_contact(self):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.return_to_home()
        self.click_for_edit_contact_by_index(index)
        # edit_contact_form
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[11]").click()
        wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[7]").click()
        wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[11]").click()
        wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[7]").click()
        # update group creation
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def click_for_edit_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//div[1]/div[4]/form[2]/table/tbody/tr/td[8]/a/img")[index].click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.return_to_home()
        # select first contact
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.return_to_home()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.return_to_home()
        # modify first contact
        self.click_for_edit_contact_by_index(index)
        # fill group form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_to_home()
            self.contact_cache = []
            for line in wd.find_elements_by_name('entry'):
                cell = line.find_elements_by_css_selector('td')
                text_last_name = cell[1].text
                text_first_name = cell[2].text
                id = cell[0].find_element_by_name("selected[]").get_attribute('value')
                all_phones = cell[5].text.splitlines()
                self.contact_cache.append(Contact(first_name=text_first_name, last_name=text_last_name,  id=id,
                                                  telephone=all_phones[0], workphone=all_phones[1],
                                                  mobile=all_phones[2], fax=all_phones[3]))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.return_to_home()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[7]
        cell.find_element_by_tag_name('a').click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.return_to_home()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[6]
        cell.find_element_by_tag_name('a').click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        first_name = wd.find_element_by_name('firstname').get_attribute('value')
        last_name = wd.find_element_by_name('lastname').get_attribute('value')
        id = wd.find_element_by_name('id').get_attribute('value')
        telephone = wd.find_element_by_name('home').get_attribute('value')
        mobile = wd.find_element_by_name('work').get_attribute('value')
        workphone = wd.find_element_by_name('mobile').get_attribute('value')
        fax = wd.find_element_by_name('home').get_attribute('value')
        return Contact(first_name=first_name, last_name=last_name, id=id, telephone=telephone, mobile=mobile,
                       workphone=workphone, fax=fax)
