from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from usermanagement.models import UserManagementModel
from usermanagement.serializers import UserManagementSerializer

@csrf_exempt
def usermanagementApi(request, id=0):
    if request.method == 'GET':
        if id:
            try:
                user = UserManagementModel.objects.get(userid=id)
                user_serializer = UserManagementSerializer(user)
                return JsonResponse(user_serializer.data)
            except UserManagementModel.DoesNotExist:
                return JsonResponse({"error": "user not found"}, status=404)
        else:
            users = UserManagementModel.objects.all()
            users_serializer = UserManagementSerializer(users, many=True)
            return JsonResponse(users_serializer.data, safe=False)