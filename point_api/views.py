from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Point

@api_view(['POST'])
def find_closest_points(request):
    points = request.data.get('points')
    points_list = points.split(';')

    # Perform logic to find closest points
    closest_points = "2,2;4,5"  
    # Replace this with your logic to find the closest points

    # Save the received set of points and the closest points in the database
    point = Point(coordinates=points, closest_points=closest_points)
    point.save()

    return Response({'closest_points': closest_points})
