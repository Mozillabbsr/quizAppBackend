from django.contrib.auth.decorators import login_required
from django.shortcuts import render
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
        #print("*******************************************sssss***************************"+str(user))
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


@csrf_exempt
def createQiuz(request):

    #Qid, Qname, Privacy, Uid

    if request.method == "POST":

        Privacy = request.GET['privacy']
        Qname = request.GET['qname']
        Uid = request.GET['uid']
        try:
            UidObj = UserDetail.objects.get(Uid=Uid)

            quiz = Quiz(Qname=Qname,Privacy=Privacy,Uid=UidObj)
            quiz.save()
            msg = "success"
            context = {'msg': msg}

        except:

            msg = "user_not_valid"
            context = {'msg': msg}

        return JsonResponse(context)

    else :
        msg = "failed"
        context = {'msg': msg}

        return JsonResponse(context)

