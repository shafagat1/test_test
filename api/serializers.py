from rest_framework import serializers
from sith.models import Sith, Planet, Recruit, Questions, Answer


class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = ['name', 'id' ]

class SithSerializer(serializers.ModelSerializer):
    planet = PlanetSerializer(many=False)
    class Meta:
        model = Sith
        fields = ['planet', 'name', 'id']
class RecruiterSerializer(serializers.ModelSerializer):
    #planet = PlanetSerializer(many=False)
    class Meta:
        model = Recruit
        fields = ['name', 'planet', 'email', 'age']

    # def create(self, validated_data):
    #     recruiter = Recruit.objects.create(name=validated_data['name'], age=validated_data['age'], planet=validated_data['planet'], email=validated_data['email'])
    #     return recruiter

class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ['name', 'id']

class AnswerSerializer(serializers.ModelSerializer):
    questions = QuestionsSerializer(many=False)
    class Meta:
        model = Answer
        fields = ['result', 'questions' ]

        def create(self, validated_data):
            print(validated_data)
            return validated_data
class RecruiterAnswerSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(many=True)
    class Meta:
        model = Recruit
        fields = ['name', 'planet', 'email', 'age', 'answer', 'id']
