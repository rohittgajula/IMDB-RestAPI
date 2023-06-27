from rest_framework import serializers
from .models import WatchList, StreamPlatform, Review

class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)       # | serailzer relations.

    class Meta:
        model = Review
        exclude = ('watchlist',)         # coma should be added because its not a tupple
        # fields = '__all__'

class WatchListSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many = True, read_only = True)

    platform = serializers.CharField(source = 'platform.name')     # over-writing platform field to show name instead of platform id.

    class Meta:
        model = WatchList
        fields = "__all__"

#  hyperlinkedmodelserializer shows url in place of id | ADD "context={'request': request}" to serializer in views
#  class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
class StreamPlatformSerializer(serializers.ModelSerializer):

  # Nested serializers. | serilalizer relation. ******
  # watchlist is related_name in models.
  # --------
    watchlist = WatchListSerializer(many=True, read_only = True)  # every field is available
  # watchlist = serializers.StringRelatedField(many=True)  # only when you want string field.

    class Meta:
        model = StreamPlatform
        fields = "__all__"

 