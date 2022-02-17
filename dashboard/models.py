from django.conf import settings
from django.db import models

from common.models import BaseModel


class Project(BaseModel):
    name = models.CharField(max_length=64)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    progress = models.IntegerField(default=0)
    path = models.CharField(max_length=64)
    flowchart = models.ForeignKey("chatbot.Flowchart", blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class SamplingProject(BaseModel):
    name = models.CharField(max_length=64)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    progress = models.IntegerField(default=0)
    path = models.CharField(max_length=64)
    flowchart = models.ForeignKey("chatbot.SamplingFlowchart", blank=True, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
