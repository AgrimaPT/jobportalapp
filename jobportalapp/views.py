from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.http import HttpResponse

from jobportal.settings import EMAIL_HOST_USER
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate
import uuid
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def reg(request):
    if request.method=='POST':
        a=regform(request.POST)
        if a.is_valid():
            nam=a.cleaned_data['name']
            emai=a.cleaned_data['email']
            numb=a.cleaned_data['no']
            dofb=a.cleaned_data['dob']
            educ=a.cleaned_data['edu']
            pwd=a.cleaned_data['pas']
            cpas=a.cleaned_data['con']
            if pwd==cpas:
                b=regmodel(nm=nam,eml=emai,num=numb,bd=dofb,edct=educ,password=pwd)
                b.save()
                return redirect(log)
            else:
                return HttpResponse("password don't match")
        else:
            return HttpResponse("enter valid data")
    return render(request,'register.html')

def log(request):
    if request.method=='POST':
        a=logform(request.POST)
        if a.is_valid():
            em=a.cleaned_data['email']
            pas=a.cleaned_data['pas']
            b=regmodel.objects.all()
            for i in b:
                if em==i.eml and pas==i.password:
                    name=i.nm
                    eml=i.eml
                    mob=i.num
                    dob=i.bd
                    ed=i.edct
                    id1=i.id
                    return render(request,'seekers.html',{'name':name,'eml':eml,'mob':mob,'dob':dob,'ed':ed,'id':id1})
            else:
                return HttpResponse("login failed...")
        else:
            return HttpResponse("enter valid details...")
    return render(request,'log.html')

def seekers(request):
    return render(request,'seekers.html')

def edit(request,id):
    user=regmodel.objects.get(id=id)
    if request.method=='POST':
        user.nm=request.POST.get('name')
        user.eml=request.POST.get('email')
        user.num=request.POST.get('no')
        user.bd=request.POST.get('dob')
        user.edct=request.POST.get('edu')
        user.save()
        return redirect(log)
    return render(request,'edit.html',{'user':user})




def login(request):
    global User
    if request.method=='POST':
        username=request.POST.get('uname')
        pas=request.POST.get('pas')
        user_obj=User.objects.filter(username=username).first()
        
        if user_obj is None:
            messages.success(request,"user not found")
            return redirect(login)
        profile_obj=Companyprofile1.objects.filter(user=user_obj).first()
        if not profile_obj.is_verified:
            messages.success(request,"profile not verified. check ur email.")
            return redirect(login)
        user=authenticate(username=username,password=pas)
        if user is None:
            messages.success(request,"wrong password or username")
            return redirect(login)
        obj=Companyprofile1.objects.filter(user=user) 
        return render(request,'companies.html',{'obj':obj})   
    return render(request,'logcomp.html')

def verify(request,auth_token):
    profile_obj=Companyprofile1.objects.filter(auth_token=auth_token).first()
    if profile_obj:
        if profile_obj.is_verified:
            messages.success(request,"your account already verified")
            redirect(login)
        profile_obj.is_verified=True
        profile_obj.save()
        messages.success(request,'ur account verified')
        return redirect(login)
    else:
        return HttpResponse("error")


def register(request):
    
    if request.method=='POST':
        unm=request.POST.get('uname')
        email=request.POST.get('email')
        pas=request.POST.get('pas')
        if User.objects.filter(username=unm).first():
            messages.success(request,"username already used")
            return redirect(register)
        if User.objects.filter(email=email).first():
            messages.success(request,"email already used")
            return redirect(register)
        user_obj=User(username=unm,email=email)    
        user_obj.set_password(pas)
        user_obj.save()
        auth_token=str(uuid.uuid4())
        profile_obj=Companyprofile1.objects.create(user=user_obj,auth_token=auth_token)
        profile_obj.save()
        send_mail_regis(email,auth_token)
        return HttpResponse("mail send successfully")
    return render(request,'regcomp.html')

def send_mail_regis(email,token):
    subject="your account has been verified"
    message=f'pass the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from=EMAIL_HOST_USER
    recipient=[email]
    send_mail(subject,message,email_from,recipient)

def companies(request):
    
    return render(request,'companies.html')

def regisco(request):
    obj=Companyprofile1.objects.all()
    return render(request,'regisco.html',{'obj':obj})

def postjob(request,id):
    obj=Companyprofile1.objects.get(id=id)
    
    if request.method=='POST':
        a=postjobform(request.POST)
        if a.is_valid():
            name=a.cleaned_data['cname']
            emai=a.cleaned_data['email']
            tit=a.cleaned_data['title']
            wt=a.cleaned_data['wtype']
            ex=a.cleaned_data['exp']
            jt=a.cleaned_data['jtype']
            
            b=postjobmodel1(cnm=name,eml=emai,ttl=tit,wktp=wt,ex=ex,jbtp=jt)
            b.save()
            return HttpResponse("job posted successfully")
    return render(request,'postjob.html',{'obj':obj})

def viewjob(request,id):
    a=postjobmodel1.objects.all()
    user=id
    return render(request,'viewjob.html',{'pj':a,'user':user})

def applyjob(request,id1,id2):
    b=postjobmodel1.objects.get(id=id1)
    c=regmodel.objects.get(id=id2)
    name=c.nm
    email=c.eml
    if request.method=='POST':
        a=applyjobform1(request.POST,request.FILES)
        if a.is_valid():
            cname=a.cleaned_data['cname']
            desg=a.cleaned_data['desg']
            name=a.cleaned_data['name']
            email=a.cleaned_data['email']
            qlf=a.cleaned_data['quali']
            phone=a.cleaned_data['phone']
            exp=a.cleaned_data['exp']
            rsm=a.cleaned_data['rsm']
            
            b=applyjobmodel1(cn=cname,dsg=desg,nm=name,eml=email,qlfn=qlf,phno=phone,ex=exp,cv=rsm)
            b.save()
            return HttpResponse("Applied successfully")
        else:
           return HttpResponse("error") 
    return render(request,'applyjob.html',{'aj':b,'name':name,'email':email})

def applicant(request,id):
    obj=Companyprofile1.objects.get(id=id)
    cnm=obj.user.username
    a=applyjobmodel1.objects.filter(cn=cnm)
    return render(request,'applicant.html',{'ap':a})

# def applied(request,id):
#     obj=regmodel.objects.get(id=id)
#     name=obj.nm
#     a=applyjobmodel1.objects.all()
    
#     cn=[]
#     tt=[]
#     for i in a:
#         if i.nm==name:
#             cn.append(i.nm)
#             c=i.cn
#             # d=i.dsg
#             cn.append(c)
#             # tt.append(d)
#     list=zip(cn)
#     return render(request,'applied.html',{'l':list,'name':name})

# def applied(request,id):
#     obj=regmodel.objects.get(id=id)
#     name=obj.nm
#     a=applyjobmodel1.objects.filter(nm=name)
#     return render(request,'applied.html',{'ap':a})

def applied1(request,id):
    a=regmodel.objects.get(id=id)
    name=a.nm
    b=applyjobmodel1.objects.all()
    d=[]
    f=[]
    for i in b:
        if i.nm == name:
            c=i.cn
            d.append(c)
            e=i.dsg
            f.append(e)
    list=zip(d,f)
    return render(request,'applied.html',{'list':list})



