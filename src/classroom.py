#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'jfsu'

class Classroom(object):
    # 班级名称，课程，学生
    def __init__(self, classroom_name, course_obj):
        self.classroom_name = classroom_name
        self.course_obj = course_obj
        # 字典形式保存学生对象
        self.classroom_student = {}