# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Shop(models.Model):

    name = models.CharField(max_length=50, verbose_name=u'名称', default='')
    add = models.CharField(max_length=50, null=True, blank=True,verbose_name=u'地址')
    shopDate = models.CharField(max_length=11, null=True, blank=True, verbose_name=u'营业时间')
    tel = models.CharField(max_length=50, null= True,blank= True , verbose_name=u"联系电话")
    image = models.ImageField(max_length=100,null= True,blank= True , upload_to='image/%Y/%m', verbose_name=u'门店照片')

    def get_readonly_fields(self):
        """  重新定义此函数，限制普通用户所能修改的字段  """
        if self.user.is_superuser:
            self.readonly_fields = []
        return self.readonly_fields

    readonly_fields = ('name',)

    class Meta:
        verbose_name = u'门店信息'
        verbose_name_plural = verbose_name



    def __unicode__(self):
        return self.name