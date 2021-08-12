from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


""" 
# @api_view()
def hello_world(request):
    if request.method == 'GET':
        return Response({'msg': 'hello world'})
"""


@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'GET':
        return Response({'msg': 'hello world'})
    if request.method == 'POST':
        print(request.data)
        return Response({'msg': 'This is post request'})
