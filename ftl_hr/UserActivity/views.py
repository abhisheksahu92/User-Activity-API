# 3-rd party packages
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Project packages
from .models import User
from .serializers import UserSerializers

# Get the list of all user and their activity
@api_view(['GET'])
def useractivity(request):
    try:
        user = User.objects.all()
        serial = UserSerializers(user, many=True)
        returned_json_response = {"ok": 'true',"members": serial.data}
        return Response(returned_json_response,status=status.HTTP_200_OK)
    except Exception as e:
        print(f'Serializer error: {e}')

