from django.shortcuts import render

def home(request):
    n={'name':'habib', 'age':'21','place':'dhaka','quote':"I'm habib",'nothing':'',
       'value':[{'name': 'zed', 'age': 19},
            {'name': 'amy', 'age': 22},{'name': 'joe', 'age': 31}],
            'unorder':['States', ['Kansas', ['Lawrence', 'Topeka'], 'Illinois']]}
    return render(request,'home.html',n)