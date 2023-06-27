from django.contrib.auth.models import User
from rest_framework import serializers

class RegestrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model = User        # here user model is default by django
        fields = ['username', 'email', 'password', 'password2']     # we are passing extra passwor2 field
        extra_kwargs = {
            'password' : {'write_only' : True}
        }

    # over-riding save method to add extra field "PASSWORD2".
    # we are over-rideing save method.
    def save(self):

        # cheaking if password1 is same as password2 or not
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({
                'error':'P1 and P2 should be same.'
            })
        
        # checking weatcer this user exists or not.
        email = self.validated_data['email']    # getting email from serializer
        user_queryset = User.objects.filter(email = email)      # getting email from User database 

        if user_queryset.exists():              # checking if email exists or not
            raise serializers.ValidationError({
                'error':'email already exists.'
            })
        
        # we are creating a New User manually.
        # creating this instance through email and username
        # we are creating inside "USER"
        account = User(email = self.validated_data['email'], username = self.validated_data['username'])
        account.set_password(password)          # setting password.
        account.save()

        return account
    
    