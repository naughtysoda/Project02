from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import Board
from django.views.generic import UpdateView
from django.views.generic import TemplateView
from django.urls import path

class ChartView(TemplateView):
    template_name = 'chart.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Board.objects.all().order_by('-star')
       
        return context

def home(request):
    mgs = {
                    'massage' : ' '
                }
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        comment = request.POST.get('comment')
        rate = request.POST.get('rate')
        x_create = Board(
            firstname = firstname,
            description = comment,
            star = rate
        )
        x_create.save()
        mgs = {
                    'massage' : 'Done'
                }
         
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards,'mgs': mgs})

def table(request):
    boards = Board.objects.all().order_by('id')
    return render(request, 'table.html', {'boards': boards})

def edit(request,Progress_ID):
    boards = Board.objects.get(pk=Progress_ID)
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        comment = request.POST.get('comment')
        rate = request.POST.get('rate')
        boards.firstname = firstname
        boards.description = comment
        boards.star = rate
        boards.save()
        return redirect('table')
    return render(request, 'edit.html',{'boards':boards})

# def chart(request):
#     # do something...
#     return render(request, 'chart.html')

def about(request):
    # do something...
    return render(request, 'about.html')

def about_company(request):
    # do something else...
    # return some data along with the view...
    return render(request, 'about_company.html', {'company_name': 'Simple Complex'})

# def logintest(idm_login):
#         Emp_id = request.POST.get('userID')
#         passwordID = str(request.POST.get('passwordID'))
        
#         # check_user = Plan_Head.objects.filter(Username = userID, Password = passwordID).count()
#         check_ID = idm_login(Emp_id,passwordID)
#         reposeMge = check_ID
#         if reposeMge == 'true':
#                 nameget = idm(Emp_id)

def logintest(request):
    if request.method == 'POST':
        username=requset.POST['username']
        password=requset.POST['password']
        check_ID = idm_login(username,password)
        print('55555555')
    return render(request, 'logintest.html')

def idm_login(username, password):
    # Emp_passc = str(Emp_pass)
    print('--------------------')
    
    url="https://idm.pea.co.th/webservices/idmservices.asmx?WSDL"
    headers = {'content-type': 'text/xml'}
    xmltext ='''<?xml version="1.0" encoding="utf-8"?>
                 <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                    <soap:Body>
                        <IsValidUsernameAndPassword_SI xmlns="http://idm.pea.co.th/">
                        <WSAuthenKey>{0}</WSAuthenKey>
                        <Username>{1}</Username>
                        <Password>{2}</Password>
                        </IsValidUsernameAndPassword_SI>
                    </soap:Body>
                </soap:Envelope>'''
    wskey = '07d75910-3365-42c9-9365-9433b51177c6'
    body = xmltext.format(wskey,Emp_id,Emp_pass)
    response = requests.post(url,data=body,headers=headers)
    print(response.status_code)
    o = xmltodict.parse(response.text)
    jsonconvert=dict(o)
    # print(o)
    authen_response = jsonconvert["soap:Envelope"]["soap:Body"]["IsValidUsernameAndPassword_SIResponse"]["IsValidUsernameAndPassword_SIResult"]["ResultObject"]
    return authen_response