from django import forms

class regform(forms.Form):
    name=forms.CharField(max_length=20)
    email=forms.EmailField()
    no=forms.CharField(max_length=20)
    dob=forms.CharField(max_length=20)
    edu=forms.CharField(max_length=20)
    pas=forms.CharField(max_length=20)
    con=forms.CharField(max_length=20)

class logform(forms.Form):
    email=forms.EmailField()
    pas=forms.CharField(max_length=20)

class regcompform(forms.Form):
    email=forms.EmailField()
    pas=forms.CharField(max_length=20)
    con=forms.CharField(max_length=20)

class logcompform(forms.Form):
    email=forms.EmailField()
    pas=forms.CharField(max_length=20)

class postjobform(forms.Form):
    cname=forms.CharField(max_length=20)
    email=forms.EmailField()
    title=forms.CharField(max_length=20)
    wtype=forms.CharField(max_length=20)
    exp=forms.CharField(max_length=20)
    jtype=forms.CharField(max_length=20)

class applyjobform1(forms.Form):
    cname=forms.CharField(max_length=20)
    desg=forms.CharField(max_length=20)
    name=forms.CharField(max_length=20)
    email=forms.EmailField()
    quali=forms.CharField(max_length=20)
    phone=forms.CharField(max_length=20)
    exp=forms.CharField(max_length=20)
    rsm=forms.FileField()
