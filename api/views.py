from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from Funds.models import wikiPagesModel
from api.serializers import WikiSerializer


class WikiDetail(APIView):
    def get(self, request):
        word = get_object_or_404(wikiPagesModel)
        data = WikiSerializer(word).data
        return Response(data)
