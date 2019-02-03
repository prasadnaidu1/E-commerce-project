from django.shortcuts import render
from PIL import Image
from.models import *
import re
from firebase.firebase import FirebaseApplication
# Create your views here.
def Home(request):
    type=request.GET.get("type")
    c = categeroy.objects.all()
    p = product.objects.all()
    items=len(request.COOKIES)
    return render(request,"INDEX.html",{"product":p,"type":type,"categery":c,"items":items})


def index(request):
    c=categeroy.objects.all()
    p=product.objects.all()
    return render(request,"INDEX.html",{"categery":c,"product":p})

def UserRegistration(request):
    type=request.GET.get("type")
    image=signupImage.objects.all()
    return render(request,"INDEX.html",{"type":type,"image":image})
def UserLogin(request):
    type=request.GET.get("type")
    login_image=LoginImage.objects.all()
    return render(request,"INDEX.html",{"type":type,"login_image":login_image})



def Register(request):
    name=request.POST.get("t1")
    contact=request.POST.get("t2")
    email=request.POST.get("t3")
    username=request.POST.get("t4")
    password=request.POST.get("t5")
    confirm_password=request.POST.get("t6")
    print(password,confirm_password)
    r=RegisterDetails.objects.values("username")
    usernames=[]
    for x in r:
        usernames.append(x["username"])
    if username in usernames:
        return render(request,"INDEX.html",{"type": "productDetails","message":"username already exists"})
    elif len(password)<8 and len(confirm_password)<8:
        return render(request,"INDEX.html",{"type": "productDetails","message":"Your password must br more than 8 characters"})

    elif re.search('[0-9]', password) is None:
        return render(request, "INDEX.html", {"type": "productDetails", "message": "Make sure your password has a digit  in it "})

    elif re.search('[A-Z]', password) is None:
        return render(request, "INDEX.html",
                      {"message": "Make sure your password has a Capital letter in it ","type": "productDetails"})

    elif re.search('[a-z]', password) is None:
        return render(request, {"message": "Make sure your password has a Small letter in it ", "type": "productDetails"})
    elif password != confirm_password:
        return render(request, "INDEX.html", {"type": "productDetails", "message": "Your password did not match"})
    else:
        RegisterDetails(name=name, contact=contact, email=email, username=username, password=password,
                        confirm_password=confirm_password).save()
        c = categeroy.objects.all()
        p = product.objects.all()
        return render(request, "INDEX.html", {"type": "productDetails", "name": name, "product": p, "categery": c})
def Forget(request):
    type=request.GET.get("type")
    return render(request,"INDEX.html",{"type":type})
def ForgetDetails(request):
    username=request.POST.get("p2")
    R=RegisterDetails.objects.filter(username=username)
    if not R:
        return render(request,"INDEX.html",{"type":"forget","message":"Invalid Username"})
    else:
        name=""
        email=""
        contact=""

        for x in R:
            name=x.name
            email=x.email
            contact=x.contact
        return render(request,"INDEX.html",{"type":"newpassword","name":name,"email":email,"contact":contact,"username":username})
def NewPassword(request):
    name=request.POST.get("p1")
    email=request.POST.get("p2")
    print(email)
    contact=request.POST.get("p3")
    username=request.POST.get("p4")
    password=request.POST.get("p5")
    confirm_password=request.POST.get("p6")
    res=RegisterDetails.objects.filter(email=email)
    #.update(name=name,email=email,contact=contact,username=username,#password=password,confirm_password=confirm_password)
    if not res:
        print("not ok")
    else:
        print("ok")

    #return render(request,"INDEX.html",{"type":"newpassword","message":"SuccessFully Changed Your Password"})
def LoginDetails(request):
    username=request.POST.get("p1")
    password=request.POST.get("p2")
    res=RegisterDetails.objects.filter(username=username,password=password)
    if not res:
        return render(request,"INDEX.html",{"type":"userlogin","message":"Invalid Credentials"})
    else:
        request.session["status"]=True
        request.session["name"]=username
        p = product.objects.all()
        c = categeroy.objects.all()
        q=CartItems.objects.filter(name=username)
        items=len(q)
        return render(request,"INDEX.html",{"type":"productDetails","name":username,"product":p,"categery":c,"items":items})
def SearchDetails(request):
    type=request.GET.get("type")
    id=request.GET.get("id")
    p=product.objects.filter(catagory_name=id)
    c=categeroy.objects.all()
    return render(request,"INDEX.html",{"type":type,"categery":c,"product":p})
def ProductDetails(request):
    type=request.GET.get("type")
    id=request.GET.get("id")
    p=product.objects.filter(product_id=id)
    if not p:
        return render(request,"INDEX.html")
    else:
        return render(request,"INDEX.html",{"type":type,"product":p})
def AddTocart(request):
    key=request.GET.get("id")
    p=product.objects.all()
    c=categeroy.objects.all()
    status = request.session["status"]
    name = request.session['name']
    if status:
        CartItems(name=name,p_id=key).save()
        q=CartItems.objects.filter(name=name)
        items=len(q)
        return render(request,"INDEX.html",{"items":items,"name":name,"product":p,"categery":c,"type":"home"})


    else:
        items = len(request.COOKIES)
        print(items)
        response = render(request, "INDEX.html", {"product": p, "categery": c, "items": items,"type":"home"})
        response.set_cookie(key, key)
        return response
def LogOut(request):
    request.session["status"]=False
    request.session["name"]=""
    p=product.objects.all()
    c=categeroy.objects.all()
    return render(request,"INDEX.html", {"product": p, "categery": c,"type":"home"})

def OpenCart(request):
    type=request.GET.get("type")
    name=request.session["name"]
    res=CartItems.objects.filter(name=name)
    p=product.objects.all()
    q = CartItems.objects.filter(name=name)
    items = len(q)
    return render(request,"INDEX.html",{"product":p,"type":type,"res":res,"items":items})
def Remove(request):
    key=request.GET.get("id")
    name=request.session["name"]
    CartItems.objects.filter(p_id=key,name=name).delete()
    res=CartItems.objects.filter(name=name)
    p=product.objects.all()
    # c=categeroy.objects.all()
    # cc=CartItems.objects.all()
    return render(request,"INDEX.html",{"product": p, "res":res,"type":"opencart"})
def ContactUs(request):
    type=request.GET.get("type")

    return render(request,"INDEX.html",{"type":type})
def ContactDetails(request):
    f_name=request.POST.get("c1")
    l_name=request.POST.get("c2")
    email=request.POST.get("c3")
    comment=request.POST.get("c4")
    fire=FirebaseApplication("https://djangoweb1-ec1db.firebaseio.com/",None)
    fire.put("contact","ContactDetails",{"firstname":f_name,"lastname":l_name,"email":email,"comment":comment})
    return  render(request,"INDEX.html",{"type":"contact","message":"Successfully Your FeedBack Given"})



