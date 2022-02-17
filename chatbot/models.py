from django.db import models

from common.models import BaseModel


class Method(BaseModel):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    video = models.URLField(blank=True)

    def __str__(self):
        return "{} - {}".format(self.pk, self.name)


class Flowchart(BaseModel):
    path = models.CharField(max_length=64, unique=True)
    method = models.ForeignKey("Method", related_name="flowcharts", on_delete=models.PROTECT)

    def __str__(self):
        return "{} - {}".format(self.path, self.method.name)


class SamplingMethod(BaseModel):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    video = models.URLField(blank=True)

    def __str__(self):
        return "{} - {}".format(self.pk, self.name)


class SamplingFlowchart(BaseModel):
    path = models.CharField(max_length=64, unique=True)
    method = models.ForeignKey("SamplingMethod", related_name="samplingflowcharts", on_delete=models.PROTECT)

    def __str__(self):
        return "{} - {}".format(self.path, self.method.name)
