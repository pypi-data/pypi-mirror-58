import json
import random

import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from thunes.APIAccessGrant import APIAccessGrant

from .models import Quotation, Source, Destination


# Create your views here.


class QuotationDetailView(APIView):
    """
    the api for showing the quotation entity detail by ID
    """
    result_body = {}

    def get(self, request, id, format=None):
        APIObject = APIAccessGrant('/quotations/' + str(id))
        apiprams = APIObject.parmReturn()

        response = requests.get(apiprams['urlparm'], headers={
            'X-TransferTo-apikey': apiprams['apikey'],
            'X-TransferTo-nonce': apiprams['nonce'],
            'X-TransferTo-hmac': apiprams['hmac'],
            'Date': apiprams['date'],
            # 'Content-Type': 'application/json',
        })
        # response_json = response.json()
        # self.result_body['id'] = response_json['id']
        # self.result_body['external_id'] = response_json['external_id']
        # self.result_body['mode'] = response_json['mode']
        # self.result_body['destination'] = response_json['destination']
        # self.result_body['source'] = response_json['source']
        return Response(response.json())


class QuotationCreateView(APIView):
    """
    the api for creating the quotation entity
    """
    quotation_body = {
        "external_id": "148118432398",
        "payer_id": "1669",
        "mode": "SOURCE_AMOUNT",
        "source": {
            "amount": 10,
            "country_iso_code": "SGP",
            "currency": "SGD"
        },
        "destination": {
            "amount": None,
            "currency": "GHS"
        }
    }

    def post(self, request, *args, **kwargs):
        # import random to generate different external id
        self.quotation_body['external_id'] = str(148118432398 + random.randint(0, 10000000000))
        APIObject = APIAccessGrant('/quotations/')
        apiprams = APIObject.parmReturn()

        # the method to get the key
        (response_body, value), = request.data.items()

        self.quotation_body['source'] = json.loads(response_body)['source']
        self.quotation_body['destination'] = json.loads(response_body)['destination']

        # Enable this function to store the quotation data
        # self.createquotationentity(request.data)

        response = requests.post(apiprams['urlparm'], headers={
            'X-TransferTo-apikey': apiprams['apikey'],
            'X-TransferTo-nonce': apiprams['nonce'],
            'X-TransferTo-hmac': apiprams['hmac'],
            'Date': apiprams['date'],
            'Content-Type': 'application/json',
        }, json=self.quotation_body)
        return Response(response.json())

    def createquotationentity(self, data):
        try:
            quotationentity = Quotation.objects.get(external_id=data['external_id'])
        except Quotation.DoesNotExist:
            sourceentity = Source.objects.create(
                country_iso_code=data['source']['country_iso_code'],
                currency=data['source']['currency'],
                amount=data['source']['amount']
            )
            destinationentity = Destination.objects.create(
                currency=data['destination']['currency'],
                amount=data['destination']['amount']
            )
            quotationentity = Quotation.objects.create(
                external_id=data['external_id'],
                payer_id=data['payer_id'],
                mode=data['mode'],
                source=sourceentity,
                destination=destinationentity
            )


class ServerPing(APIView):

    def get(self, request, format=None):
        """
        the function to test the backend API's connectivity
        """
        APIObject = APIAccessGrant('')
        apiprams = APIObject.parmReturn()

        pingUrl = apiprams['urlparm'].replace('v1/money-transfer', 'ping')

        # Enable this function to store the quotation data
        # self.createquotationentity(request.data)

        response = requests.get(pingUrl, headers={
            'X-TransferTo-apikey': apiprams['apikey'],
            'X-TransferTo-nonce': apiprams['nonce'],
            'X-TransferTo-hmac': apiprams['hmac'],
            'Date': apiprams['date'],
        })
        return Response(response.json())

