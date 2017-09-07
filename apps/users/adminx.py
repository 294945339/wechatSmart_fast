# -*- coding: utf-8 -*-
import xadmin
from xadmin.plugins.auth import UserAdmin
from xadmin import views
from .models import UserProfile

# ----- adminx 全局配置
class BaseSetting:
    enable_themes = True
    use_bootswatch = True

# from django.contrib.auth import get_user_model
# User = get_user_model()
#
# class UserProfileAdmin(UserAdmin):
#     pass
#
# from django.contrib.auth.models import User
# xadmin.site.unregister(User)
#
# xadmin.site.register(UserProfile, UserProfileAdmin)

class GlobalSettings:
    site_title = 'dj快速开发平台'
    site_footer  = '294945339@qq.com'
    menu_style = 'accordion'

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)