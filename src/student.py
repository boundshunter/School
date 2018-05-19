#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'


class Student(object):
    # 学生姓名，性别，年龄
    def __init__(self, stu_name, stu_gender, stu_age):
        self.stu_name = stu_name
        self.stu_gender = stu_gender
        self.stu_age = stu_age
        # 初始化学生成绩为0分
        self.score = 0

    # 修改分数，讲师进行修改
    def modify_score(self, new_score):
        self.score = new_score
