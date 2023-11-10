from rest_framework import serializers
class BookSerializer(serializers.Serializer):
    id=serializers.IntegerField(label="enter book id")
    title=serializers.CharField(label="enter book title")
    author=serializers.CharField(label="enter Author names")