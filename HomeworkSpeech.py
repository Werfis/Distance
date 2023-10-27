import requests
import json
from io import BytesIO
from os import path
from requests.exceptions import ConnectionError
API_KEY
AUDIO_FILE_PATH
MODEL_ID = "ru-model"
SAMPLE_RATE = 16000
MAX_RETRY = 3
class SpeechKit:
    def __init__(self, api_key: str, model_id: str, sample_rate: int):
        self.api_key = api_key
        self.model_id = model_id
        self.sample_rate = sample_rate