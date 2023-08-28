from django.http import HttpResponse
from django.shortcuts import render

data = {
    'movies':[
        {
            'id':1,
            'title':"valorent",
            'year':2021


        },
        {
            'id':2,
            'title':"CS Go",
            'year':2020

        },
        {
            'id':3,
            'title':"Fortnite",
            'year':2020

        }
    ]
}

def Home(request):
    return HttpResponse("<h1>This is supposed to be a home page<h1/><a href = 'http://127.0.0.1:8000/movies'>click and go to movies page</a>")

def movies(request):
    return render(request,'movies/movies.html',data)
    