from rest_framework import serializers
from .models import Leadership


class LeadershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leadership
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        images = instance.leadership_img.all()

        if images:
            request = self.context.get('request')
            data['images'] = [{'image': request.build_absolute_uri(img.image.url)} for img in images]

        return data



