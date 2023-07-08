import requests
import os
from datetime import datetime
from workout_data import WorkoutData
from data_manager import DataManager

SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
NUTRITIONIX_APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
NUTRITIONIX_APP_KEY = os.environ.get("NUTRITIONIX_APP_KEY")

dm = DataManager(token=SHEETY_TOKEN)

nl_exercises = input("Tell me which exercises you did: ")


def get_workouts(nl_workout):
    headers = {
        "x-app-id": NUTRITIONIX_APP_ID,
        "x-app-key": NUTRITIONIX_APP_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "query": nl_workout,
        "gender": "male",
        "weight_kg": 80,
        "height_cm": 170,
        "age": 37
    }
    response = requests.post("https://trackapi.nutritionix.com/v2/natural/exercise", headers=headers, json=data)
    response.raise_for_status()
    exercises = response.json()["exercises"]
    now = datetime.now()
    return [
        WorkoutData(
            date=now.strftime("%d/%m/%Y"),
            time=now.strftime("%H:%M:%S"),
            exercise=ex["name"].capitalize(),
            duration=ex["duration_min"],
            calories=ex["nf_calories"]
        ) for ex in exercises]


workouts = get_workouts(nl_exercises)

for w in workouts:
    print(f"date: {w.date} time: {w.time} exercise: {w.exercise} duration: {w.duration} calories: {w.calories}")
    dm.post_workout(w)

