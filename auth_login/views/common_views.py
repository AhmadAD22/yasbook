from utils.sms import SmsSender
from ..models import *
from ..serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class ForgetPasswordAPIView(APIView):
    permission_classes=[]
    authentication_classes=[]
    def post(self,request,*args, **kwargs):
        
        phone=request.data['phone']
        try:
            user=MyUser.objects.get(phone=phone)
        except MyUser.DoesNotExist:
            return Response({"error":"the account not found"},status=status.HTTP_404_NOT_FOUND)
        if OTPRequest.checkRateLimitReached(phone=phone):
            return Response({'error': 'MANY_OTP_REQUESTS'}, status=status.HTTP_409_CONFLICT)
        otp=OTPRequest.objects.create(phone=phone,type=OTPRequest.Types.FORGET_PASSWORD)
        
            
        sms = SmsSender()
        if sms.send_otp(phone.replace('0', '966', 1), f"Your OTP for Update Your Password is: {otp}"):
                return Response("created", status=status.HTTP_201_CREATED)
        else:
                return Response({'error': 'Failed to send OTP", "SMS_SEND_FAILED'}, status=status.HTTP_502_BAD_GATEWAY)
        
class VerifyPhoneAPIView(APIView):
    permission_classes=[]
    authentication_classes=[]
    def post(self,request,*args, **kwargs):
        otp=OTPRequest.objects.filter(phone=request.data['phone'],
                                        code=request.data['code'],
                                        isUsed=False,
                                        type=OTPRequest.Types.FORGET_PASSWORD).first()
        if otp:
            # deactivate otp code
            otp.isUsed=True
            otp.save()
            return Response({"result":"OTP is correct"},status.HTTP_200_OK)
        else:
            return Response({"error":"OTP is not correct!"},status.HTTP_404_NOT_FOUND)



class UpdateForgottenPasswordAPIView(APIView):
    permission_classes=[]
    authentication_classes=[]
    def post(self,request,*args, **kwargs):
        try:
            phone=request.data['phone']
            new_password=request.data['password']
            user=MyUser.objects.get(phone=phone)
            # Update the password
            user.set_password(new_password)
            user.save()
            return Response({"result":"Password updated"},status.HTTP_200_OK)
        except MyUser.DoesNotExist:
            return Response({"erorr":"user does not found"},status.HTTP_404_NOT_FOUND)
            

        
        
    
    