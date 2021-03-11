from django.shortcuts import render
import requests
import json
from . import models
from datetime import datetime
import base64


def index(request):
    """
    Get Quote from external API and save it to the database.
    First, try load that quote from DB, because there is 10 requests per hour limitation on external API.
    """
    quote_of_the_day = models.DailyQuoteModel
    bg_of_the_day = models.DailyBackgroundModel

    try:
        quote_of_the_day = models.DailyQuoteModel.objects.filter(created_at__day=datetime.utcnow().day)[:1].get()
    except quote_of_the_day.DoesNotExist or None:
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

    try:
        bg_of_the_day = models.DailyBackgroundModel.objects.filter(created_at__day=datetime.utcnow().day)[:1].get()
    except bg_of_the_day.DoesNotExist:
        bg_of_the_day = requests.get('https://picsum.photos/1200/800.jpg', stream=True)
        bg_of_the_day_id = bg_of_the_day.headers['Picsum-Id']
        bg_of_the_day_metadata = requests.get(f'https://picsum.photos/id/{bg_of_the_day_id}/info')
        bg_of_the_day_metadata_serialized = json.loads(bg_of_the_day_metadata.text)

        bg_of_the_day = models.DailyBackgroundModel(
            bg_id=bg_of_the_day_id,
            bg_author=bg_of_the_day_metadata_serialized['author'],
            bg_url=bg_of_the_day_metadata_serialized['url'],
            bg_str_b64=base64.b64encode(bg_of_the_day.content).decode()
        )
        bg_of_the_day.save()
    except Exception as e:
        print('error getting background image', e)
        bg_of_the_day = None

    context = {
        'quote_of_the_day': quote_of_the_day,
        'bg_of_the_day': bg_of_the_day
    }
    return render(request, 'base/index.html', context)
