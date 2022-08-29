from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token

from django.utils import timezone

from user.models.user import User
from user.models.otp import OTP
from user.serializers import UserSerializer
from user.utils.utils import end_time


class VerifiedAPI(generics.GenericAPIView):
    permission_classes = (AllowAny, )
    serializer_class = UserSerializer

    def post(self, request):
        user = User.objects.filter(phone=request.data['phone'])
        if user.exists():
            user = User.objects.get(phone=request.data['phone'])
            serializer = self.get_serializer(user)
            otp = OTP.objects.filter(user=user).last()
            if otp.number_error_3time >= 3:
                if otp.exp_time_error_verified > timezone.now():
                    return(Response('Try again an hour', status=status.HTTP_429_TOO_MANY_REQUESTS))
                else:
                    otp.number_error_3time = 0
                    otp.save()
                return(Response('use the new code', status=status.HTTP_401_UNAUTHORIZED))
            else:
                if timezone.now() < otp.exp_time:
                    if otp.code == request.data['code']:
                        user.is_active = True
                        user.save()
                        context = (serializer.data)
                        return(Response(context, status=status.HTTP_200_OK))
                    else:
                        otp.number_error_3time = otp.number_error_3time + 1
                        otp.exp_time_error_verified = end_time()
                        otp.save()
                        return(Response('incorrect code', status=status.HTTP_401_UNAUTHORIZED))
                else:
                    otp.number_error_3time = 0
                    otp.save()
                    return(Response('use the new code', status=status.HTTP_401_UNAUTHORIZED))
        else:
            return (Response("user with this Phone not exists.", status=status.HTTP_400_BAD_REQUEST))
