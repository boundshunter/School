#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import sys
sys.path.append(BASE_DIR)
import time
import json
import shelve
from conf import settings
from src.school import School
from src.course import Course
from src.student import Student
from src.teacher import Teacher
from src.classroom import Classroom


class School_view(object):

    def __init__(self):

        if os.path.exists(settings.school_file + '.dat'):
            self.sh_obj = shelve.open(settings.school_file)
            self.school_manager()
            self.sh_obj.close()

        else:
            print("没有学校和班级数据，初始化创建学校：")
            self.school__init()
            self.school_manager()
            self.sh_obj.close()

    def school__init(self):
        # 获取 shelve对象
        self.sh_obj = shelve.open(settings.school_file)
        self.sh_obj['北京'] = School('北京分校', '北京')
        self.sh_obj['上海'] = School('上海分校', '上海')

    def school_manager(self):
        while True:
            for sch_name in self.sh_obj:
                print("\033[33;1m学校 : {}\033[0m".format(sch_name))

            sch_option = input("请输入您要选择的学校：").strip()
            # 判断选择的学校是否在学校对象字典中
            if sch_option in self.sh_obj:
                # 取出学校对象
                self.sch_option = sch_option
                # 填充对象，存储的是学校对象，相当于 src.school.School('北京分校','北京')
                self.sch_obj = self.sh_obj[sch_option]
                # print("\033[42;1m填充对象\033[0m", self.sh_obj[sch_option])

                while True:
                    menu = u'''
                        \033[33;1m-------欢迎来到{}校区-------
                        1、添加课程
                        2、添加班级
                        3、添加讲师
                        4、查看课程
                        5、查看班级
                        6、查看讲师
                        7、退出\033[0m
                    '''.format(self.sch_option)
                    print(menu)
                    menu_dic = {
                        '1': 'add_course',
                        '2': 'add_classroom',
                        '3': 'hire_teacher',
                        '4': 'list_course',
                        '5': 'list_classroom',
                        '6': 'list_teacher',
                        '7': 'exit_sys'
                    }
                    user_option = input("请输入您要操作的项目:").strip()
                    if user_option in menu_dic:
                        user_action = menu_dic[user_option]

                        # 反射
                        if hasattr(self, user_action):
                            func = getattr(self, user_action)()
                        else:
                            print("您的选择有误，请重新选择")
                    else:
                        print("您的选项不存在。")
            else:
                print("选择有误，重新输入")
    def add_course(self):
        course_name = input("请输入要添加的课程名：").strip()
        course_price = input("请输入课程的价格：").strip()
        course_time = input("请输入课程的周期(单位:周)：").strip()
        # School类中sch_course方法获取字典
        if course_name in self.sch_obj.sch_course:
            print("课程[%s]已经存在" % course_name)
        else:
            self.sch_obj.create_course(course_name, course_price, course_time)
            print("课程[%s]添加成功" % course_name)


    def add_classroom(self):
        # 班级信息
        classroom_name = input("请输入要添加的班级名称：").strip()
        classroom_course = input("请输入班级所属的课程：").strip()
        # 判断条件，班级不存在，但课程要存在
        if classroom_name not in self.sch_obj.sch_classroom:
            if classroom_course in self.sch_obj.sch_course:
                # course_obj 获取输入课程名称所对应的课程字典对象
                course_obj = self.sch_obj.sch_course[classroom_course]
                self.sch_obj.create_classroom(classroom_name, course_obj)
                # 更新shelve数据
                self.sh_obj.update({self.sch_option: self.sch_obj})
                print("班级\033[33;1m[%s]\033[0m创建成功" % classroom_name)

            else:
                print("您所选择的课程\t[%s]\t不存在,请选择\033[33;1m[查看课程]\033[0m选项后在重新添加."
                      % classroom_course)

        else:
            print("您需要添加的班级[%s]已存在，请使用其他班级名称." % classroom_name)


    def hire_teacher(self):
        # 输入讲师信息
        tech_name = input("输入讲师姓名：").strip()
        tech_gender = input("输入讲师性别：").strip()
        tech_age = input("输入讲师年龄：").strip()
        tech_sal = input("输入讲师薪水：").strip()
        tech_classroom_name = input("输入讲师班级名称：").strip()
        # 判断班级存在
        if tech_classroom_name in self.sch_obj.sch_classroom:
            # 生成班级对象
            tech_classroom_obj = self.sch_obj.sch_classroom[tech_classroom_name]
            # 讲师不存在，创建讲师
            if tech_name not in self.sch_obj.sch_teacher:
                self.sch_obj.create_teacher(tech_name, tech_age, tech_gender, tech_sal,
                                            tech_classroom_name, tech_classroom_obj)
                print("讲师[%s]招聘成功" % tech_name)
            else:
                # 讲师存在，修改讲师信息
                teacher_obj = self.sch_obj.sch_teacher[tech_name]
                self.sch_obj.modify_teacher(tech_name=tech_name, tech_age=tech_age, tech_gender=tech_gender,
                                            tech_sal=tech_sal, tech_classroom_name=tech_classroom_name)
                print("讲师[%s]信息修改成功" % tech_name, tech_age)
            # self.sch_obj[self.sch_option].append(self.sch_obj)
            # 更新 shelve 信息
            self.sh_obj.update({self.sch_option: self.sch_obj})
            print("讲师数据已更新")
        else:
            print("输入的班级[%s]不存在，请先创建班级信息." % tech_classroom_name)


    def list_course(self):
        self.sch_obj.show_course()

    def list_classroom(self):
        self.sch_obj.show_classroom()

    def list_teacher(self):
        self.sch_obj.show_teacher()

    def exit_sys(self):
        sys.exit("Exit the system,bye~")


