from django.shortcuts import render
import requests

root='http://127.0.0.1:8000/api/admin/'

def home(request):
    api=root+'books/'
    data=requests.get(api)
    print(data.json())
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
    percent=int((datas['available_copies']/datas['total_copies'])*100)
    return render(request,'details.html',{'i':data.json(),'percent':percent, "width": f"{percent}%"})