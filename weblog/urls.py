"""weblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from posts.views import index, home, text_post_list, post_list, post_details, post_create,PostList, PostDetails

urlpatterns = [
    # تو اولين آرگومان حتما بايد تهه اسم، يدونه بك اسلش بذاريا
    path("admin/", admin.site.urls),
    path("index/", index),
    path("house/", home),
    path("text/post/list/", text_post_list, name='text-post-list'),

    path("posts/", post_list),
    path("posts2/", PostList.as_view()),
    # دوتا خط بالا مثل هم عمل ميكنن اما اوليه با تابع كار ميكنه و دومي با كلاس

    # اختياريهnameدادن پارامتر
    path("posts/<int:post_id>/", post_details, name='post-details'),
    path("posts2/<int:pk>/", PostDetails.as_view(), name='post-details'),
    # دوتا خط بالا مثل هم عمل ميكنن اما اوليه با تابع كار ميكنه و دومي با كلاس (فقط دقت كن به لينكي كه دادم به هر كودوم)
    
    path("posts/create/", post_create, name='post-create'),
]
