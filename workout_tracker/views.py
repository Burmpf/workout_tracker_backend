from rest_framework import generics
from rest_framework.decorators import authentication_classes, permission_classes
from .models import MuscleGroup, Exercise, DailyLog, ExerciseLog
from .serializers import MuscleGroupSerializer, ExerciseSerializer, DailyLogSerializer, ExerciseLogSerializer

# API view for listing and creating MuscleGroup instances
class MuscleGroupList(generics.ListCreateAPIView):
    queryset = MuscleGroup.objects.all()
    serializer_class = MuscleGroupSerializer

# API view for retrieving, updating, and deleting a MuscleGroup instance
class MuscleGroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MuscleGroup.objects.all()
    serializer_class = MuscleGroupSerializer

# API view for listing and creating Exercise instances
class ExerciseList(generics.ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

# API view for retrieving, updating, and deleting an Exercise instance
class ExerciseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

# API view for listing and creating DailyLog instances
class DailyLogList(generics.ListCreateAPIView):
    queryset = DailyLog.objects.all()
    serializer_class = DailyLogSerializer

# API view for retrieving, updating, and deleting a DailyLog instance
class DailyLogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DailyLog.objects.all()
    serializer_class = DailyLogSerializer

# API view for listing and creating ExerciseLog instances
class ExerciseLogList(generics.ListCreateAPIView):
    queryset = ExerciseLog.objects.all()
    serializer_class = ExerciseLogSerializer

# API view for retrieving, updating, and deleting an ExerciseLog instance
class ExerciseLogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExerciseLog.objects.all()
    serializer_class = ExerciseLogSerializer
