from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from . import rwd


# Create your views here.


def index(request):
    return render(request, 'index.html')


# post请求向数据库中添加数据
@csrf_exempt
def add(request):
    # 确认是否为post请求
    if request.method == "POST":
        # 从post请求中获取数据
        number = request.POST.get("number")
        star = request.POST.get("star")
        nicknames = request.POST.get("nicknames")
        name = request.POST.get("name")
        debut = request.POST.get("debut")
        enertmountain = request.POST.get("enertmountain")
        positions = request.POST.get("positions")
        # 验证一下当需要使用的数据全部得到之后再将数据插入数据库
        if number and star and nicknames and name and debut and enertmountain and positions:
            rwd.write_one(number=number, star=star, nicknames=nicknames, name=name, debut=debut, enertmountain=enertmountain, positions=positions)
            # 数据插入成功，返回一个正确的信息
            date = {
                "status": 200,
                "msg": "ok"
            }
            return JsonResponse(date)
        # 数据存在缺失，让请求放检查一下
        date1 = {
            'status': 202,
            'msg': 'check again please'
        }
        return JsonResponse(date1)

# 删除表中所有内容
@csrf_exempt
def delete_all(request):
    if request.method == "GET":
        rwd.delete_all()
        date = {
            "status": 200,
            "msg": "all deleted"
        }
        return JsonResponse(date)
    date1 = {
        'status': 202,
        'msg': 'check again please'
    }
    return JsonResponse(date1)

# 删除表中一条信息
@csrf_exempt
def delete_one(request):
    if request.method == "GET":
        name = request.GET.get('name')
        rwd.delete_one(name=name)
        date = {
            "status": 200,
            "msg": "one deleted"
        }
        return JsonResponse(date)
    date1 = {
        'status': 202,
        'msg': 'check again please'
    }
    return JsonResponse(date1)

# 更新一条信息
@csrf_exempt
def update_one(request):
    if request.method == "POST":
        # 从post请求中获取数据
        old_number = request.POST.get('old_number')
        number = request.POST.get("number")
        star = request.POST.get("star")
        nicknames = request.POST.get("nicknames")
        name = request.POST.get("name")
        debut = request.POST.get("debut")
        enertmountain = request.POST.get("enertmountain")
        positions = request.POST.get("positions")
        # 验证一下当需要使用的数据全部得到之后再更新数据
        if number and star and nicknames and name and debut and enertmountain and positions and old_number:
            rwd.update_one(number=number, star=star, nicknames=nicknames, name=name, debut=debut, enertmountain=enertmountain, positions=positions,
                           old_number=old_number)
            # 数据插入成功，返回一个正确的信息
            date = {
                "status": 200,
                "msg": "ok"
            }
            return JsonResponse(date)
        # 数据存在缺失，让请求放检查一下
    date1 = {
        'status': 202,
        'msg': 'check again please'
    }
    return JsonResponse(date1)

# 查询表中所有内容
def query_all(request):
    if request.method == "GET":
        return JsonResponse(rwd.query_all())

# 查询表中一条信息
def query_one(request):
    if request.method == "GET":
        name = request.GET.get("name")
        return JsonResponse(rwd.query_one(name=name))

# 一个测试路径的
def number(request, nu, qwe):
    if request.method == "GRT":
        pass
    return HttpResponse("adsf{}sadf{}".format(nu, qwe))
