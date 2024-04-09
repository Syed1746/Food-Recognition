from django.shortcuts import render
import json
import requests

def home(request):
    if request.method == 'POST':
        query = request.POST.get('query', '')
        if query:
            try:
                api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
                headers = {'X-Api-Key': 'qSC5rcyPAZLooTU5Biea4A==IINGAnyLYqLNrSOA'}
                api_request = requests.get(api_url + query, headers=headers)
                api_response = api_request.json()
                return render(request, 'service2.html', {'api': api_response})
            except requests.RequestException as e:
                error_message = f"Request to external API failed: {str(e)}"
                return render(request, 'service2.html', {'error': error_message})
            except json.JSONDecodeError as e:
                error_message = f"Failed to parse JSON response: {str(e)}"
                return render(request, 'service2.html', {'error': error_message})
        else:
            return render(request, 'service2.html', {'error': 'Enter a valid query'})
    else:
        return render(request, 'service2.html', {'query': 'Enter a query'})
