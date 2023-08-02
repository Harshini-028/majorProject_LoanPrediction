from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request,'index.html')

def predictpage(request):
    if request.method=='POST':
        married=request.POST.get('married')
        Education=request.POST.get('Education')
        Gender=request.POST.get('Gender')
        Self_Employed=request.POST.get('Self_Employed')
        Dependents=request.POST.get('Dependents')
        Income=request.POST.get('Income')
        Property_Area=request.POST.get('Property_Area')
        Loan_Term=request.POST.get('loanterm')
        print(married)

    return render(request,'form.html')
