from rest_framework.serializers import ModelSerializer, CharField, ValidationError

from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()

class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
                'username',
                ]

class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField(required=True)
    class Meta:
        model = User
        fields = [
                'username',
                'password',
                'token',
                ]
        # This ensures the pw is not returned
        extra_kwargs = {'password':
                            {'write_only': True}
                            }
    
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        
        user = User.objects.filter(
                username=username
                )
        
        if user.exists():
            user_obj = user.first()
        else:
            raise ValidationError('Invalid username')
        
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError('Invalid password')
        
        data['token'] = 'adsf'
        return data