class Teacher_view(object):

    def __init__(self):
        if os.path.exists(settings.school_file + '.dat'):
            self.school_file = shelve.open(settings.school_file)
            self.teacher_manager()
            self.school_file.close()
        else:
            print("讲师不存在，请先创建学校，并招聘讲师")

    def teacher_manager(self):
        while True:
            for school_name in self.school_file:
                print("学校名称：{}".format(school_name))
            school_option = input("请输入学校名称：").strip()
            if school_option in self.school_file:
                self.sch_obj = self.school_file[school_option] # 学校对象
                self.sch_option = school_option # 学校名称
                teacher_option = input("输入讲师姓名：").strip()
                if teacher_option in self.sch_obj.sch_teacher:
                    self.teacher_obj = self.sch_obj.sch_teacher[teacher_option]
                    self.teacher_option = teacher_option
                    print("欢迎登陆讲师管理系统".center(30,'-'))
                    print("\033[31;1m讲师姓名:{}\n讲师年龄：{}\n讲师性别：{}\n讲师薪资：{}\033[0m"
                          .format(self.teacher_obj.tech_name, self.teacher_obj.tech_age,
                                  self.teacher_obj.tech_gender, self.teacher_obj.tech_sal))
                    menu = u'''
                    1、选择教室
                    2、查看班级、学员
                    3、修改学员成绩
                    '''
                    menu_dic = {
                        '1': 'choose_classroom',
                        '2': 'view_classroom_student',
                        '3': 'change_student_score'
                    }
                    while True:
                        print(menu)
                        option = input("输入选项>>:").strip()
                        if hasattr(self, menu_dic[option]):
                            func = getattr(self, menu_dic[option])()


                else:
                    print("您输入的讲师不存在")
                    return True #返回一级菜单
            else:
                print("学校名称输入有误")
                return True





