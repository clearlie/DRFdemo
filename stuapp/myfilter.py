#coding=utf-8


#过滤器
from django.template import Library
import markdown

register = Library()

@register.filter
def md(value):
    return markdown.markdown(value)