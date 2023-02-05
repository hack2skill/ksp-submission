from rest_framework import serializers
from .models import Person
import face_recognition
import numpy as np
from PIL import  Image

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
        # exclude=('encodings',)


    def create(self, validated_data):
        # Add the prefix to the name
        # validated_data['name'] = "Mr. " + validated_data['name']

        # Perform face recognition
        # image = self.context['request'].FILES.get('image')
        image = validated_data.pop('image')
        np_image = np.array(Image.open(image))
        face_encodings = face_recognition.face_encodings(np_image)

        if len(face_encodings) > 0:
            validated_data['encodings'] = face_encodings[0].tolist()
        person = Person.objects.create(**validated_data)
        person.image = image
        person.save()

        return person



    # def create(self, serializer):
    #     person = serializer.save()
    #     image = face_recognition.load_image_file(person.image.path)
    #     encodings = face_recognition.face_encodings(image)[0]
    #     print(encodings)
    #     person.save_encodings(encodings)
    #
    #     person.save()
    #     print("saved")



