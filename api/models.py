from django.db import models


class Pgs(models.Model):
    id = models.AutoField(primary_key=True)
    pg_title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    address = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.pg_title  # More descriptive for admin view


class Users(models.Model):  
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=128)  
    email = models.EmailField(unique=True)
    pg = models.ForeignKey(Pgs, on_delete=models.CASCADE, related_name="users")  # ✅ better naming


    def __str__(self):
        return self.username
    
class Rooms(models.Model):
    id = models.AutoField(primary_key=True)
    room_number = models.CharField(max_length=10)
    pg = models.ForeignKey(Pgs, on_delete=models.CASCADE, related_name="rooms")
    is_occupied = models.BooleanField(default=False)

    def __str__(self):
        return f"Room {self.room_number} in {self.pg.pg_title}"
        
    # class Billing(models.Model):
    #     id = models.AutoField(primary_key=True)
    #     user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="billings")  # ✅ better naming
    #     amount = models.DecimalField(max_digits=10, decimal_places=2)
    #     due_date = models.DateField()
    #     is_paid = models.BooleanField(default=False)

    #     def __str__(self):
    #         return f"Billing for {self.user.username} - Amount: {self.amount}"
