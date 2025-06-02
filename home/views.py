from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Blog
from .models import Comments
def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username = email).exists():
            messages.error(request,'user already exists')
            return redirect('register')
        else:
            user = User.objects.create_user(username=email, email=email, password=password)
            user.first_name = firstname
            user.save()
            return redirect('login')
    return render(request, 'signup.html')

def user_log(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('landing')
        else:
            messages.error(request,'Invalid Crednetials')
            return redirect('login')
    return render(request, 'login.html')
def user_logout(request):
    logout(request)
    return redirect('landing')
def upload_blogs(request):
    if request.method == 'POST':
        title = request.POST.get('title')        
        desc = request.POST.get('desc')    
        author = request.POST.get('author')  
        published = request.POST.get('published')  
        file = request.FILES['file']
        blog = Blog.objects.create(
            title = title,
            desc = desc,
            author = author,
            published = published,
            file = file,
            user = request.user,
            )
        
        return redirect('landing')
    return render(request,'uploadBlog.html')
def view_blogs(request,id):
    blogs = Blog.objects.get(id = id)
    opinion = Comments.objects.filter(blog_id = id).order_by('created_at')
    context = {'blog':blogs, 'opinions': opinion}
    return render(request,'viewBlog.html',context)
def update_blogs(request,id):
    blogs = Blog.objects.get(id = id)
    context = {'blog':blogs}
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        author = request.POST.get('author')
        published = request.POST.get('published')
        blogs.title = title
        blogs.desc = desc
        blogs.author = author
        blogs.published = published
        if 'file' in request.FILES:
            blogs.file = request.FILES['file']
        blogs.save()
        return redirect('landing')
    return render(request,'updateBlog.html',context)
def delete_blogs(request,id):
    blogs = Blog.objects.get(id = id)
    blogs.delete()
    return redirect('landing')
def landing(request):
    blogs = Blog.objects.all()
    context = {'blog':blogs,'is_landing': True}
    return render(request,'landing.html',context)
def comments(request,id):
    if request.method == 'POST':
        blog = Blog.objects.get(id = id)
        name = request.POST.get('name')
        email = request.POST.get('email')
        comments = request.POST.get('comments')
        Comments.objects.create(
            name = name,
            email = email,
            comments = comments,
            blog = blog
        )
        return redirect('view_blogs',id=id)
    return render(request,'viewBlog.html')