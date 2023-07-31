from django.shortcuts import render

# Create your views here.
def data_render(request):
    d={'name':'Pravesh','age':23,'hobbies':['cricket','football']}
    return render(request,'data_render.html',context=d)

def conditions(request):
    d={'a':10000,'b':1500,'c':2000}
    return render(request,'conditionalstatement.html',context=d)

