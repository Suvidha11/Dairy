from django.shortcuts import render,HttpResponse,redirect
from  django.contrib.auth.models import User
from .models import memo,comments
from django.contrib.auth.decorators import login_required



#create postS
def add_post(request):
      if request.method == 'POST':
          id1 = request.session['user_id']
          title= request.POST['title']
          desc= request.POST['desc']
          image= request.FILES['image']
          Privcy=request.POST['Privcy']     
          add=memo.objects.create(title=title,desc=desc,image=image,user = User(id = id1),Privcy=Privcy)
          return redirect('home')
      else:     
          return render(request,"post.html")
# home page
# @login_required(login_url="user_login")

def home(request):
    # view_cmnt=comments.objects.filter(post__user= request.session['user_id']).count()
    total=comments.objects.filter(post__user=request.session['user_id']).count()
   
    disp=memo.objects.filter(Privcy='Public')
    return render(request,'index.html',{'disp':disp})

def your_post(request):
    get_user_id = request.session['user_id']
    disp=memo.objects.filter(user=get_user_id)
    return render(request,'your_post.html',{'disp':disp})

#delete post
def del_post(request,id):
    delt=memo.objects.get(post_id = id).delete()
    return redirect('your_post')

# update user post
def Update_post(request,id):
    update=memo.objects.get(post_id = id)
    if request.method == 'POST':
      title= request.POST['title']
      desc= request.POST['desc']
      image= request.FILES['image']
      Privcy=request.POST['Privcy']
      
      update.title = title
      update.desc = desc
      update.image = image
      update.Privcy=Privcy
      update.save()
      return redirect('your_post')
    else:
     return render(request,"update.html",{'update_data':update})
    

# display comments and user_b post
def display (request,id):
    disp=memo.objects.get(post_id=id)
    
    # add and view comments
    view_cmnt=comments.objects.filter(post=id)
    count = view_cmnt.count()
    if request.method=='POST':
        cmnt=request.POST['comments']   
        #save comments
        add_cmnt=comments.objects.create(post=memo(post_id=id) ,comment=cmnt, comment_by = User(id = request.session['user_id']))
    return render(request,'display.html',{'disp':disp,'view_cmnt':view_cmnt, 'count':count})


 