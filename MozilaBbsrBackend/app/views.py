from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Questions
from .serializers import QuestionsSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .models import *
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import authenticate

@csrf_exempt
def register(request):

    if(request.method == 'POST'):

        #print("===========================",request.POST)
        email = request.GET['mail']


        name = request.GET['name']
        password = request.GET['password']
        mobile = request.GET['mobile']

        try:
            user = User.objects.create_user(email, email, password)
            user.first_name = name
            user.save()
        except:
            msg = "Already Exist"
            context = {'msg': msg}
            return JsonResponse(context)

        userDetails = UserDetail(Mobile=mobile,Uid=user.email,Name=name,Email=email)
        userDetails.save()

        msg = "Success"
        context = {'msg': msg}

        return JsonResponse(context)


    msg = "Error"
    context = {'msg':msg}

    return JsonResponse(context)


@csrf_exempt
def login(request):



    if request.method == "POST":

        username = request.GET['username']
        password = request.GET['password']
        user = authenticate(username = username,password = password)
        print("*******************************************sssss***************************"+str(user))
        if user is not None:
            # Successful
            userDetail = UserDetail.objects.get(Uid=user.email)

            mobile = userDetail.Mobile
            email = userDetail.Email

            msg = "true"
            context = {'msg':msg,'mobile':mobile,'email':email}
            return JsonResponse(context)


        else:
            msg = "false"
            context = {'msg':msg}
            return JsonResponse(context)

    else:
        msg = "false_get"
        context = {'msg':msg}
        return JsonResponse(context)