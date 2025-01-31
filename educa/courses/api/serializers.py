from rest_framework import serializers

from ..models import Subject, Course, Module, Content

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'title', 'slug']

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = [
            'order', 'title', 'description'
        ]
    
class CourseSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = [
            'id', 'subject', 'title', 'slug',
            'overview', 'created', 'owner',
            'modules'
        ]

class ItemRealatedField(serializers.RelatedField):
    def to_representation(self, value):
        return value.render()

class ContentSerializer(serializers.ModelSerializer):
    item = ItemRealatedField(read_only=True)

    class Meta:
        model = Content
        fields = ['order', 'item']

class ModuleWithContentSetializer(serializers.ModelSerializer):
    contents = ContentSerializer(many=True)

    class Meta:
        model = Module
        fields = [
            'order', 'title', 
            'description', 'contents'
        ]

class CourseWithContentSerializer(serializers.ModelSerializer):
    modules = ModuleWithContentSetializer(many=True)

    class Meta:
        model = Course
        fields = [
            'id', 'subject', 'title', 'slug',
            'overview', 'created', 'owner',
            'modules'
        ]