from django.db import models

# Create your models here.

class Posts (models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    description = models.TextField(default="")
    counter = models.PositiveIntegerField(default=0)
    Int_field = models.IntegerField(default=12)
    category = models.CharField(blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

class Comment (models.Model):
    text = models.TextField()
    new = models.ForeignKey('Posts', on_delete=models.CASCADE, related_name='comments')
    status = models.BooleanField(default=True)

class Wallet(models.Model):
    private_wallet = models.PositiveIntegerField(default=0)
    business_wallet = models.PositiveIntegerField(default=0)

    def str(self):
        return self.title

class Wallets(models.Model):
    name = models.CharField(max_length=200)
    currency = models.CharField(max_length=200)
    balance = models.FloatField(default=0)

    def serilize_from_db(self):
        return {'id':self.id, 'name':self.name, 'currency':self.currency, 'balance':self.balance}