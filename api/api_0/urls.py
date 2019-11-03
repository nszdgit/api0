from . import views
from django.urls import path

urlpatterns = [
    #增加一条信息到数据库
    path('add/', views.add, name='add'),
    # 删除数据库所有信息
    path('delete_all/', views.delete_all, name='delete_all'),
    # 删除一条信息
    path('delete_one/', views.delete_one, name='delete_one'),
    # 更新一条信息
    path('update_one/', views.update_one, name='update_one'),
    # 查询所有信息
    path('query_all/', views.query_all, name='query_all'),
    # 查询一条信息
    path('query_one/', views.query_one, name='query_one'),
    # 测试一个路径而已
    path('<nu>/<qwe>', views.number, name='index')
]
