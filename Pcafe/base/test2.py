import serial
import time

import pandas as pd

from models import TranscationHistory

data = TranscationHistory.objects.all().first()
print(data)
    
