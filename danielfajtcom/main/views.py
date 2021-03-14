from django.shortcuts import render
import requests
import json
from . import models
from datetime import datetime


def index(request):

    quote_of_the_day = models.DailyQuoteModel

    try:
        # Request quote for a current day from the database
        quote_of_the_day = models.DailyQuoteModel.objects.filter(created_at__day=datetime.utcnow().day)[:1].get()
    except quote_of_the_day.DoesNotExist or None:
        # If there is no quote for today yet, request external API (limit: 10 requests/hour)
        quote_of_the_day_api_query = requests.get('https://quotes.rest/qod?categories=inspire')
        quote_of_the_day_serialized = json.loads(quote_of_the_day_api_query.text)

        quote_of_the_day = models.DailyQuoteModel(
            quote=quote_of_the_day_serialized['contents']['quotes'][0]['quote'],
            author=quote_of_the_day_serialized['contents']['quotes'][0]['author'],
            permalink=quote_of_the_day_serialized['contents']['quotes'][0]['permalink'],
            quote_id=quote_of_the_day_serialized['contents']['quotes'][0]['id'],
            copyright=quote_of_the_day_serialized['copyright']['url']
        )
        quote_of_the_day.save()
    except Exception as e:
        print('error getting quote of the day', e)
        quote_of_the_day = None

    context = {
        'quote_of_the_day': quote_of_the_day,
    }
    return render(request, 'base/index.html', context)
