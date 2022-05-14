from rest_framework import serializers
from blog .models import Article

class BlogArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'pk',
            'user',
            'title',
            'content',
        ] 
        read_only_fields = ['user']
    
    # converts to JSON
    # validations for data passed

    def validate_title(self, value):
        qs = Article.objects.filter(title__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists() :
            raise serializers.ValidationError('This title has already been used')
        return value
