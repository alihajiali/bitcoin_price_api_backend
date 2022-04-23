from rest_framework.views import APIView
from rest_framework.response import Response
from pysondb import db
import datetime

a=db.getDb("./database.json")

class ShowData(APIView):
    def get(self, requests):
        result = a.getAll()
        result = result[:-102:-1]
        return Response(result[::-1])