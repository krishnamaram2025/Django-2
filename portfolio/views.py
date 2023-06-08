from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .db_operations import retrieve_records, create_record

def skills(request):
    create_record()
    records = retrieve_records()
    print(records)
    # return HttpResponse(records)
    return JsonResponse(records, safe=False)