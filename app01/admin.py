#coding:utf-8

from django.contrib import admin
from app01 import models
# Register your models here.

class BBS_admin(admin.ModelAdmin):
    list_display = ["title", "summary", "author", "signature", "view_cnt", "ranking"]
    list_filter = ["created_at", "updated_at"]
    search_fields = ["title", "author__user__username"] #外键不能直接用

    def signature(self, obj):
        return obj.author.signature
    signature.short_description = "签名"

admin.site.register(models.BBS, BBS_admin)
admin.site.register(models.BBS_User)
admin.site.register(models.Category)
admin.site.register(models.Comments)