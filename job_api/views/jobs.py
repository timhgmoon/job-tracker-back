from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import PermissionDenied

from ..serializers.job import JobSerializer
from ..models.job import Job

class JobsView(APIView):
  def post(self, request):
    request.data['owner'] = request.user.id
    job = JobSerializer(data=request.data)
    if job.is_valid():
      job.save()
      return Response(job.data, status=status.HTTP_201_CREATED)
    return Response(job.errors, status=status.HTTP_400_BAD_REQUEST)

  def get(self, request):
    jobs = Job.objects.filter(owner=request.user.id)
    data = JobSerializer(jobs, many=True).data
    return Response(data)

class JobView(APIView):
  def get(self, request, pk):
    job = get_object_or_404(Job, pk=pk)
    if request.user != job.owner:
      raise PermissionDenied('Unauthorized, you do not own this job')
    data = JobSerializer(job).data
    return Response(data)
  
  def patch(self, request, pk):
    job = get_object_or_404(Job, pk=pk)
    if request.user != job.owner:
      raise PermissionDenied('Unauthorized, you do not own this job')
    request.data['owner'] = request.user.id
    updated_job = JobSerializer(job, data=request.data)
    if updated_job.is_valid():
      updated_job.save()
      return Response(updated_job.data)
    return Response(updated_job.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):
    job = get_object_or_404(Job, pk=pk)
    if request.user != job.owner:
      raise PermissionDenied('Unauthorized, you do not own this job')
    job.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)