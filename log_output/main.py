import time
from datetime import datetime
from uuid import uuid4

base = str(uuid4())

while True:
    print(f"{datetime.now()}: {base}")
    time.sleep(5)
