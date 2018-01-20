import unittest
import sys
sys.path.append('../../../../')
from test_case.page_obj.form.radio_page import RadioPhonePage
import time
from test_case.running.phone.form.component_test import ComponentPhoneTest


class RadioPhoneTest(ComponentPhoneTest):
    '''手机端单选框测试'''

    menu1 = '表单'
    menu2 = '表单控件'  # 主页打开菜单时使用
    menu3 = '单选框'

    def test_designpattern_case(self):
        '''单选框设计模式'''
        name = '单选框_选项脚本设计模式'
        comp = RadioPhonePage (self.driver,name)
        target_element = comp.get_components()
        comp.scroll_to_target_element(target_element[0])
        for i in target_element:
            comp.wait_elem_disappear('.weui_mask_transparent')
            i.click()
            #time.sleep(0.5)
            val2 = i.is_selected()
            self.assertTrue(val2, msg='单选框_选项脚本设计模式检验不通过')

    def test_type_case(self):
        '''类型'''
        name = '单选框_名称'
        comp = RadioPhonePage(self.driver, name)
        bool = comp.elements_attr_test('type','radio')
        self.assertTrue(bool,msg=name + '检验不通过')

    def test_readonly_case(self):
        '''显示只读和条件只读'''
        name = '单选框_只读'
        comp = RadioPhonePage(self.driver, name)
        bool = comp.elements_attr_test ('disabled', 'true')
        self.assertTrue (bool, msg=name + '检验不通过')

    def test_refresh_calculate_case(self):
        '''刷新_重计算'''
        name = '单选框_刷新'
        name2 = '单选框_重计算'
        num = 0
        comp = RadioPhonePage (self.driver, name)
        target_element = comp.get_components()
        comp.scroll_to_target_element(target_element[0])
        for i in target_element:
            comp.wait_elem_disappear ('.weui_mask_transparent')
            i.click()
            #time.sleep(0.5)
            val2 = self.driver.find_elements_by_name(name2)[num].is_selected()
            self.assertTrue(val2, msg='单选框刷新_重计算检验不通过')
            num += 1

    def test_valuescript_case(self):
        '''单选框_值脚本'''
        name = '单选框_值脚本'
        comp = RadioPhonePage(self.driver, name)
        self.assertTrue(comp.valuescript_test(name,"2"), msg=name + '检验不通过')

    def test_desription_case(self):
        '''描述'''
        name = '单选框_描述'
        comp = RadioPhonePage(self.driver, name)
        bool = comp.is_desription_effect(name)
        self.assertTrue(bool, msg=name + '检验不通过')

    def test_not_null_case(self):
        '''非空校验'''
        name = '单选框_非空校验'
        comp = RadioPhonePage(self.driver, name)
        self.assertIn("'单选框_非空校验'必须填写", comp.notnull_test(), msg=name + '检验不通过')

    def test_hide_case(self):
        '''条件隐藏'''
        name = '单选框_隐藏条件'
        comp = RadioPhonePage(self.driver, name)
        locator = '[name="' + name + '"]'
        bool = comp.find_elems(locator)[1].is_displayed()
        self.assertFalse(bool, msg=name + '检验不通过')

    def test_show_when_hide_case(self):
        '''隐藏时显示值'''
        name = '单选框_隐藏时显示值'
        comp = RadioPhonePage(self.driver, name)
        self.assertIn("控件已隐藏", comp.get_text_by_css_selector('.flexbox'), msg=name + '检验不通过')

    def test_display_case(self):
        """条件只读"""
        name = '单选框_只读条件'
        comp = RadioPhonePage(self.driver,name)
        bool = comp.elements_attr_test ('disabled', 'true')
        self.assertTrue (bool, msg=name + '检验不通过')

    def init(self):
        '''单选按钮测试'''
#         self.test_type_case()
#         self.test_readonly_case()
        self.test_refresh_calculate_case()
#         self.test_desription_case()
#         self.test_valuescript_case()
#         self.test_designpattern_case()
#         self.test_not_null_case()
#         self.test_hide_case()
#         self.test_show_when_hide_case()


if __name__ == '__main__':
    unittest.main()