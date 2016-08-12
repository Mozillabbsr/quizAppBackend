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

