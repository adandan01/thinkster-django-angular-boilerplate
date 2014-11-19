import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "thinkster_django_angular_boilerplate.settings")
import django
django.setup()
from django.contrib.auth.models import User
from authentication.models import UserProfile
from authentication.serializers import UserSerializer, UserProfileSerializer

if __name__ == "__main__":


    user = User.objects.get(pk=1)
    serialized_profile = UserProfileSerializer(user.profile)
    print serialized_profile.data
    d = serialized_profile.data
    d['first_name'] = 'daniel'
    d['username'] = 'daniel'
    d['user_id'] = 1
    print 'data', d
    s = UserProfileSerializer(data=d, partial=True)
    print s.errors
    #print s.is_valid()
