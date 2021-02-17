from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import Board,Profile
from django.views.generic import UpdateView
from django.views.generic import TemplateView
from django.urls import path
import datetime
import requests, xmltodict

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

def logintstar(request):
    aerror = {
                'x' : ' '
                }
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        if username == '464628' or username == '501103':
                check_ID = idm_login(username,password)
                reposeMge = check_ID  
                if reposeMge == 'true':
                        nameget = idm(username)
                        Fullname = nameget['TitleFullName']+nameget['FirstName']+' '+nameget['LastName']
                        Position = nameget['Position']
                        LevelCode = nameget['LevelCode']
                        DepartmentShort = nameget['DepartmentShort']
                        Sap = nameget['NewOrganizationalCode']
                        StaffStartDate = nameget['StaffDate'].split('/')
                        SSD = StaffStartDate[2]+"-"+StaffStartDate[1]+"-"+StaffStartDate[0]
                        StaffDate = nameget['StaffDate'].split('/')
                        Workage = int(StaffDate[2])-543
                        today = datetime.datetime.today()
                        yearBE = today.year
                        Someyear = yearBE-Workage  
                        x_create = Profile(
                              empid = username,
                              name = Fullname,
                              position = Position,
                              position_level = LevelCode,
                              department_name = DepartmentShort,
                              department_code = Sap,
                              workage = SSD
                               )
                        x_create.save()
                        print(Fullname,Position,LevelCode,DepartmentShort,Sap,Someyear,SSD)
                        return redirect('pinthestar')
        else:
            aerror = {
                    'x':'Invalid Credentials. Please try again.'
                    }
    return render(request,'logintstar.html',{'aerror': aerror,'Profile': Profile})        

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
    body = xmltext.format(wskey,username,password)
    response = requests.post(url,data=body,headers=headers)
    print(response.status_code)
    o = xmltodict.parse(response.text)
    jsonconvert=dict(o)
    # print(o)
    authen_response = jsonconvert["soap:Envelope"]["soap:Body"]["IsValidUsernameAndPassword_SIResponse"]["IsValidUsernameAndPassword_SIResult"]["ResultObject"]
    return authen_response

def idm(username):
    url="https://idm.pea.co.th/webservices/EmployeeServices.asmx?WSDL"
    headers = {'content-type': 'text/xml'}
    xmltext ='''<?xml version="1.0" encoding="utf-8"?>
                <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
                <soap:Body>
                    <GetEmployeeInfoByEmployeeId_SI xmlns="http://idm.pea.co.th/">
                        <WSAuthenKey>{0}</WSAuthenKey>
                        <EmployeeId>{1}</EmployeeId>
                        </GetEmployeeInfoByEmployeeId_SI>
                </soap:Body>
                </soap:Envelope>'''
    wsauth = 'e7040c1f-cace-430b-9bc0-f477c44016c3'
    body = xmltext.format(wsauth,username)
    response = requests.post(url,data=body,headers=headers)
    o = xmltodict.parse(response.text)

    # print(o)
    jsonconvert=o["soap:Envelope"]['soap:Body']['GetEmployeeInfoByEmployeeId_SIResponse']['GetEmployeeInfoByEmployeeId_SIResult']['ResultObject']
    employeedata = dict(jsonconvert)
    # print(employeedata['FirstName'])
    return employeedata

def pinthestar(request):
    pin = {
                    'pin' : ' '
                }
    if request.method == 'POST':
        pin = request.POST.get('pin')
        x_create = Profile(
            pin = pin
        )
        x_create.save()
        pin = {
                    'pin' : 'Done'
                }
        return redirect('home')
    return render(request,'pinthestar.html',{'pin': pin,'Profile': Profile}) 