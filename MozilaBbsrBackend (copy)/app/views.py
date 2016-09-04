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
        logged = []
        if user is not None:
            # Successful
            userDetail = UserDetail.objects.get(Uid=user.email)

            mobile = userDetail.Mobile
            email = userDetail.Email

            msg = "success"
            context = {'msg':msg,'mobile':mobile,'uid':email}


            
           '''
            try:
                if request.session['logged'] != None:

                    logged = request.session['logged']
                    logged.append(email)
                    request.session['logged'] = logged
                    print("****************************************************" + str(request.session['logged']))

                else:
                    logged.append(email)
                    request.session['logged'] = logged

            except:
                request.session['logged'] = logged
            '''
            return JsonResponse(context)

        else:

            msg = "failed"
            context = {'msg':msg}
            return JsonResponse(context)

    else:
        msg = "failed"
        context = {'msg':msg}
        return JsonResponse(context)

@csrf_exempt
def logout(request):

    if request.method == "POST":
        uid = request.GET['uid']
        try:
            print("---------------------------------"+str(uid))
            logged = request.session['logged']
            request.session['logged'] = logged.remove(uid)
            print("#####################################" + str(logged))
            print(request.session['logged'])
            context = {'msg':'success'}


        except:
            context = {'msg':'failed'}

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



        try:
            print("***************************************************************" + str(request.session['logged']))

            if Uid in request.session['logged']:

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

                msg = "failed1"
                context = {'msg':msg}

        except:
            msg = "not_logged"
            context = {'msg': msg}

        return JsonResponse(context)

    else :
        msg = "failed2"
        context = {'msg': msg}

        return JsonResponse(context)

