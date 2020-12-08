from users.models import VerifyCode

__author__='derek'
# from django.contrib import admin
import xadmin
from xadmin import views
# Register your models here.

'''添加主体功能'''
class BaseSetting(object):
    enable_themes=True
    use_bootswatch=True

'''全局配置，后台管理标题和页脚'''
class GlobalSettings(object):
    site_title = "仙剑奇侠传"
    site_footer = "http://www.cnblogs.com/derek1184405959/"
    #菜单收缩
    menu_style="accordion"

class VerifyCodeAdmin(object):
    list_display = ['code','mobile','add_time']

xadmin.site.register(VerifyCode, VerifyCodeAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)