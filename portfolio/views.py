from django.shortcuts import render
from django.http import HttpResponse
from .db_operations import retrieve_records

def skills(request):
    records = retrieve_records()
    print(records)
    return HttpResponse(records)