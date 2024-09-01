from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import get_object_or_404, GenericAPIView
from .models import EIAData, CrudeOil

from .serializers import UserSerializer, TokenObtainPairSerializer, PasswordSerializer, EIADataSerializer, CrudeOilSerializer


class SignUpView(APIView):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            get_user_model().objects.create_user(**serializer.validated_data)
            return Response(status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST)


class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


class ResetPasswordView(APIView):

    def get_object(self, email):
        user = get_object_or_404(get_user_model(), email=email)
        return user

    def put(self, request):
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.data['email']
            user = self.get_object(email)
            password = serializer.data['password']
            if user.check_password(password):
                return Response({
                    'status': HTTP_400_BAD_REQUEST,
                    "message": "It should be different from your last password."
                })
            user.set_password(password)
            user.save()
            return Response({"status": HTTP_200_OK})
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class CrudeOilView(GenericAPIView):
    serializer_class = CrudeOilSerializer
    queryset = CrudeOil.objects.all()

    

    def get(self, request):
        data = CrudeOil.objects.all()
        print(request.query_params.get('start', None))
        if request.query_params.get('start', None) is not None and request.query_params.get('end', None) is not None:
            data = CrudeOil.objects.filter(date__range=(
                request.query_params.get("start"), request.query_params.get('end')))

        if request.query_params.get('start', None) is not None and request.query_params.get('end', None) is None:
            data = CrudeOil.objects.filter(
                date__gte=request.query_params.get('start'))

        if request.query_params.get('start', None) is None and request.query_params.get('end', None) is not None:
            data = CrudeOil.objects.filter(
                date__lte=request.query_params.get('end'))
        serializer = self.serializer_class(data, many=True)

        return Response({
            "status": "success",
            "data": serializer.data
        }, status=HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", 'data': serializer.data}, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class EIADataView(GenericAPIView):
    serializer_class = EIADataSerializer
    queryset = EIAData.objects.all()

    def get(self, request):
        data = EIAData.objects.all()

        print(request.query_params.get('start', None))
        if request.query_params.get('start', None) is not None and request.query_params.get('end', None) is not None:
            data = EIAData.objects.filter(date__range=(
                request.query_params.get("start"), request.query_params.get('end')))

        if request.query_params.get('start', None) is not None and request.query_params.get('end', None) is None:
            data = EIAData.objects.filter(
                date__gte=request.query_params.get('start'))

        if request.query_params.get('start', None) is None and request.query_params.get('end', None) is not None:
            data = EIAData.objects.filter(
                date__lte=request.query_params.get('end'))
        serializer = self.serializer_class(data, many=True)

        return Response({
            "status": "success",
            "data": serializer.data
        }, status=HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", 'data': serializer.data}, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)