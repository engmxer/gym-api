from django.db import models

# Create your models here.
class Client(models.Model):
    GENDER_CHOICES = [
        ('M', 'Мужской'),
        ('F', 'Женский'),
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    membership_start = models.DateField(auto_now_add=True)
    membership_end = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Workout(models.Model):
    CATEGORY_CHOICES = [
        ('cardio', 'Кардио'),
        ('strength', 'Силовая'),
        ('yoga', 'Йога'),
        ('pilates', 'Пилатес'),
    ]
    
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    duration_minutes = models.PositiveIntegerField()
    max_participants = models.PositiveIntegerField(default=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидание'),
        ('confirmed', 'Подтверждена'),
        ('cancelled', 'Отменена'),
        ('completed', 'Проведена'),
    ]
    
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='bookings')
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='bookings')
    booking_date = models.DateTimeField(auto_now_add=True)
    workout_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='confirmed')
    notes = models.TextField(blank=True)

    class Meta:
        unique_together = ['client', 'workout', 'workout_date']

    def __str__(self):
        return f"{self.client} - {self.workout}"
