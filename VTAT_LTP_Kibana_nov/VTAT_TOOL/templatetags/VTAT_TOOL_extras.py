from django import template
from VTAT_TOOL.models import *
register = template.Library()


@register.filter(name='split')
def split(string, sep):
	return string.split(sep)[-1]

@register.filter(name='query')
def query(file_category):
	#return [qs]
    return addFilesToCategories.objects.filter(file_category=file_category)

@register.filter(name='concat')
def concat(str1,str2):
	return str(str1)+str(str2)

@register.filter(name="list_to_string")
def list_to_string(list1,sep):
	return sep.join(list1)

@register.filter
def lookup(d, key):
	if d.has_key(key):
		return d[key]
	else:
		return ''

@register.filter
def multi(value,arg):
	return int(value+1)*int(arg)

@register.filter
def add_char(str1,character):
	return str1+character

@register.filter
def list_extract(list_obj):
	return ','.join(str(i.id) for i in list_obj)

@register.filter
def to_lower(str1):
	return str1.lower()

@register.assignment_tag
def define(val=None):
  return val