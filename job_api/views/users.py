from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from ..serializers.user import UserSerializer
from django.contrib.auth import authenticate, login, logout

class SignUp(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    
    def post(self, request):
        created_user = UserSerializer(data=request.data['user'])
        if created_user.is_valid():
            created_user.save()
            return Response({ 'user': created_user.data }, status=status.HTTP_201_CREATED)
        else:
            return Response(created_user.errors, status=status.HTTP_400_BAD_REQUEST)

class SignIn(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        data = request.data['user']
        user = authenticate(request, email=data['email'], password=data['password'])
        if user is not None:  
            login(request, user)
            Token.objects.filter(user=user).delete()
            token = Token.objects.create(user=user)
            user.token = token.key
            user.save()
            return Response({
                'user': {
                    'id': user.id,
                    'email': user.email,
                    'token': token.key
                }
            })
        else:
            return Response({ 'msg': 'The username and/or password is incorrect.' }, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class SignOut(generics.DestroyAPIView):
  def delete(self, request):
    user = request.user

    Token.objects.filter(user=user).delete()
    user.token = None
    user.save()
    logout(request)
    return Response(status=status.HTTP_204_NO_CONTENT)

class ChangePassword(generics.UpdateAPIView):
  def patch(self, request):
    user = request.user
    old_pw = request.data['passwords']['old']
    new_pw = request.data['passwords']['new']
   
    if not user.check_password(old_pw):
      return Response({'msg':'Wrong Password'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    user.set_password(new_pw)
    user.save()
    return Response(status=status.HTTP_204_NO_CONTENT)