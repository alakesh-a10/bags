from django.shortcuts import render,HttpResponseRedirect
from application . forms import BagsForm

a=[]
def add(request):
    fm=BagsForm()
    if request.method=='POST':
        fm=BagsForm(request.POST)
        if fm.is_valid():
            b=fm.cleaned_data['Feedback']
            a.append(b)
    return render(request,'application/bags.html',{'a':a,'form':fm,})

def delete(request,c):
    a.remove(c)
    return HttpResponseRedirect('/')


    


