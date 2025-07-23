from django.db import models

# Create your models here.
class Room(models.Model):
    hotel = models.CharField(max_length=100)
    room_number = models.IntegerField()
    description = models.TextField()
    capacity = models.IntegerField()
    cost_per_day = models.FloatField()
    all_inclusive = models.BooleanField()
    room_image = models.ImageField(upload_to="rooms/", blank=True, null=True)

    def __str__(self):
        return self.hotel + " " + str(self.room_number)

class People(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name + " " + self.last_name

class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.PROTECT)
    people = models.ForeignKey(People, on_delete=models.PROTECT)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def total_cost(self):
        days_in = self.end_time - self.start_time
        total_cost = days_in.days * self.room.cost_per_day
        return total_cost

    def __str__(self):
        return self.room.hotel + " " + str(self.room.room_number) + " by " + self.people.first_name + " " + self.people.last_name