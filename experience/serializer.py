from rest_framework import serializers

from experience.models import Experience


class ExperienceSerializer(serializers.HyperlinkedModelSerializer):
    # rank = serializers.CharField()


    class Meta:
        model = Experience
        fields = '__all__'

