from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from .models import Formerdata
import pandas as pd
import pickle 
from django.contrib import messages
from .models import Formerdata,District, Taluk, Hobali, Village, Surveynumber, HissaNO, Peroid, Owner

import pickle 
import locale
pipe=pickle.load(open("prediction/finalized_model (1).pkl","rb"))
# Create your views here.
context = {}
def homepage(request):
    return render(request,'index.html')


def predictpage(request):
    if request.method=='POST':
        
        Married=request.POST.get('Married')
        Education=request.POST.get('Education')
        Gender=request.POST.get('Gender')
        
        Self_Employed=1
        Dependents=request.POST.get('Dependents')
        ApplicantIncome=request.POST.get('ApplicantIncome')
        Property_Area=request.POST.get('Property_Area')
        Loan_Amount_Term=request.POST.get('Loan_Amount_Term')
        CoapplicantIncome=request.POST.get('CoapplicantIncome')
        LoanAmount=request.POST.get('LoanAmount')
        Credit_History= 0
        Loan_ID=request.POST.get('Loan_ID')    
        print(Married,Education,Gender,Self_Employed,Dependents,ApplicantIncome,Property_Area,Loan_Amount_Term,CoapplicantIncome,LoanAmount,Credit_History)
        input=pd.DataFrame([[Gender,Married,Dependents,Education,Self_Employed,ApplicantIncome,CoapplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area
]],columns=['Gender','Married','Dependents','Education','Self_Employed','ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History','Property_Area'
])
        print(input)
        answer=(pipe.predict(input))
        
        # print(answer)

        
        # print(Loan_ID)
        if(answer[0]==1):
           answer1="Loan Approved"
           return render(request,"form.html",{"result":answer1})
        else:
            answer2="Loan is Not Approved"
            return render(request,"form.html",{"result":answer2})

    return render(request,'form.html')


def verify(request):
    if request.method=='POST':
        fid=request.POST.get('Farmer_id')
        aadhar_num=request.POST.get('aadhar_number')
        number=request.POST.get('phone_number')
        print(fid,aadhar_num,number)
        if not Formerdata.objects.filter(fid=fid,aadharno=aadhar_num):
             return render(request,"form.html",{"result12":"Farmer Not Verified"})
        else:
             return render(request,"form.html",{"result12":"Farmer Verified"})

        return render(request,'form.html')
    

def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'services.html')

def aadharverify(request):
    return render(request,'aadharVerification.html')

def prediction(request):
    return render(request,'prediction.html')


# getvillage = None
# getsurveynum = None
# gethissanum = None
# getperiod = None

def dependantfield(request):
    districtid = request.GET.get('district', None)
    talukid = request.GET.get('taluk', None)
    hobaliid = request.GET.get('hobali', None)
    villageid = request.GET.get('village', None)
    surveyid = request.GET.get('survey',None)
    hissaid = request.GET.get('hissa',None)

    district = None
    taluk = None
    hobali = None
    village = None
    surveynum = None
    hissanum = None
    period = None
    flag = False
    
    if districtid:
        getdistrict = District.objects.get(id=districtid)
        taluk = Taluk.objects.filter(district=getdistrict)
    if talukid:
        gettaluk = Taluk.objects.get(id=talukid)
        hobali = Hobali.objects.filter(taluk=gettaluk)
    if hobaliid:
        gethobali = Hobali.objects.get(id=hobaliid)
        village = Village.objects.filter(hobali=gethobali)
    if villageid:
        getvillage = Village.objects.get(id=villageid)
        surveynum = Surveynumber.objects.filter(village=getvillage)
    if surveyid:
        getsurveynum = Surveynumber.objects.get(id=surveyid)
        hissanum = HissaNO.objects.filter(village=getvillage,surveyno=getsurveynum)
        if hissanum:
            flag = True
    if hissaid:
        gethissanum = HissaNO.objects.get(id=hissaid)
        period = Peroid.objects.filter(village=getvillage,surveyno=getsurveynum,hissano=gethissanum)

    

    district = District.objects.all()
    
    return render(request, 'dependentfiled.html', locals())

def findPahani(request):   
    villageid = request.POST.get('village',None)
    surveyid = request.POST.get('surveynum',None)
    hissaid = request.POST.get('hissanum',None)
    periodid = request.POST.get('period',None)
    
    # print(villageid,surveyid,hissaid,periodid)
    thisvillage = Village.objects.get(id=villageid)
    surveynum = Surveynumber.objects.get(id=surveyid)
    hissa = HissaNO.objects.get(id=hissaid)
    period = Peroid.objects.get(id=periodid)

    # print(village,surveynum,hissanum)
    # print(villageid,surveyid,hissaid)
    data = None
    data = Owner.objects.filter(village=thisvillage,surveyno=surveynum,hissano=hissa)
    # context = {
    #     'result' :data,
    #     'resvillage' :thisvillage,
    #     'ressurveynum':surveynum ,
    #     'reshissanum' : hissa,
    #     'resperiod' : period 
    # }
    context['result'] = data
    context['resvillage'] = thisvillage
    context['ressurveynum'] = surveynum
    context['reshissanum'] = hissa
    context['resperiod'] = period
    print("Result")
    print(context)
    return render(request,'dependentfiled.html',context)

def getImage(request):
    # data = Owner.objects.all()
    # # context = {
    # #     'data' : data
    # # }
    # context['data'] = data
    return render(request,"displayImage.html", context)