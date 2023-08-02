from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request,'index.html')

def predictpage(request):
    if request.method=='POST':
        married=request.POST.get('married')
        print(married)

    return render(request,'form.html')
