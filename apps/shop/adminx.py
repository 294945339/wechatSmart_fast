# -*- coding: utf-8 -*-
import xadmin


from .models import Shop
import xadmin


class ShopAdmin(object):

    shops = ('id','name', 'tel', 'add')
    list_per_page = 20
    show_detail_fields = ['name']
    refresh_times = (3,5)

#还有点问题
    list_bookmarks = [{
        'title': "温州地区",         # 书签的名称, 显示在书签菜单中
        'query': {'tel__contains': '1'}, # 过滤参数, 是标准的 queryset 过滤
        'order': ('-id'),         # 排序参数
        'cols': ('id', 'name', 'add'),  # 显示的列
        'search': 'tel'    # 搜索参数, 指定搜索的内容
        }
    ]


xadmin.site.register(Shop, ShopAdmin)