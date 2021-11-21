"""
添加成员页面
"""
from wechat_web_test.page_object.contact_page import ContactPage


class AddMemberPage:
    def goto_contact(self):
        """
        跳转通讯录页面
        :return:
        """
        return ContactPage()

    def add_member(self, mem_name):
        """添加成员操作
        """
        return ContactPage()
