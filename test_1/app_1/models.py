from django.db import models

# Create your models here.


class State(models.Model):
    s_name = models.CharField(max_length=100)

    def __str__(self):
        return self.s_name

class District(models.Model):
    state_name =models.ForeignKey(State,on_delete=models.CASCADE)
    d_name = models.CharField(max_length=100)


    def __str__(self):
        return self.d_name

class Village(models.Model):
    dis_name =models.ForeignKey(District,on_delete=models.CASCADE)
    v_name = models.CharField(max_length=100)


    def __str__(self):
        return self.v_name

class User(models.Model):
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    district = models.ForeignKey(District,on_delete=models.CASCADE)
    Village = models.ForeignKey(Village,on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    roll = models.IntegerField()
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name
