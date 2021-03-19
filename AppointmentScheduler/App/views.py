from django.shortcuts import render
from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient

client = FaunaClient(secret="fnAEEpXoUEACANrA9kCkDGRnaTM0De2OHmQMFgVS")

indexes = client.query(q.paginate(q.indexes()))

def login(request):
 return render(request,"login.html")

def create_appointment(request):
 return render(request,"appoint/create-appointment.html")



def dashboard(request):
 return render(request,"index.html")


def today_appointment(request):
 return render(request,"today-appointment.html")


def all_appointment(request):
 return render(request,"all-appointment.html")

def register(request):
 return render(request,"register.html")
