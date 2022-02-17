from django.contrib import admin

from chatbot.models import Flowchart, Method, SamplingFlowchart, SamplingMethod

admin.site.register(Flowchart)
admin.site.register(Method)
admin.site.register(SamplingFlowchart)
admin.site.register(SamplingMethod)
