import requests
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from thunes.APIAccessGrant import APIAccessGrant


from django.db.models import Q

from .models import Transaction, CreditPartyIdentity
from .serializers import TransactionSerializer

from sender.models import Sender
from beneficiary.models import Beneficiary


# Create your views here.


class TransactionListView(generics.ListAPIView):
    """
    the api for listing all transactions entities
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionCreateView(APIView):
    """
    the api for creating an transaction entity based on the quotation entity
    """

    def post(self, request, quotation_id, *args, **kwargs):
        APIObject = APIAccessGrant('/quotations/' + str(quotation_id) + '/transactions')
        apiprams = APIObject.parmReturn()

        # print(request.data)
        self.transactioncreate(request.data)

        response = requests.post(apiprams['urlparm'], headers={
            'X-TransferTo-apikey': apiprams['apikey'],
            'X-TransferTo-nonce': apiprams['nonce'],
            'X-TransferTo-hmac': apiprams['hmac'],
            'Date': apiprams['date'],
            'Content-Type': 'application/json',
        }, json=request.data)
        return Response(response.json())

    def transactioncreate(self, data):
        """
        the function for creating the transaction entity
        """
        try:
            transactionentity = Transaction.objects.get(external_id=data['external_id'])
        except Transaction.DoesNotExist:
            senderentity = self.sendercreate(data['sender'])
            beneficiaryentity = self.beneficiarycreate(data['beneficiary'])
            self.creditpartyidentity(data['credit_party_identifier'])
            transactionentity = Transaction.objects.create(
                sender=senderentity,
                beneficiary=beneficiaryentity,
                external_id=data['external_id'],
                retail_fee_currency=data['retail_fee_currency'],
                purpose_of_remittance=data['purpose_of_remittance'],
                # retail_fee=data['retail_fee']
            )

    def sendercreate(self, senderdata):
        """
        the function for creating the sender entity
        """
        try:
            senderentity = Sender.objects.get(lastname=senderdata['lastname'], firstname=senderdata['firstname'])
            return senderentity
        except Sender.DoesNotExist:
            senderentity = Sender.objects.create(
                lastname=senderdata['lastname'],
                firstname=senderdata['firstname'],
                nationality_country_iso_code=senderdata['nationality_country_iso_code'],
                date_of_birth=senderdata['date_of_birth'],
                country_of_birth_iso_code=senderdata['country_of_birth_iso_code'],
                gender=senderdata['gender'],
                address=senderdata['address'],
                postal_code=senderdata['postal_code'],
                city=senderdata['city'],
                country_iso_code=senderdata['country_iso_code'],
                msisdn=senderdata['msisdn'],
                email=senderdata['email'],
                id_type=senderdata['id_type'],
                id_number=senderdata['id_number'],
                id_delivery_date=senderdata['id_delivery_date'],
                occupation=senderdata['occupation']
            )
        return senderentity

    def beneficiarycreate(self, beneficiarydata):
        """
        the function for creating the beneficiary entity
        """
        try:
            beneficiaryentity = Beneficiary.objects.get(lastname=beneficiarydata['lastname'],
                                                        firstname=beneficiarydata['firstname'])
            return beneficiaryentity
        except Beneficiary.DoesNotExist:
            beneficiaryentity = Beneficiary.objects.create(
                lastname=beneficiarydata['lastname'],
                firstname=beneficiarydata['firstname'],
                nationality_country_iso_code=beneficiarydata['nationality_country_iso_code'],
                date_of_birth=beneficiarydata['date_of_birth'],
                country_of_birth_iso_code=beneficiarydata['country_of_birth_iso_code'],
                gender=beneficiarydata['gender'],
                address=beneficiarydata['address'],
                postal_code=beneficiarydata['postal_code'],
                city=beneficiarydata['city'],
                country_iso_code=beneficiarydata['country_iso_code'],
                msisdn=beneficiarydata['msisdn'],
                email=beneficiarydata['email'],
                id_type=beneficiarydata['id_type'],
                id_number=beneficiarydata['id_number'],
                occupation=beneficiarydata['occupation']
            )
        return beneficiaryentity

    def creditpartyidentity(self, creditdata):
        """
         the function for creating the credit party identity entity
        """
        try:
            creditentity = CreditPartyIdentity.objects.get(
                msisdn=creditdata['msisdn'],
                bank_account_number=creditdata['bank_account_number'],
                swift_bic_code=creditdata['swift_bic_code']
            )
        except CreditPartyIdentity.DoesNotExist:
            creditentity = CreditPartyIdentity.objects.create(
                msisdn=creditdata['msisdn'],
                bank_account_number=creditdata['bank_account_number'],
                swift_bic_code=creditdata['swift_bic_code']
            )


class TransactionConfirmView(APIView):
    """
    the api for confirming the transaction has been created.
    """

    def post(self, request, transaction_id, *args, **kwargs):
        APIObject = APIAccessGrant('/transactions/' + str(transaction_id) + '/confirm')
        apiprams = APIObject.parmReturn()

        # print(request.data)
        # self.transactioncreate(request.data)
        # self.transactioncreate(request.data)

        response = requests.post(apiprams['urlparm'], headers={
            'X-TransferTo-apikey': apiprams['apikey'],
            'X-TransferTo-nonce': apiprams['nonce'],
            'X-TransferTo-hmac': apiprams['hmac'],
            'Date': apiprams['date'],
            'Content-Type': 'application/json',
        }, json=request.data)
        return Response(response.json())


class TransactionDetailRetrieveView(generics.RetrieveAPIView):
    """
    the api for showing the transactoin entity detail
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TransactionDetailUpdateView(generics.UpdateAPIView):
    """
    the api for updating the transaction entity detail
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class BeneficiaryListBySenderName(generics.RetrieveAPIView):
    """
    the api for showing Beneficiary based on the given sender name
    """
    beneficiary_list = {}
    beneficiary_list_result = []

    def get(self, request, *args, **kwargs):
        lastname = self.request.GET.get('lastname', None)
        firstname = self.request.GET.get('firstname', None)
        # Add the clear function to not create too much memory space for these two para
        self.beneficiary_list.clear()
        self.beneficiary_list_result.clear()

        if lastname is None and firstname is None:
            pass
        elif lastname is None or firstname is None:
            pass
        else:
            senderentity = self.getsenderentity(lastname, firstname)
            beneficiaryentities = Transaction.objects.filter(Q(sender=senderentity)).values('beneficiary_id')
            # for loop to get a beneficiary map with beneficiary_id as key and
            # occurancy of this beneficiary as the value
            for beneficiary in beneficiaryentities:
                if beneficiary['beneficiary_id'] in self.beneficiary_list.keys():
                    self.beneficiary_list[beneficiary['beneficiary_id']] += 1
                else:
                    self.beneficiary_list[beneficiary['beneficiary_id']] = 1
            sorted(self.beneficiary_list.values())
            for key in self.beneficiary_list.keys():
                beneficiary_single_entity = self.getbeneficiary(key)
                self.beneficiary_list_result.append({'beneficiary_id': key,
                                                'beneficiary_name': beneficiary_single_entity.__str__(),
                                                'counter': self.beneficiary_list[key]})
        return Response(self.beneficiary_list_result)

    def getsenderentity(self, lastname, firstname):
        """
        the function for get the sender entity by its lastname and firstname
        """
        if firstname is not None and lastname is not None:
            try:
                return Sender.objects.get(firstname=firstname, lastname=lastname)
            except Sender.DoesNotExist:
                return None
        elif firstname is not None:
            try:
                return Sender.objects.get(firstname=firstname)
            except Sender.DoesNotExist:
                return None
        else:
            try:
                return Sender.objects.get(lastname=lastname)
            except Sender.DoesNotExist:
                return None
        return None

    def getbeneficiary(self, pk):
        try:
            return Beneficiary.objects.get(pk=pk)
        except Beneficiary.DoesNotExist:
            return None

