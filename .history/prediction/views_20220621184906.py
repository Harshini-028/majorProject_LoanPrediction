from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout

import pandas as pd
import pickle 
from django.contrib import messages

import pickle 
import locale
pipe=pickle.load(open("/home/shreyank/miniprojectc18/loanprediction/finalized_model.pkl","rb"))
# Create your views here.

def homepage(request):
    return render(request,'index.html')

def predictpage(request):
    if request.method=='POST':
        married=request.POST.get('married')
        Education=request.POST.get('Education')
        Gender=request.POST.get('Gender')
        
        Self_Employed=request.POST.get('Self_Employed')
        Dependents=request.POST.get('Self_Employed')
        Income=request.POST.get('Income')
        Property_Area=request.POST.get('Property_Area')
        Loan_Term=request.POST.get('loanterm')
        CoapplicantIncome=request.POST.get('CoapplicantIncome')
        LoanAmount=request.POST.get('LoanAmount')
        Credit_History=request.POST.get('Credit_History')
        # print(married,Education,Gender,Self_Employed,Dependents,Income,Property_Area,Loan_Term)
        input=pd.DataFrame([[married,Education,Gender,Self_Employed,Dependents,Income,Property_Area,Loan_Term,CoapplicantIncome,LoanAmount,Credit_History]],columns=['Married','Education','Gender','Self_Employed','Dependents','ApplicantIncome','Property_Area','Loan_Amount_Term','CoapplicantIncome','LoanAmount','Credit_History'])
        answer=(pipe.predict(input))
        
        print(answer)
        if(answer==1):
            answer="Loan Approved"
        else:
            answer="Loan is Not Approved"
        return render(request,'form.html',{'result':answer})

    return render(request,'form.html')
