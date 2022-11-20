from django.db import models

class Plan(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['complete']
