from rest_framework import serializers
from ..models.job import Job

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('id', 'company', 'location', 'job_title', 'salary', 'app_process', 'owner')