import random

def make_prediction(data):
    forecast = []
    for _ in range(3):
        forecast.append(round(random.uniform(1000, 2000), 2))
    
    return {'forecast': forecast}
