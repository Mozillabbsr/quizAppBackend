# Quiz App Backend
To construct the quiz App backend API

#Api Docs  

##Register
Method : POST

Endpoint: 
127.0.0.1:8000/register/

Params:

mobile    = 89845****5 
password  = password 
name      = Prashant Kumar 
mail      = mail@gmail.com

Json Response

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

Endpoint 
127.0.0.1:8000/login/

Params 
username  = JohnSnow@gmail.com 
password  = GOT

Json Response

Success
```json
{ 
  "msg": "success",
  "mobile": 9898989898, 
  "email": " JohnSnow@gmail.com"
}
```
Failed  
```json
{ 
  "msg": "failed",
}
```
