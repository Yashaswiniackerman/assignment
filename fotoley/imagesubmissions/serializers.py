from rest_framework import serializers
from .models import Imagesubmissions

class ImagesubmissionSerializer(serializers.ModelSerializer):
    uploader = serializers.ReadOnlyField(source='User.username')
    uploader_id = serializers.ReadOnlyField(source='User.id')
    image_file = serializers.ImageField(required=True)
    
    
    class Meta:
        model = Imagesubmissions
        fields = ['id', 'uploader', 'uploader_id',  'description', 'image_file']
        
    def create(self, validated_data):
        context = self.context
        instance = Imagesubmissions.objects.create(
            uploader=context["user"],
            description=validated_data["description"],
            image_file=validated_data["image_file"]
        )
        
        instance.save()
        return instance
        
        
        