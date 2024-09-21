from django.contrib import admin
from .models import VehicleTrajectory, Vehicle, VehicleTrajectoryRoute
from .forms import VehicleTrajectoryForm, VehicleTrajectoryRouteForm


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    ...


@admin.register(VehicleTrajectoryRoute)
class VehicleTrajectoryRouteAdmin(admin.ModelAdmin):
    form = VehicleTrajectoryRouteForm


@admin.register(VehicleTrajectory)
class VehicleTrajectoryAdmin(admin.ModelAdmin):
    form = VehicleTrajectoryForm
