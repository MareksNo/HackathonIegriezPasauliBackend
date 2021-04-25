from rest_framework import serializers
from rest_framework.authtoken.models import Token
from core.models import Question, Option, Member

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['question', 'correct', 'choice_text']

    

class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=False)

    class Meta:
        model = Question
        fields = ['q', 'xtraInfo', 'image', 'options']

    def create(self, validated_data):
        
        options_data = validated_data.pop('options')

        question_data = validated_data
        
        question = Question.objects.create(**validated_data)
        
        for option_data in options_data:
           
            Option.objects.create(question=question, correct=option_data['correct'], choice_text=option_data['choice_text'])
        return question

    def update(self, instance, validated_data):
        options_data = validated_data.pop('options')
        options = (instance.options).all()
        options = list(options)
        instance.q = validated_data.get('q', instance.q)
        instance.xtraInfo = validated_data.get('xtraInfo', instance.xtraInfo)
        instance.image = validated_data.get('image', instance.image)
        instance.save()

        for option_data in options_data:
            option = options.pop(0)
            option.choice_text = option_data.get('choice_text', option.choice_text)
            option.correct = option_data.get('correct', option.correct)
            option.save()
        return instance


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['username', 'score']
