from rest_framework import serializers
from .models import MuscleGroup, Exercise, DailyLog, ExerciseLog

# Serializer for MuscleGroup model
class MuscleGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MuscleGroup
        fields = '__all__'

# Serializer for Exercise model
class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

# Serializer for DailyLog model
class DailyLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyLog
        fields = '__all__'

# Serializer for ExerciseLog model
class ExerciseLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseLog
        fields = '__all__'
