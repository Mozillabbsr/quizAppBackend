from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib import sessions


@csrf_exempt
def register(request):

    if(request.method == 'POST'):

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

        msg = "success"
        context = {'msg': msg}

        return JsonResponse(context)

    msg = "failed"
    context = {'msg':msg}

    return JsonResponse(context)


@csrf_exempt
def login(request):

    if request.method == "POST":


        username = request.GET['username']
        password = request.GET['password']
        user = authenticate(username = username,password = password)

        if user is not None:

            # Successful
            userDetail = UserDetail.objects.get(Uid=user.email)

            mobile = userDetail.Mobile
            email = userDetail.Email

            msg = "success"
            context = {'msg':msg,'mobile':mobile,'uid':email,'seesion_key':request.session.session_key}

        else:

            msg = "failed"
            context = {'msg':msg}
    else:
        msg = "failed"
        context = {'msg':msg}
    return JsonResponse(context)

@csrf_exempt
def logout(request):
    #TODO : Implement logout
    if request.method == "POST":
        uid = request.GET['uid']
        context = {'msg':'success'}
    else:
        context = {'msg':'failed'}
    return JsonResponse(context)


@csrf_exempt
def createQiuz(request):

    #Qid, Qname, Privacy, Uid

    if request.method == "POST":

        Privacy = request.GET['privacy']
        Qname = request.GET['qname']
        Uid = request.GET['uid']

        if request.session.session_key != request.GET['session_key']:
            context = {'msg':'failed'}
            return JsonResponse(context)

        try:
           UidObj = UserDetail.objects.get(Uid=Uid)
           quiz = Quiz(Qname=Qname,Privacy=Privacy,Uid=UidObj)
           quiz.save()
           qid = quiz.Qid
           msg = "success"
           context = {'msg': msg, 'qid':qid}

        except:
            msg = "user_not_valid"
            context = {'msg': msg}
    else :
        msg = "failed"
        context = {'msg':msg}

    return JsonResponse(context)

def create_question(request):

    if request.method == "POST":
        pass



    return JsonResponse()

