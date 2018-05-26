#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'


class Teacher(object):
    # 讲师姓名，讲师年龄，讲师薪水，所关联的班级
    def __init__(self, tech_name, tech_age, tech_gender, tech_sal, tech_classroom_name, tech_classroom_obj):
        self.tech_name = tech_name
        self.tech_age = tech_age
        self.tech_gender = tech_gender
        self.tech_sal = tech_sal
        self.tech_classroom = {}
        self.tech_classroom_name = tech_classroom_name
        self.tech_classroom_obj = tech_classroom_obj

    # 讲师和教师建立关系
    def add_tech_classroom(self, tech_classroom_name, tech_classroom_obj):
        self.tech_classroom[tech_classroom_name] = tech_classroom_obj
