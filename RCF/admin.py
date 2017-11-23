from django.contrib import admin
from .models import Relay, CTVT, Frq, CurrentRating, Power, Outline, InOut_1,InOut_2, InOut_3, InOut_4, InOut_5, InOut_6, InOut_7, InOut_8, Com_Port, Function, Protocol, Language

admin.site.register(Relay)
admin.site.register(CTVT)
admin.site.register(Frq)
admin.site.register(CurrentRating)
admin.site.register(Power)
admin.site.register(Outline)
admin.site.register(InOut_1)
admin.site.register(InOut_2)
admin.site.register(InOut_3)
admin.site.register(InOut_4)
admin.site.register(InOut_8)
admin.site.register(InOut_5)
admin.site.register(InOut_6)
admin.site.register(InOut_7)
admin.site.register(Com_Port)
admin.site.register(Function)
admin.site.register(Protocol)
admin.site.register(Language)


# Register your models here.
