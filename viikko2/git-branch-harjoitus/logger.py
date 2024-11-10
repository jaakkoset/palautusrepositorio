from datetime import datetime

def logger(viesti):
    """Tulostaa asioita"""
    print(f"{datetime.now()}: {viesti}")
