from rest_framework.decorators import api_view, authentication_classes, pagination_class, throttle_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.throttling import AnonRateThrottle
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from .models import User_details
from .serializers import User_Detail_Serializer
from rest_framework import status

# Custom Pagination class
class CustomPagination(PageNumberPagination):
    page_size = 10  # Set the number of items per page as needed
    page_size_query_param = 'page_size'
    max_page_size = 100

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes([SessionAuthentication])
@pagination_class([CustomPagination])  # Add pagination
@throttle_classes([AnonRateThrottle])  # Add AnonRateThrottle
def user_management(request, pk=None):
    if request.method == "GET":
        if pk is not None:
            try:
                user = User_details.objects.get(pk=pk)
                serializer = User_Detail_Serializer(user)
                return Response(serializer.data)
            except User_details.DoesNotExist:
                return Response({"msg": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        users = User_details.objects.all()
        serializer = User_Detail_Serializer(users, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = User_Detail_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': "Data Created"})
        return Response(serializer.errors)

    if request.method == "PUT":
        try:
            id = int(request.data.get('id'))
            user = User_details.objects.get(pk=id)
            serializer = User_Detail_Serializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg': "Data Updated"})
            return Response(serializer.errors)
        except (ValueError, User_details.DoesNotExist):
            return Response({"msg": "Data Not Found or Invalid ID"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        try:
            id = int(request.data.get('id'))
            user = User_details.objects.get(pk=id)
            user.delete()
            return Response({"msg": "Data Deleted"})
        except (ValueError, User_details.DoesNotExist):
            return Response({"msg": "Data Not Found or Invalid ID"}, status=status.HTTP_404_NOT_FOUND)
