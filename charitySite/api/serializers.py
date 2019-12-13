from rest_framework.serializers import ModelSerializer

from Funds.models import wikiPagesModel


class WikiSerializer(ModelSerializer):
    class Meta:
        model = wikiPagesModel
        fields = '__all__'
