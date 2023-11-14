from __future__ import print_function
from six.moves import urllib
from io import BytesIO
from google.oauth2 import service_account
from google.cloud import speech
from pydub import AudioSegment
audio_file_name = "D/sldpaldpladp.wav"
credentials = service_account.Credentials.from_service_account_file
client = speech.SpeechClient(credentials=credentials)
with open(audio_file_name, 'rb') as audio_file:
  content = audio_file.read()
  audio = AudioSegment.from_wav(BytesIO(content))
  uri = urllib.parse.urlparse(audio.get_backend_configuration_uri())