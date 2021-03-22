from django.shortcuts import render


def home(request):
# pk_bdcd2f6f2976438383fade06ae364594
  import requests
  import json

  api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_bdcd2f6f2976438383fade06ae364594")

  try:
    api = json.loads(api_request.content)
  except Exception as e:
    api = "Error..."


  return render(request, 'home.html', {'api': api})

def about(request):
  return render(request, 'about.html', {})