from django.contrib import admin

from .models import Post, Comment


# براي اينكه كامنت ها رو بياد تو صفحه ي پست ها نشون بده،بجاي اين كلاس
# class Commentadmin(admin.ModelAdmin):
#     list_display = ['text','create_time', 'update_time']

# از همچين كلاسي استفاده كن
class CommentAdminInline(admin.TabularInline):
    model = Comment
    fields = ['text']
    extra = 0

# هندل كردن پست ها


class Postadmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_enable', 'publish_date']
    # براي اتصال كامنت ها به پست ها
    inlines = [CommentAdminInline]


admin.site.register(Post, Postadmin)
# يك روش ديگر براي رجيستر كردن يك مدل اينه كه دقيقا تو خط بالاييه كلاس ادمين يك مدل
# بيايي و اين دكوريتور را بنويسي
# @admin.register(Post)
# admin.site.register(Comment , Commentadmin)
