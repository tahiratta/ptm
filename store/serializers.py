
from .models import User
from .models import Post
from .models import Group
from .models import Acadamic_Record
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:

        image = serializers.ImageField(max_length=None, use_url=True)

        model = User
        fields = ('email', 'password')
        #fields =('profile_photo', 'name', 'password', 'cell_number', 'email', 'gender', 'date_of_birth', 'type')
        #fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:

        file = serializers.FileField(max_length=None, use_url=True)

        model = Post
        fields = ('add_photo', 'status', 'files', 'comments')
        #fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('cover_photo', 'add_photo', 'g_name', 'status', 'files', 'comments')
        # fields = '__all__'

class Acadamic_RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acadamic_Record
        fields = ('attendance','quiz_number','quiz_marks')
        # fields = '__all__'