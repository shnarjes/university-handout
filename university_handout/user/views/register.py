from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from django.utils import timezone

from user.models.user import User
from user.models.otp import OTP
from user.serializers import UserSerializer
from user.utils.utils import create_end_time, randN, end_time, send_sms_otp


class RegisterAPIView(generics.GenericAPIView):
    permission_classes = (AllowAny, )
    serializer_class = UserSerializer

    def post(self, request):
        user = User.objects.filter(phone=request.data['phone'])
        if user.exists():
            user = User.objects.get(phone=request.data['phone'])
            if user.is_active is False:
                obj = OTP.objects.filter(user=user, type=1)
                if obj.exists():
                    obj = OTP.objects.get(user=user, type=1)
                    count_otp = obj.number_error_5time
                    if count_otp < 5:
                        obj.code = randN(6)
                        obj.exp_time = create_end_time()
                        obj.exp_time_error_send = end_time()
                        obj.number_error_5time = count_otp + 1
                        obj.save()
                        send_sms_otp(mobile=user.phone, token=obj.code)
                        return (Response(obj.code, status=status.HTTP_200_OK))
                    else:
                        if obj.exp_time_error_send < timezone.now():
                            obj.code = randN(6)
                            obj.exp_time = create_end_time()
                            obj.exp_time_error_send = end_time()
                            obj.number_error_5time = 0
                            obj.save()
                            send_sms_otp(mobile=user.phone, token=obj.code)
                            return (Response(obj.code, status=status.HTTP_200_OK))
                        else:
                            return(Response('Try again an hour', status=status.HTTP_429_TOO_MANY_REQUESTS))
                else:
                    obj = OTP.objects.create(
                        code=randN(6),
                        exp_time=create_end_time(),
                        exp_time_error_send=end_time(),
                        user=user,
                        type=1,
                        number_error_3time=0,
                        number_error_5time=1
                    )
                    send_sms_otp(mobile=user.phone, token=obj.code)
                    return (Response(obj.code, status=status.HTTP_200_OK))
            else:
                return (Response("user with this Phone already exists.", status=status.HTTP_400_BAD_REQUEST))
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()
            user.is_active = False
            user.save()
            obj = OTP.objects.filter(user=user, type=1)
            if obj.exists():
                obj = OTP.objects.get(user=user, type=1)
                count_otp = obj.number_error_5time
                if count_otp <= 5:
                    obj.code = randN(6)
                    obj.exp_time = create_end_time()
                    obj.exp_time_error_send = end_time()
                    obj.number_error_5time = count_otp + 1
                    obj.save()
                    send_sms_otp(mobile=user.phone, token=obj.code)
                    return (Response(obj.code, status=status.HTTP_200_OK))
                else:
                    if obj.exp_time_error_send < timezone.now():
                        obj.code = randN(6)
                        obj.exp_time = create_end_time()
                        obj.exp_time_error_send = end_time()
                        obj.number_error_5time = 0
                        obj.save()
                        send_sms_otp(mobile=user.phone, token=obj.code)
                        return (Response(obj.code, status=status.HTTP_200_OK))
                    else:
                        return(Response('Try again an hour', status=status.HTTP_429_TOO_MANY_REQUESTS))
            else:
                obj = OTP.objects.create(
                    code=randN(6),
                    exp_time=create_end_time(),
                    exp_time_error_send=end_time(),
                    user=user,
                    type=1,
                    number_error_3time=0,
                    number_error_5time=1
                )
                send_sms_otp(mobile=user.phone, token=obj.code)
                return (Response(obj.code, status=status.HTTP_200_OK))
