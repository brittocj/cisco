from rest_framework.response import Response
from rest_framework.views import APIView
import requests as rq


class DemoAPIGet(APIView):
    """Demo API for CISCO"""
    def get(self, request, format=None):
        """ Static output for a get request """
        data = {"Receiver": "Cisco is the best!"}
        return Response(data)

class DemoAPIPost(APIView):
    """Demo API for CISCO"""
    def post(self, request, format=None):
        """ Dynamic output for a post request """
        url_from_request = request.data.get("url")
        if url_from_request == None:
            return Response("Url is missing in request.")
        final_url_response = rq.get(url_from_request).text
        return Response(final_url_response)


# Improvisation on assignment

from django.shortcuts import render

def index(request):
    return render(request, "index.html")
