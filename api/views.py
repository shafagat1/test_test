from django.shortcuts import render
from rest_framework import permissions, generics
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .serializers import *
from sith.models import Sith, Planet, Questions, Answer
from django.http import JsonResponse
from rest_framework.response import Response
import json

class GetSithInfo(generics.GenericAPIView):
    serializer_class = SithSerializer
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        sith = Sith.objects.all()
        serializer = self.get_serializer(sith, many=True)
        data = { 'data': serializer.data}
        return JsonResponse(data, safe=False)

class GetPlanet(generics.GenericAPIView):
    serializer_class = PlanetSerializer
    permission_classes = [permissions.AllowAny, ]

    def get(self, request):
        planet = Planet.objects.all()
        serializer = self.get_serializer(planet, many=True)
        data = { 'data': serializer.data}
        return JsonResponse(data, safe=False)
class AddRecruiter(generics.GenericAPIView):
    serializer_class = RecruiterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Succes', status=HTTP_200_OK)
        else:
            return Response('Error', status=HTTP_400_BAD_REQUEST)
class GetQuestions(generics.GenericAPIView):
    serializer_class = QuestionsSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        questions = Questions.objects.all()
        serializer = self.get_serializer(questions, many=True)
        data = { 'data': serializer.data }
        return JsonResponse(data, safe=False)

class AddAnswer(generics.CreateAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        print(request.data)
        answer = request.POST.getlist("answer[]")
        email = request.data.get('email')
        recruit = Recruit.objects.get(email=email)
        questions = request.POST.getlist("questions[]")
        questions_obj = Questions.objects.filter(id__in=questions)
        for answer, question in zip(answer, questions_obj):
            if answer == 'true':
                ans = True
            else:
                ans = False
            answer_obj = Answer.objects.create(result=ans, questions=question)
            recruit.answer.add(answer_obj)
            recruit.save()
        return Response('sdsd')

class SingleSith(generics.GenericAPIView):
    serializer_class = SithSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        sith = request.GET.get('sith')
        questions = Sith.objects.get(id=sith)
        serializer = self.get_serializer(questions, many=False)
        recruit = Recruit.objects.filter(activate=False)
        serializer_recruit = RecruiterAnswerSerializer(recruit, many=True)
        data = { 'sith': serializer.data,
                 'recruit': serializer_recruit.data
                 }
        return JsonResponse(data, safe=False)

# Create your views here.

class EnrollRecruit(generics.CreateAPIView):
    serializer_class = RecruiterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        recruit_id = request.POST.get("recruit")
        sith_name = request.POST.get("sith")
        print(sith_name)
        sith = Sith.objects.get(id=sith_name)
        recruit = Recruit.objects.get(id=recruit_id)
        recruit.activate =True
        sith.recruits.add(recruit)
        recruit.save()
        return Response ('Save', status=HTTP_200_OK)