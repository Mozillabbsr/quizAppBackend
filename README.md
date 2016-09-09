# Quiz App Backend
To construct the quiz App backend API

#Api Docs  

##Register
Method : POST

#####Endpoint: 
127.0.0.1:8000/register/

#####Params:

mobile    = 89845****5

password  = password

name      = Prashant Kumar

mail      = mail@gmail.com


#####Json Response

Success :
```json
{ 
  "msg": "success",
}
```

Failed : 
```json
{ 
  "msg": "failed",
}
```

##Login
Method : POST

#####Endpoint 
127.0.0.1:8000/login/

#####Params 
username  = JohnSnow@gmail.com

password  = GOT

#####Json Response

Success
```json
{ 
  "msg": "success",
  "mobile": 9898989898, 
  "uid": "JohnSnow@gmail.com"
  "session_key" : some hashed key
}
```
Failed  
```json
{ 
  "msg": "failed",
}
```

###Crate Quiz

Method : POST

#####Endpoint 
127.0.0.1:8000/create_quiz/

#####Params 
qname
privacy
uid
session_key

#####Json Response

Success
```json
{ 

}
```
Failed  
```json
{ 
  
}
```
