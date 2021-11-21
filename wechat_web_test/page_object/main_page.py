"""
首页页面
"""
from wechat_web_test.page_object.add_member_page import AddMemberPage
from wechat_web_test.page_object.contact_page import ContactPage


class MainPage:
    # 问题：如果一条用例有多个页面交互，是否要做十几次页面的实例化操作？
    # 解决方案：一旦涉及到页面跳转的方法，可以直接return
    # 要跳转页面的实例对象， 形成链式调用， 描述清楚了页面和页面的跳转逻辑
    def goto_contact(self):
        """
        跳转通讯录页面
        :return:
        """
        return ContactPage()

    def goto_add_member(self):
        """
        跳转到添加成员页面
        :return:
        """
        return AddMemberPage()

