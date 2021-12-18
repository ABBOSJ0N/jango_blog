from django.shortcuts import render,redirect
from .models import Post

# # Create your views here.
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse('<h1>Blog home</h1>')

# def about(request):
#     return HttpResponse('<h1>Blog About</h1>')
# posts =[
#     {
#         'author':'Abbos',
#         'title':'Blog post 1',
#         'content':'Birinchi postning matni',
#         'date_posted':'Dekabr 9, 2021'

#     },
#     {
#         'author':'Abbos',
#         'title':'Blog post 1',
#         'content':'Birinchi postning matni',
#         'date_posted':'Dekabr 11, 2021'

#     },
    
# ]

def home(request):
    context={'posts':Post.objects.all()}
    return render(request, 'home.html', context)
def about(request):
    return render(request, 'about.html', {'title':'About'})

