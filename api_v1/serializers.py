from rest_framework import serializers
from .models import Client, Workout, Booking


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    client_info = ClientSerializer(source='client', read_only=True)
    workout_info = WorkoutSerializer(source='workout', read_only=True)
    client_id = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(), source='client', write_only=True
    )
    workout_id = serializers.PrimaryKeyRelatedField(
        queryset=Workout.objects.all(), source='workout', write_only=True
    )

    class Meta:
        model = Booking
        fields = ['id', 'client_id', 'workout_id', 'client_info', 'workout_info',
                  'booking_date', 'workout_date', 'status', 'notes']