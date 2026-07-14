from django.shortcuts import render, redirect
import requests
from django.contrib import messages

root='http://127.0.0.1:8000/api/admin/'

def home(request):
    api=root+'books/'
    data=requests.get(api)
    return render(request,'home.html',{'data':data.json()})

def catelog(request):
    if request.method=='GET':
        if 'q' in request.GET:
            q=request.GET['q']
            if q=='':
                api=root+'books/'
                data=requests.get(api)
            else:
                api=root+f'search/{q}'
                data=requests.get(api)
        else:
            api=root+'books/'
            data=requests.get(api)
    return render(request,'catelog.html',{'data':data.json()})

def details(request,id):
    api=root+f'book/{id}'
    data=requests.get(api)
    datas=data.json()
    api2=root+f'similarbooks/{id}'
    data1=requests.get(api2)
    if datas['total_copies'] > 0:
        percent = int((datas['available_copies'] / datas['total_copies']) * 100)
    else:
        percent = 0
    return render(request,'details.html',{'i':datas,'percent':percent, "width": f"{percent}%",'j':data1.json()})




def borrowBook(request,id):
    if request.method=='GET':
        access = request.session.get("access")
        response = requests.get("http://127.0.0.1:8000/api/profile/",
        headers={
            "Authorization": f"Bearer {access}"
        }
        )
        data = {}
        if response.status_code == 200:
            data = response.json()
            uname=data['username']
            api=f'http://127.0.0.1:8000/api/members/buy_book/'
            res=requests.post(api,{'id':id,'uname':uname})
            if res.status_code!=201:
                print('already borrowed')
                messages.error(request,'Book already Borrowed')
                return redirect(details,id)
            else:
                messages.success(request,'Book Reserved Successfully.')
                return redirect(home)
    return redirect(home)


def about(request):
    return render(request,'about.html')


def dashboard(request):
    access = request.session.get("access")
    response = requests.get("http://127.0.0.1:8000/api/profile/",
    headers={
        "Authorization": f"Bearer {access}"
    }
    )
    data = {}
    if response.status_code == 200:
        data = response.json()
        uname=data['username']
        api='http://localhost:8000/api/members/reservedBooks/'
        res=requests.post(api,{'uname':uname})
        return render(request,'dashboard.html',{'data':res.json(),'user':uname})
    return render(request,'dashboard.html')