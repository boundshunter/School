#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

from src.classroom import Classroom
from src.course import Course
from src.teacher import  Teacher
from src.student import Student

class School(object):
    # 校名，地址，课程，班级，讲师，学生
    def __init__(self,name,address):
        self.name = name
        self.address = address
        self.sch_classroom = {}
        self.sch_course = {}
        self.sch_teacher = {}
        self.sch_student = {}

    # 创建课程
    def create_course(self,course_name,course_price,course_time):
        # 创建课程对象
        # 根据课程名称key，课程对象value，建立对应关系
        course_obj = Course(course_name,course_price,course_time)
        self.sch_course[course_name] = course_obj

    # 显示课程
    def show_course(self):
        for course in self.sch_course:
            course_obj = self.sch_course[course]
            print(course_obj)
            print("课程名称{%s}\t课程价格{%s}\t学习周期{%s}"% ( course_obj.course_name,course_obj.course_price,
                                                    course_obj.course_time))
    # 修改课程
    def modify_course(self,**kwargs):
        # 根据key取出课程对象
        # 修改course_obj的每个值 **kwargs
        # 保存
        pass

    # 创建班级
    def create_classroom(self,class_name, course_obj):
        class_obj = Classroom(class_name, course_obj)
        self.sch_classroom[class_name] = class_obj

    def show_classroom(self):
        pass

    def modify_classroom(self,**kwargs):
        pass


    # 创建讲师
    def create_teacher(self, tech_name, tech_age, tech_gender, tech_sal, class_name, class_obj):

        teacher_obj = Teacher(tech_name, tech_age, tech_gender, tech_sal)
        teacher_obj.add_tech_classroom(class_name,class_obj)
        self.sch_teacher[tech_name] = teacher_obj

    def show_teacher(self):
        pass

    def modify_teacher(self,**kwargs):
        pass


    # 创建学生
    def create_student(self, name, gender, age, class_name):
        # 创建学生对象
        student_obj = Student(name,gender,age)
        self.sch_student[name] = student_obj

        # 建立学生和班级的关联关系
        class_obj = self.sch_classroom[class_name]
        class_obj.class_student[name] = student_obj

        # 更新班级信息
        self.sch_classroom[class_name] = class_obj

    def show_teacher_student_info(self, tech_name):

        teacher_obj = self.sch_teacher[tech_name]
        # teacher_obj 初始化为 讲师的对象，讲师对象里面包含 tech_classroom 属性 (self.tech_classroom = {})
        for t in teacher_obj.tech_classroom:
            class_obj = self.sch_classroom[t]
            stu_list = []
            # classroom 含有 class_student属性
            for j in class_obj.class_student:
                stu_list.append(j)
            print("班级名称{%s}\t课程{%s}\t学生{%s}"% (class_obj.class_name,
                                               class_obj.course_obj.course_name,
                                               stu_list))

    # 哪个老师修改的哪个学生的新分数
    def modify_student_score(self,tech_name,new_score):

        # 查出讲师对应的班级
        # 查出该班级学生数
        # 输入学生姓名，如果存在，则调用 modify_score方法进行修改
        # 保存
