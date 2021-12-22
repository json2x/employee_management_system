from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Location
import json

def get_provinces(request):
    try:
        provinces = Location.lists.provinces()
        province_list = [{'name': province['province']} for province in provinces]
        data = {
            'success': True,
            'provinces': province_list,
            'length': len(provinces)
        }
        return JsonResponse(data)
    except:
        data = {
            'success': False
        }
        return JsonResponse(data)

def get_citymuni(request, province=None):
    try:
        citimunis = Location.lists.citymuni(province)
        citymuni_list = [{'name': citymuni['city_muni']} for citymuni in citimunis]
        data = {
            'success': True,
            'provinces': citymuni_list,
            'length': len(citymuni_list)
        }
        return JsonResponse(data)
    except:
        data = {
            'success': False
        }
        return JsonResponse(data)