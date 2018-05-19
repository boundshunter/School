#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

from src.classroom import Classroom
from src.course import Course
from src.teacher import  Teacher
from src.student import Student

class School(object):
    # 校名，地址，课程，班级，讲师，学生
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.sch_classroom = {}
        self.sch_course = {}
        self.sch_teacher = {}
        self.sch_student = {}

    # 创建课程
    def create_course(self,course_name,course_price,course_time):
        # 创建课程对象
        course_obj = Course(course_name, course_price, course_time)
        # 根据课程名称key，课程对象value，建立对应关系
        self.sch_course[course_name] = course_obj

    # 显示课程
    def show_course(self):

        for course in self.sch_course:
            # 循环取出 course_name对应的课程对象，取出sch_course字典的value
            course_obj = self.sch_course[course]
            print(course_obj)
            # 打印显示结果
            print("课程名称{%s}\t课程价格{%s}\t学习周期{%s}"% ( course_obj.course_name,course_obj.course_price,
                                                    course_obj.course_time))
    # 修改课程
    def modify_course(self,**kwargs):
        # 根据key取出课程对象
        # 修改course_obj的每个值 **kwargs  update 字典
        # 保存
        pass

    # 创建班级
    def create_classroom(self, classroom_name, course_obj):
        # 调用 src.Classroom 生成班级对象
        classroom_obj = Classroom(classroom_name, course_obj)
        # 班级对象存入字典
        self.sch_classroom[classroom_name] = classroom_obj
        print(self.sch_classroom)

    # 显示班级
    def show_classroom(self):
        # 循环取出班级
        for classroom in self.sch_classroom:
            # 根据取出的班级获取班级对象，根据key获取value，key为 classroom
            classroom_obj = self.sch_classroom[classroom]
            print(classroom_obj)
            # 打印结果
            print("班级名称[%s]\t课程[%s]\t学生[%s]" % (classroom_obj.classroom_name, classroom_obj.course_obj,
                                                classroom_obj.classroom_student))


    def modify_classroom(self,**kwargs):
        pass


    # 创建讲师
    def create_teacher(self, tech_name, tech_age, tech_gender, tech_sal, class_name, class_obj):
        # 调用src.Teacher 获取 讲师对象
        teacher_obj = Teacher(tech_name, tech_age, tech_gender, tech_sal)
        # 生成对象调用add_tech_classroom方法生成讲师和教室关系
        teacher_obj.add_tech_classroom(class_name, class_obj)
        # 生成 讲师 字典
        self.sch_teacher[tech_name] = teacher_obj

    def show_teacher(self):
        pass

    def modify_teacher(self, **kwargs):
        pass


    # 创建学生
    def create_student(self, stu_name, stu_gender, stu_age, classroom_name):
        # 创建学生对象
        student_obj = Student(stu_name, stu_gender, stu_age)
        self.sch_student[stu_name] = student_obj

        # 建立学生和班级的关联关系
        # 获取班级对象
        classroom_obj = self.sch_classroom[classroom_name]
        # classroom_obj.classroom_student 获取字典值，取自src.classroom类中的 classroom_student 属性
        classroom_obj.classroom_student[classroom_name] = student_obj

        # 更新班级信息
        self.sch_classroom[classroom_name] = classroom_obj

    # 显示讲师对应学员信息
    def show_teacher_student_info(self, tech_name):

        # 获取讲师对象
        teacher_obj = self.sch_teacher[tech_name]
        # teacher_obj 初始化为 讲师的对象，讲师对象里面包含 tech_classroom 属性 (self.tech_classroom = {})
        for t in teacher_obj.tech_classroom:
            class_obj = self.sch_classroom[t]
            stu_list = []
            # classroom 含有 classroom_student属性，循环获取学员列表
            for j in class_obj.classroom_student:
                stu_list.append(j)
            print("班级名称{%s}\t课程{%s}\t学生{%s}" % (class_obj.class_name,
                                                class_obj.course_obj.course_name,
                                                stu_list))

    # 哪个老师修改的哪个学生的新分数
    def modify_student_score(self, tech_name, new_score):

        # 查出讲师对应的班级
        # 查出该班级学生数
        # 输入学生姓名，如果存在，则调用 modify_score方法进行修改
        # 保存
        pass
