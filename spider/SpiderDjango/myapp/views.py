from django.shortcuts import render
from myapp.models import Job
from django.http import JsonResponse
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.
def load(request,pIndex):
    # if request.GET.get('position') and request.GET.get('edu') != '':
    # 如果已有了职位搜索
    if request.GET.get('position') or request.GET.get('position')!= '':
        # 筛选相关职位
        # joblist = Job.objects.filter(Q(company__contains=request.GET.get('company'))|Q(job_name__contains=request.GET.get('position')))  # aParent__isnull=True
        joblist = Job.objects.filter(job_name__contains=request.GET.get('position'))  # aParent__isnull=True
        position = request.GET.get('position')
        company = request.GET.get('company')
        print('已有职位搜索条件:',position)
        # 判断是否有学历要求
        if request.GET.get('edu') != '':
            # 再次筛选学历要求
            joblist = joblist.filter(degree=request.GET.get('edu'))
            # 获取选择的学历要求
            degree = request.GET.get('edu')
            print('已有职位搜索条件的学历=1:', degree)
        else:
            joblist = joblist.filter()
            degree = request.GET.get('edu')
            print('已有学历搜索条件的学历2:', degree)
        # 使页码归零
        pIndex = ''
    else:
        # joblist = Job.objects.filter(Q(company__contains=request.GET.get('company'))|Q(job_name__contains=request.GET.get('position')))  # aParent__isnull=True
        joblist = Job.objects.filter(job_name__contains=request.GET.get('position'))  # aParent__isnull=True
        position = request.GET.get('position')
        company = request.GET.get('company')

        print('无职位搜索 1:',position)

        if request.GET.get('edu') != '':
            joblist = joblist.filter(degree=request.GET.get('edu'))
            degree = request.GET.get('edu')
            print('无职位搜索 学历搜索条件:', degree)

        else:
            joblist = joblist.filter()
            degree = request.GET.get('edu')
            print('已有学历搜索条件:', degree)

        pIndex = ''
    p = Paginator(joblist,20)
    if pIndex == '':
        pIndex = '1'
    pIndex = int(pIndex)
    joblist = p.page(pIndex)
    plist = p.page_range
    list = []
    list.append({'pIndex': pIndex,'position':position,'degree':degree,},)
    return render(request, 'index.html', { 'plist': plist, 'pIndex': pIndex,'content':joblist,'degree':degree,'position':position})
    # return JsonResponse({'data':list})
# def index(request):

#     degree = ''
#     position = ''
#
#     joblist = Job.objects.filter()  # aParent__isnull=True
#     pIndex = ''
#     p = Paginator(joblist,20)
#     if pIndex == '':
#         pIndex = '1'
#     pIndex = int(pIndex)
#     joblist = p.page(pIndex)
#     plist = p.page_range
#     return render(request,'index.html',{ 'plist': plist, 'pIndex': pIndex,'content':joblist,'degree':degree,'position':position})




# def load2(request,pIndex):
#     # if request.GET.get('position') and request.GET.get('edu') != '':
#     # 如果已有了职位搜索
#     if request.GET.get('company') != '':
#         # 筛选相关职位
#         # Q(a) | Q(b)
#
#         joblist = Job.objects.filter(Q(company__contains=request.GET.get('company'))|Q(job_name__contains=request.GET.get('position')))  # aParent__isnull=True
#         company = request.GET.get('company')
#         print('已有职位搜索条件:',position)
#         # 判断是否有学历要求
#         if request.GET.get('edu') != '':
#             # 再次筛选学历要求
#             joblist = joblist.filter(degree=request.GET.get('edu'))
#             # 获取选择的学历要求
#             degree = request.GET.get('edu')
#             print('已有职位搜索条件的学历=1:', degree)
#         else:
#             joblist = joblist.filter()
#             degree = request.GET.get('edu')
#             print('已有学历搜索条件的学历2:', degree)
#         # 使页码归零
#         pIndex = ''
#     else:
#         joblist = Job.objects.filter(company__contains=request.GET.get('company'))  # aParent__isnull=True
#         company = request.GET.get('company')
#         print('无职位搜索 1:',company)
#
#         if request.GET.get('edu') != '':
#             joblist = joblist.filter(degree=request.GET.get('edu'))
#             degree = request.GET.get('edu')
#             print('无职位搜索 学历搜索条件:', degree)
#
#         else:
#             joblist = joblist.filter()
#             degree = request.GET.get('edu')
#             print('已有学历搜索条件:', degree)
#
#         pIndex = ''
#
#     p = Paginator(joblist,20)
#     if pIndex == '':
#         pIndex = '1'
#     pIndex = int(pIndex)
#     joblist = p.page(pIndex)
#     plist = p.page_range
#     list = []
#     list.append({'pIndex': pIndex,'company':company,'degree':degree,},)
#
#     return render(request, 'index.html', { 'plist': plist, 'pIndex': pIndex,'content':joblist,'degree':degree,'company':company})