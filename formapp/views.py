from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import State, District, Post
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
import json


class StateListView(APIView):
    def get(self, request):
        states = State.objects.all().values('id', 'name')
        return Response({'states': list(states)})


class DistrictListView(APIView):
    def get(self, request, state_id):
        districts = District.objects.filter(state_id=state_id).values('id', 'name')
        return Response({'districts': list(districts)})


class PostView(APIView):
    def get(self, request, post_id=None):
        if post_id:
            post = get_object_or_404(Post, id=post_id)
            post_data = {
                'id': post.id,
                'name': post.name,
                'gender': post.gender,
                'language': post.language,
                'state_id': post.state.id,
                'state_name': post.state.name,
                'district_id': post.district.id,
                'district_name': post.district.name
            }
            return Response(post_data, status=status.HTTP_200_OK)
        else:
            posts = Post.objects.all()
            posts_data = [
                {
                    'id': post.id,
                    'name': post.name,
                    'gender': post.gender,
                    'language': post.language,
                    'state_id': post.state.id,
                    'state_name': post.state.name,
                    'district_id': post.district.id,
                    'district_name': post.district.name
                } for post in posts
            ]
            return Response({'posts': posts_data}, status=status.HTTP_200_OK)
    
    def post(self, request):
        try:
            data = json.loads(request.body)
            state = get_object_or_404(State, id=data['state'])
            district = get_object_or_404(District, id=data['district'])
            post = Post.objects.create(
                name=data['name'],
                gender=data['gender'],
                language=data['language'],
                state=state,
                district=district
            )
            post_data = {
                'id': post.id,
                'name': post.name,
                'gender': post.gender,
                'language': post.language,
                'state_id': post.state.id,
                'state_name': post.state.name,
                'district_id': post.district.id,
                'district_name': post.district.name
            }
            return Response({'message': 'Post created successfully', 'post': post_data}, status=status.HTTP_201_CREATED)
        except KeyError as e:
            return Response({'error': f"Missing field: {e}"}, status=status.HTTP_400_BAD_REQUEST)
        

    def put(self, request,post_id):
        try:
            data = json.loads(request.body)
            post = get_object_or_404(Post, id=post_id)
            state = get_object_or_404(State, id=data['state'])
            district = get_object_or_404(District, id=data['district'])
            post.name = data['name']
            post.gender = data['gender']
            post.language = data['language']
            post.state = state
            post.district = district
            post.save()

            post_data = {
                'id': post.id,
                'name': post.name,
                'gender': post.gender,
                'language': post.language,
                'state_id': post.state.id,
                'state_name': post.state.name,
                'district_id': post.district.id,
                'district_name': post.district.name
            }
            return Response({'message': 'Post updated successfully', 'post': post_data}, status=status.HTTP_200_OK)
        except KeyError as e:
            return Response({'error': f"Missing field: {e}"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        post.delete()
        return Response({'message': 'Post deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
