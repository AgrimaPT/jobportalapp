from django.urls import path
from .views import *

urlpatterns=[
    path('',index),
    path('reg/',reg),
    path('log/',log),
    path('seek/',seekers),
    path('edit/<int:id>',edit),

    path('login/',login),
    path('register/',register),
    path('verify/<auth_token>',verify),
    path('send/',send_mail_regis),
    path('comp/',companies),
    path('regisco/',regisco),
    path('postjob/<int:id>',postjob),
    path('viewjob/<int:id>',viewjob),
    path('applyjob/<int:id1>/<int:id2>',applyjob),
    path('applicant/<int:id>',applicant),
    path('applied/<int:id>',applied1)

]