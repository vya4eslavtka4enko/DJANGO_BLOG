from datetime import date

from django.shortcuts import render

all_posts = [
    {
    "slug":"hike-in-the-mountains",
    "image":"mountains.webp",
    "author":"Viacheslav",
    "date":date(2022,7,21),
    "title":"Mountain Hiking",
    "excerpt":"There's nothing like the views you get when hiking in the mountain",
    "content":"""
        Hiking It is a long established fact that a reader will be distracted by the readable content of a page when 
        looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution 
        of letters, as opposed to using 'Content here, content here', making it look like readable English. Many
        desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a 
        search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions 
        have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).
    """
    },
    {
    "slug":"programing",
    "image":"coding.webp",
    "author":"Viacheslav",
    "date":date(2021,7,30),
    "title":"Programming",
    "excerpt":"There's nothing like the views you get when hiking in the mountain",
    "content":"""
        Programming It is a long established fact that a reader will be distracted by the readable content of a page when 
        looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution 
        of letters, as opposed to using 'Content here, content here', making it look like readable English. Many
        desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a 
        search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions 
        have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).
    """
    },
     {
    "slug":"woods",
    "image":"woods.jpeg",
    "author":"Viacheslav",
    "date":date(2021,8,2),
    "title":"Run",
    "excerpt":"There's nothing like the views you get when hiking in the mountain",
    "content":"""
        Woods It is a long established fact that a reader will be distracted by the readable content of a page when 
        looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution 
        of letters, as opposed to using 'Content here, content here', making it look like readable English. Many
        desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a 
        search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions 
        have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).
    """
    },
    
]

def get_date(post):
    return post['date']

# Create your views here.
def starting_page(request):
    sorted_posts = sorted(all_posts, key = get_date)
    latest_posts = sorted_posts[-3:]
    return render(request,"blog/index.html",{
        "posts":latest_posts
    })

def posts(request):
    return render(request,'blog/all-posts.html',{
        "all_posts":all_posts
    })

def post_detail(request,slug):
    identified_post = next(post for post in all_posts if post['slug']==slug)
    return render(request,"blog/post_detail.html",
                  {
                      "post":identified_post
                  })