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

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.return_to_home()
        self.click_for_edit_first_contact()
        # edit_contact_form
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[11]").click()
        wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[7]").click()
        wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[11]").click()
        wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[7]").click()
        # update group creation
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def click_for_edit_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[1]/div[4]/form[2]/table/tbody/tr[2]/td[8]/a/img").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.return_to_home()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.return_to_home()
        # modify first contact
        self.click_for_edit_first_contact()
        # fill group form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

