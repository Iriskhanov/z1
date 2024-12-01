from rest_framework.viewsets import ModelViewSet
from property.models import Property
from property.api.serializers import PropertySerializer

class PropertyViewSet(ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
