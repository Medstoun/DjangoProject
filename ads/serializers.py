from rest_framework import serializers

from ads.models import Location, User, Ad, Category


class UserCreateSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(
        required=False,
        queryset=Location.objects.all(),
        many=True,
        slug_field='name'
    )

    def is_valid(self, raise_exception=False):
        self._locations = self.initial_data.pop('locations')
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        user = User.objects.create(**validated_data)

        for locations in self._locations:
            obj, _ = Location.objects.get_or_create(name=locations)
            user.locations.add(obj)
        return user

    class Meta:
        model = User
        fields = "__all__"


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'role']


class UserDetailSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(
        read_only=True,
        many=True,
        slug_field='name'
    )

    class Meta:
        model = User
        exclude = ['password']


class UserUpdateSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(
        queryset=Location.objects.all(),
        many=True,
        slug_field='name',
        required=False
    )

    def is_valid(self, raise_exception=False):
        if "locations" in self.initial_data:
            self._locations = self.initial_data.pop('locations')
        else:
            self._locations = []
        return super().is_valid(raise_exception=raise_exception)

    def save(self, **kwargs):
        user = super().save(**kwargs)
        for locations in self._locations:
            obj, _ = Location.objects.get_or_create(name=locations)
            user.locations.add(obj)
        return user

    class Meta:
        model = User
        fields = "__all__"


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"


class AdSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        required=False,
        queryset=User.objects.all(),
        slug_field='username'
    )

    category = serializers.SlugRelatedField(
        required=False,
        queryset=Category.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Ad
        fields = "__all__"
