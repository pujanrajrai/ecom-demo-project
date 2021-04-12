from django.db import models
from accounts.models import MyUser


# Create your models here.

class Chat(models.Model):
    send_from = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='send_from')
    send_to = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='send_to')
    message = models.CharField(max_length=500, blank=True)
    image = models.ImageField(blank=True)
    seen = models.BooleanField(default=False)
    send_date = models.DateTimeField(auto_now_add=True)
    seen_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.send_from}_to_{self.send_to}'
