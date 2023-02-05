from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .pdf import html2pdf
from .models import Person
from django.db import connection, reset_queries
import psycopg2
from django.shortcuts import render
import asyncio
import fuzzywuzzy
from fuzzywuzzy import fuzz
import psycopg2
from .models import Person
from django.db import connection

# Create your views here.
def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if(request.method == 'POST'):
            username = request.POST.get('username')
            password = request.POST.get('password')
                
            user = authenticate(request, username=username, password=password)
            if user is not None: 
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Username or password error")
    context = {}
    return render(request, 'loginpage.html', context)
def logoutuser(request):
     logout(request)
     return redirect("login")
def loginhelp(request):

        context = {}
        return render(request, 'loginhelp.html', context)

@login_required(login_url='login/login')
def home(request):
     context = {}
     return render(request, 'home.html', context)
def search(request):
      context = {}
      return render(request, 'search.html', context)
def fingerprint(request):
      context = {}
      return render(request, 'fingerprint.html', context)
def userguide(request):
      context = {}
      return render(request, 'userguide.html', context)



async def fuzzy_name_search(names, query):
    async def check_name(name):
        return fuzz.token_sort_ratio(name, query)

    checks = [asyncio.ensure_future(check_name(name)) for name in names]
    results = await asyncio.gather(*checks)

    return [names[i] for i, score in enumerate(results) if score >= 72]

def search(request):
    if request.method == 'POST':
        query = request.POST['query']
        
        names = []

        # conn = psycopg2.connect(
        #         host="kspone.postgres.database.azure.com",
        #         database="police",
        #         user="mykspadmin",
        #         password="PoliceHackathon123",
        #         port='5432')
        with connection.cursor() as curr:
            curr.execute("SELECT person_name from icjs union select person_name from ksp where person_name is not null;")
            names=curr.fetchall()
       
        names=[i[0] for i in names]

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        result = loop.run_until_complete(fuzzy_name_search(names, query))
        return render(request, 'search.html',  {'result': result})

    return render(request, 'search.html')


def pdf(request):
     pdf = html2pdf("search.html")
     return HttpResponse(pdf, content_type="application/pdf")