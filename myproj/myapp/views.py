from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import request_otp, verify_otp

@api_view(['POST'])
def request_otp_view(request):
    mobile_number = request.data.get('mobile_number')
    if not mobile_number:
        return Response({'error': 'Please provide a valid mobile number.'}, status=400)

    otp, message = request_otp(mobile_number)
    if not otp:
        return Response({'error': message}, status=429)

    return Response({'otp': otp, 'message': message}, status=200)

@api_view(['POST'])
def verify_otp_view(request):
    mobile_number = request.data.get('mobile_number')
    user_otp = request.data.get('otp')

    if not mobile_number or not user_otp:
        return Response({'error': 'Please provide both mobile number and OTP.'}, status=400)

    is_verified, message = verify_otp(mobile_number, user_otp)
    if is_verified:
        return Response({'message': message}, status=200)
    else:
        return Response({'error': message}, status=400)
