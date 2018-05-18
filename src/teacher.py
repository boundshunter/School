#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'


class Teacher(object):
    # 讲师姓名，讲师年龄，讲师薪水，所关联的班级
    def __init__(self, tech_name, tech_age, tech_gender, tech_sal):
        self.tech_name = tech_name
        self.tech_age = tech_age
        self.tech_gender = tech_gender
        self.tech_sal = tech_sal
        self.tech_classroom = {}

    # 讲师和教师建立关系
    def add_tech_classroom(self,class_name,class_obj):
        self.tech_classroom[class_name] = class_obj
