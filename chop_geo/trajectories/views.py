from rest_framework import viewsets, generics, permissions
from .models import VehicleTrajectoryRoute, VehicleTrajectory, Vehicle
from .serializers import VehicleTrajectoryRouteSerializer, VehicleTrajectorySerializer, \
    BulkVehicleTrajectorySerializer, VehicleTrajectoryCreateSerializer


class VehicleTrajectoryRouteViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = VehicleTrajectoryRoute.objects.all()
    serializer_class = VehicleTrajectoryRouteSerializer


class VehicleTrajectoryCreateAPIView(generics.CreateAPIView):
    queryset = VehicleTrajectory.objects.all()
    serializer_class = VehicleTrajectorySerializer
    permission_classes = [permissions.IsAuthenticated]  # Ensure only authenticated users can create trajectories

    def perform_create(self, serializer):
        # Automatically associate the VehicleTrajectory with the Vehicle of the current user
        try:
            vehicle = self.request.user.vehicle
        except Vehicle.DoesNotExist:
            vehicle = Vehicle.objects.create(user=self.request.user)
        serializer.save(vehicle=vehicle)


class BulkVehicleTrajectoryCreateAPIView(generics.CreateAPIView):
    queryset = VehicleTrajectory.objects.all()
    serializer_class = VehicleTrajectoryCreateSerializer

    def perform_create(self, serializer):
        try:
            vehicle = self.request.user.vehicle
        except Vehicle.DoesNotExist:
            vehicle = Vehicle.objects.create(user=self.request.user)
        # Additional logic to prevent multiple objects creation
        serializer.save(vehicle=vehicle)
