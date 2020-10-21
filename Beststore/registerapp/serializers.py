from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.HyperlinkedModelSerializer):

	password = serializers.CharField(
		write_only=True,
		required=True,
		help_text='Leave empty if no change needed',
		style={'input_type': 'password', 'placeholder': 'Password'}
	)

	class Meta:
		model = User
		fields = ('username', 'password','first_name','last_name','address')

	def create(self, validated_data):
		validated_data['password'] = make_password(validated_data.get('password'))
		return super(UserSerializer, self).create(validated_data)

	def update(self, instance, validated_data):
		instance.username = validated_data.get('username', instance.username)
		 # = validated_data.get('password', instance.password)
		instance.password = make_password(validated_data.get('password',instance.password))
		instance.first_name = validated_data.get('first_name', instance.first_name)
		instance.last_name =  validated_data.get('last_name', instance.last_name)
		instance.address =  validated_data.get('address', instance.address)
		instance.save()
		return instance
