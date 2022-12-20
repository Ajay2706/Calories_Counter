from django.shortcuts import render
from django.http import HttpResponse


# 8YZzguovP6DxosrbuUYToA==b40W4jbYB1DUvtGY

# Create your views here.
def home(request):
    import json
    import requests
    query = request.POST.get('query')
    api_url = "https://api.api-ninjas.com/v1/nutrition?query={}".format(query)
    api_request = requests.get(api_url, headers={'X-Api-Key': '8YZzguovP6DxosrbuUYToA==b40W4jbYB1DUvtGY'})
    api = json.loads(api_request.content)
    return render(request, 'index.html', {"api": api})