class Student_view(object):
    def __init__(self):
        if os.path.exists(settings.school_file + '.dat'):
            # 定义shelve对象
            self.shool_file = shelve.open(settings.school_file)
            self.student_manager()
            self.shool_file.close()
        else:
            print("学员不存在，请先创建学校，课程，班级，讲师")

    def student_manager(self):
        menu = u'''
        \033[33;1m-------学员管理项-------
            1、注册学员(注册时选择班级）
            2、学员缴费
            3、修改班级
            4、退出\033[0m
        '''
        menu_dic = {
            '1': 'student_enroll',
            '2': 'student_payment',
            '3': 'student_choose_classroom',
            '4': 'exit_sys'
        }
        while True:

            for sch_name in self.shool_file:
                print("\033[35;1m学校名称：%s\033[0m"% sch_name)
            stu_choice_sch = input("请选择管理的学校名称:").strip()


            if stu_choice_sch in self.shool_file:
                self.sch_option = stu_choice_sch
                self.sch_obj = self.shool_file[stu_choice_sch]
                print("欢迎选择{}学校".format(stu_choice_sch))
            else:
                print("您输入的学校不存在，请重新输入")
                return True

            while True:
                print(menu)
                student_option = input("请输入您的选择：").strip()
                if student_option in menu_dic:
                    student_action = menu_dic[student_option]

                    if hasattr(self, student_action):
                        func = getattr(self, student_action)()
                else:
                    print("您的选择有误，请重新选择")

    def student_enroll(self):
        while True:
            stu_name = input("请输入学员姓名：").strip()
            stu_gender = input("请输入学员性别：").strip()
            stu_age = input("请输入学员年龄：").strip()
            #关联学员班级
            for stu_class_name in self.sch_obj.sch_classroom:
                print("班级：",stu_class_name)

            stu_classroom_name = input("请输入学员班级：").strip()
            if stu_classroom_name in self.sch_obj.sch_classroom:
                # 如果姓名不存在，
                if stu_name not in self.sch_obj.sch_student:
                    # 调用School类中，创建学员函数
                    # 关联学员和班级，将学员添加到相应班级中
                    self.sch_obj.create_student(stu_name, stu_gender, stu_age, stu_classroom_name)
                    self.shool_file.update({self.sch_option:self.sch_obj})
                    print("\033[35;1m------------ student info ------------\033[0m"
                          "\n学员名字：[%s]\t学员性别：[%s]\t学员年龄：[%s]\t" %
                          (stu_name, stu_gender, stu_age))

                    # print("从字典中取出学员：", self.sch_obj.sch_student)
                    return False
                else:
                    print("学员[%s]已经存在，请使用其他名字重新输入" % stu_name)
            else:
                print("您输入的班级[%s]不存在，请重新输入。" % stu_classroom_name)
                return False

    def student_payment(self):
        stu_name = input("请重新输入姓名：").strip()
        if stu_name in self.sch_obj.sch_student:
            student_obj = self.sch_obj.sch_student[stu_name]
            # 对象中取学员信息，student_obj.stu_name 而不是student_obj[stu_name]
            # print("学员信息:",student_obj.stu_name)

            classroom_name = input("请输入班级：").strip()
            if classroom_name in self.sch_obj.sch_classroom:
                classroom_obj = self.sch_obj.sch_classroom[classroom_name]
                course_obj = classroom_obj.course_obj
                # 判断学生注册时关联的班级信息是否为该学生对象信息
                if classroom_obj.classroom_student[classroom_name] == student_obj:
                    print("学员缴费信息：".center(30,'*'))
                    print("\033[31;1m学员班级:%s\n课程名称:%s\n应缴费用:%s\033[0m"
                          % (classroom_name, course_obj.course_name, course_obj.course_price))
                else:
                    print("学员[%s]不属于班级[%s]"% (stu_name, classroom_name))
            else:
                print("班级输入不正确，请重新输入.")
        else:
            print("学员不存在，请先注册学员。")

    def student_choose_classroom(self):
        print("打印班级列表：".center(20,'*'))
        for classroom in self.sch_obj.sch_classroom:
            classroom_obj = self.sch_obj.sch_classroom[classroom]
            print("班级名称:{}".format(classroom_obj.classroom_name))
        stu_name = input("请输入您的姓名：").strip()
        if stu_name in self.sch_obj.sch_student:
            student_obj = self.sch_obj.sch_student[stu_name]
            classroom_name = input("请输入您要选择的班级:").strip()
            if classroom_name in self.sch_obj.sch_classroom:
                 classroom_obj = self.sch_obj.sch_classroom[classroom_name]
                 # 判断 本次所选班级 是否已经存在所选班级中
                 if classroom_obj.classroom_student[classroom_name] == student_obj:
                     print("\033[31;1m班级{}已经选择过，请选择其他班级\033[0m".format(classroom_name))
                 else:# 班级没选择过，选择班级，然后更新班级列表
                     stu_gender = student_obj.stu_gender
                     stu_age = student_obj.stu_age
                     stu_classroom_name = classroom_name
                     self.sch_obj.create_student(stu_name, stu_gender, stu_age, stu_classroom_name)
                     self.shool_file.update({self.sch_option:self.sch_obj})
            else:
                print("班级名不存在，请重新输入")
        else:
            print("学员不存在，请重新输入")


    def exit_sys(self):
        sys.exit("退出系统，谢谢使用")

class Main(object):

    menu = u'''
        \033[35;1m-------- 选课系统入口--------
        1、学校管理
        2、讲师管理
        3、学生管理
        4、退出系统
    \033[0m'''

    menu_dic = {
        "1": "School_view",
        "2": "Teacher_view",
        "3": "Student_view",
        "4": "exit",
    }

    exit_flag = False
    while not exit_flag:
        print(menu)
        user_choice = input("请选择您的管理项:").strip()
        if user_choice in menu_dic:
            func = eval(menu_dic[user_choice])()

        else:
            print("你的选择有误，请重新输入")


