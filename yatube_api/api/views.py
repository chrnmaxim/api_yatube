from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from posts.models import Comment, Group, Post

from .permissions import AuthorPermission
from .serializers import CommentSerializer, GroupSerializer, PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """ViewSet for post's comments."""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (AuthorPermission, )

    def get_post(self):
        return get_object_or_404(Post, id=self.kwargs.get('post_id'))

    def perform_create(self, serializer):
        serializer.save(author=self.request.user,
                        post=CommentViewSet.get_post(self))

    def get_queryset(self):
        return CommentViewSet.get_post(self).comments.all()


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet for displaying groups."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    """ViewSet for posts."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorPermission, )

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
