from django.contrib import admin

from users.models import User, Payouts, Position, Bonus, WorkingHours, Department

admin.site.register(User)
admin.site.register(Payouts)
admin.site.register(Position)
admin.site.register(Bonus)
admin.site.register(WorkingHours)
admin.site.register(Department)