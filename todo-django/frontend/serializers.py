from rest_framework import serializers

class TaskSerializer(serializers.Serializer):
	title = serializers.CharField()
	text = serializers.CharField()
