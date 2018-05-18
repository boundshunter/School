#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

import os
import shelve
from conf import settings
from src.school import School
from src.teacher import Teacher
from src.course import Course
from src.classroom import Classroom
from src.student import Student

class Main(object):


    menu = u'''
        \033[35;1m---------View info-----------
            1、学生视图
            2、讲师视图
            3、学校视图
            4、退出\033[0m
    '''

    exit_flag = False

    while not exit_flag:
        print(menu)
        user_ops = input("请选择要管理的视图，[q] 退出>>:").strip()
        if user_ops =='1':
            Student_view()

        elif user_ops == '2':
            Teacher_view()

        elif user_ops == '3':
            Student_view()

        elif user_ops == '4':

        else:
            print("您输入的选项不正确，请重新输入")


class School_view(object):
    # 学校管理视图
    def __init__(self):
        if os.path.isfile(settings.school_file+'.dat'):
            self.school_file = shelve.open(settings.school_file)
            self.school_manager()
            self.school_file.close()

        else:
            print("没有学校和班级的数据，请先创建")
            self.init_school()
            self.school_manager()
            self.school_file.close()
        '''
        shelve模块
        提供简单数据操作，以键值对方式将数据序列化到文件中，默认以pickle保存，它的key必须是字符串类型
        主要方法:
        f = shelve.open(r'dir/aaa.txt') # 存在则打开文件，不存在就创建文件
        f.update({'key':'value'}) # 更新数据
        f.close() # 关闭文件
        '''

    def init_school(self):
        self.school_file = shelve.open(settings.school_file)
        # 调用 src下school 中的School 类的方法
        self.school_file['北京'] = School('北京总校','北京')
        self.school_file['上海'] = School('上海分校','上海')

    def school_manager(self):

        while True:
            for sch_name in self.school_file:
                print("学校名称{%s}"% sch_name)

            sch_option = input("请输入要管理的学校名称：").strip()
            # 判断学校是否在文件中
            if sch_option in self.school_file:
                # 存在 则 取出学校对象
                self.sch_option = sch_option
                # 填充对象
                self.school_obj = self.school_file[sch_option]

                while True:
                    menu = u'''
                        \033[31;1m------欢迎来到[%s]校区-------
                        1、添加课程 add_course
                        2、添加班级 add_classroom
                        3、添加讲师 add_teacher
                        4、查看班级 show_classroom
                        5、查看课程 show_course
                        6、查看讲师 show_teacher
                        7、退出 \033[0m
                    '''%sch_option
                    print menu
                    user_choice = input("请选择以上操作：").strip()
                    # 反射
                    if hasattr(self,user_choice):
                        getattr(self,user_choice)()

    def add_course(self):
        # 输入创建信息
        course_name = input("请输入课程名称：").strip()
        course_price = input("请输入课程价格：").strip()
        course_time = input("请输入课程周期：").strip()
        # 判断课程，有课程提示，没有课程则创建
        if course_name in self.school_obj.sch_course:
            print("课程[%s]已存在"% course_name)
        else:
            # 调用 src.course中的create_course方法
            self.school_obj.create_course(course_name,course_price,course_time)
            print("课程[%s]添加成功"% course_name)
        # shevle 方式存入文件
        self.school_file.update({self.sch_option:self.school_obj})

    def add_classroom(self):
        # 输入创建班级的信息
        class_name = input("请输入班级名称：").strip()
        class_course = input("请输入课程名称：").strip()
        # 判断班级不存在，且课程存在
        if class_name not in self.school_obj.sch_classroom:
            # 且课程对象在字典中
            if class_name in self.school_obj.sch_course:
                course_obj = self.school_obj.sch_course(class_course)
                self.school_obj.create_class(class_name,course_obj)
                self.school_file.update({self.sch_option:self.school_obj})
                print("班级[%s]创建成功"% class_name)
            else:
                print("课程不存在")
        else:
            print("班级[%s]已经存在"% class_name)

    def add_teacher(self):
        # 输入讲师信息
        tech_name = input("请输入讲师名字：").strip()
        tech_age = input("年龄：")
        tech_sal = input("薪水")
        tech_class = input("授课班级")
        # 判断讲师是否存在
        if tech_class in self.school_obj.sch_classroom:
            class_obj = self.school_obj.sch_classroom[tech_class]
            # 没有讲师就创建讲师
            if tech_name not in self.school_obj.sch_teacher:
                self.school_obj.create_teacher(tech_name,tech_age,tech_gender,tech_sal)
                print("讲师招聘成功")
            # 有讲师就修改讲师信息
            else: # class_obj 修改成classroom obj
                self.school_obj.modify_teacher(tech_name,tech_class,class_obj)
                print("讲师信息修改成功")
            self.school_file.update({self.sch_option:self.school_obj})

        else:
            print("没有讲师对应的班级，请先创建班级信息")

    def show_classroom(self):

    def show_course(self):

    def show_teacher(self):

class Teacher_view(object):

    def __init__(self):
        if os.path.exists(settings.school_file + '.dat'):
            self.school_file = shelve.open(settings.school_file)
            self.teacher_manager()
            self.school_file.close()
        else:
            print("讲师不存在，请先创建学校")

class Student_view(object):
    # 判断数据文件是否存在
    # 输入学校，班级，课程
    # 验证输入的是否存在
    # 存在更新文件，完成学生注册
    print("欢迎进入学生管理视图")
    def __init__(self):
        pass

    def student_manager(self):
        for sch_name in self.school_file:
            print("学校名称:[%s]"% sch_name)

        stu_choice_sch = input("请选择学校名称:").strip()
        if stu_choice_sch in self.school_file:
            self.sch_option = stu_choice_sch
            self.sch_obj = self.school_file[stu_choice_sch]
            stu_name = input("姓名：").strip()
            stu_gender = input("性别：").strip()
            stu_age = input("年龄：").strip()
            self.sch_obj.show_classroom()
            stu_classroom = input("选择要上的班级：").strip()

            if stu_classroom in self.sch_obj.sch_classroom:
                self.sch_obj.create_student(stu_name,stu_gender,stu_age,stu_classroom)
                self.school_file.update({self.sch_option:self.sch_obj})
                print("学生注册成功")
            else:
                print("班级不存在，请先创建班级")
        else:
            print("学校不存在，请先创建学校")
            exit()


