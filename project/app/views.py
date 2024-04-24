from django.shortcuts import render

# Create your views here.
def home(request):
    
    return render(request,'home.html')

# def integer123(request,pk):
#     data=pk
#     return render (request,'home.html',{'key':data})

# def string123(request,ab):
#     data=ab
#     return render (request,'home.html',{'key':data})

# def slug123(request,abc):
#     data=abc
#     return render (request,'home.html',{'key':data})

# def path123(request,pkabc):
#     data=pkabc
#     return render (request,'home.html',{'key':data})

def combination(request,pk,abc,pkabc):
    data:{
        'data1':pk,
        'data2':abc,
        'data3':pkabc
    }

    return render(request,'home.html',{'key': data})


