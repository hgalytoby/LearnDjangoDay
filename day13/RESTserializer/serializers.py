from rest_framework import serializers

from RESTserializer.models import Person, Student, Book


class PersonSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    p_name = serializers.CharField(max_length=32)
    p_age = serializers.IntegerField(default=1)
    p_sex = serializers.BooleanField(default=False)



    def create(self, validated_data):
        # 不知道這用處是什麼。
        print('create')
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # 不知道這用處是什麼。
        print('update')
        instance.p_name = validated_data.get('p_name', instance.p_name)
        instance.p_age = validated_data.get('p_age', instance.p_age)
        instance.p_sex = validated_data.get('p_sex', instance.p_sex)
        instance.save()
        return instance

    class Meta:
        model = Person
        fields = ('id', 'p_name', 'p_age', 'p_sex')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('s_name', 's_age')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('b_name', 'b_price')
