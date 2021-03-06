#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : forms.py
# @Author: hanxx
# @Date  : 2018/5/3
# @Desc  : 前端form表单
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField, FileField, TextAreaField
from wtforms.validators import EqualTo, DataRequired, Email, Regexp, ValidationError
from app.modules import *


class RegistForm(FlaskForm):
    '''注册'''
    name = StringField(
        label='用户账号',
        validators=[
            DataRequired('请输入您的账号')
        ],
        description='账号',
        render_kw={
            "id": "input_name",
            "class": "form-control input-lg",
            "placeholder": "昵称"
        }
    )
    email = StringField(
        label='邮箱',
        validators=[
            DataRequired('请输入您的邮箱'),
            Email('邮箱格式不正确')
        ],
        description='邮箱',
        render_kw={
            "id": "input_email",
            "class": "form-control input-lg",
            "placeholder": "邮箱"
        }
    )
    phone = StringField(
        label='手机号码',
        validators=[
            DataRequired('请输入手机号码'),
            Regexp('1[3,4,5,6,7,8]\\d{9}', message='手机号码格式不正确')
        ],
        description='手机号码',
        render_kw={
            "id": "input_phone",
            "class": "form-control input-lg",
            "placeholder": "手机号码"
        }
    )
    pwd = PasswordField(
        label='密码',
        validators=[
            DataRequired('请输入密码')
        ],
        description='密码',
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入密码！",
        }
    )
    repwd = PasswordField(
        label='确认密码',
        validators=[
            DataRequired('请输入确认密码'),
            EqualTo('pwd', message='两次密码输入不一致')
        ],
        description='确认密码',
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入确认！",
        }
    )
    submit = SubmitField(
        label='注册',
        render_kw={
            "class": "btn btn-lg btn-success btn-block",
        }
    )

    # 验证账号是否存在
    def validate_name(self, field):
        name = field.data
        user = User.query.filter_by(name=name).count()
        if user != 0:
            raise ValidationError('账号已存在！')

    # 验证邮箱
    def validate_email(self, field):
        email = field.data
        user = User.query.filter_by(email=email).count()
        if user != 0:
            raise ValidationError('邮箱已存在！')

    # 验证手机号码
    def validate_phone(self, field):
        phone = field.data
        user = User.query.filter_by(phone=phone).count()
        if user != 0:
            raise ValidationError('手机号码已存在！')


class LoginForm(FlaskForm):
    '''登陆'''
    name = StringField(
        label='账号',
        validators=[
            DataRequired('请输入账号')
        ],
        description='账号',
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入账号",
        }
    )
    pwd = PasswordField(
        label="密码",
        validators=[
            DataRequired("请输入密码！")
        ],
        description="密码",
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "请输入密码！",
        }
    )
    submit = SubmitField(
        '登录',
        render_kw={
            "class": "btn btn-lg btn-primary btn-block",
        }
    )


class UserinfoForm(FlaskForm):
    '''用户中心'''
    name = StringField(
        label='账号',
        validators=[
            DataRequired('请输入账号')
        ],
        description='账号',
        render_kw={
            "class": "form-control",
            "placeholder": "请输入账号",
        }
    )
    email = StringField(
        label="邮箱",
        validators=[
            DataRequired("请输入邮箱！"),
            Email("邮箱格式不正确！")
        ],
        description="邮箱",
        render_kw={
            "class": "form-control",
            "placeholder": "请输入邮箱！",
        }
    )
    phone = StringField(
        label='手机号码',
        validators=[
            DataRequired('请输入手机号码'),
            Regexp('1[3,4,5,6,7,8]\\d{9}', message='手机号码格式不正确')
        ],
        description='手机号码',
        render_kw={
            "id": "input_phone",
            "class": "form-control input-lg",
            "placeholder": "手机号码"
        }
    )
    face = FileField(
        label='头像',
        validators=[
            DataRequired('请上传您的头像')
        ],
        description='头像'
    )
    info = TextAreaField(
        label="个性签名",
        description="简介",
        render_kw={
            "class": "form-control",
            "rows": 10
        }
    )
    submit = SubmitField(
        '保存修改',
        render_kw={
            "class": "btn btn-success"
        }
    )


class PwdForm(FlaskForm):
    '''修改密码'''
    old_pwd = PasswordField(
        label='旧密码',
        validators=[
            DataRequired('请输入旧密码')
        ],
        description='旧密码',
        render_kw={
            "class": "form-control",
            "placeholder": "请输入旧密码"
        }
    )
    new_pwd = PasswordField(
        label='新密码',
        validators=[
            DataRequired('请输入新的密码')
        ],
        description='新密码',
        render_kw={
            "class": "form-control",
            "placeholder": "请输入新密码"
        }
    )
    submit = SubmitField(
        '修改密码',
        render_kw={
            "class": "btn btn-success"
        }
    )


class CommentForm(FlaskForm):
    '''评论列表'''
    content = TextAreaField(
        label='内容',
        validators=[
            DataRequired('请输入内容！')
        ],
        description='内容',
        render_kw={
            'id': 'input_content'
        }
    )
    submit = SubmitField(
        '提交评论',
        render_kw={
            "class": "btn btn-success",
            "id": "btn-sub"
        }
    )
