#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'jfsu'

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
            Student_vies()

        elif user_ops == '2':
            Tea
        elif user_ops == '3':

        elif user_ops == '4':

        else:
            print("您输入的选项不正确，请重新输入")


class School_view(object):



class Teacher_view(object):
    pass

class Student_view(object):
    pass
