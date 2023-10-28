from rest_framework import serializers
from sinhalaNLP.models import  SinhalaAudio
from sinhalaNLP.models import  AudioBook

class SinhalaAudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = SinhalaAudio
        fields = ['studentId', 'studentName', 'words']

class AudioBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioBook
        fields = ['bookId', 'bookName', 'author']

