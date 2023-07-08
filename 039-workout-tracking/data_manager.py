import requests
from workout_data import WorkoutData


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self, token):
        self.token = token

    def post_workout(self, workout: WorkoutData):
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        body = {
            "workout": {
                "date": workout.date,
                "time": workout.time,
                "exercise": workout.exercise,
                "duration": workout.duration,
                "calories": workout.calories
            }
        }
        response = requests.post(
            "https://api.sheety.co/a3a7667cd4673d4ec7c8f671312c9eba/myWorkouts/workouts",
            headers=headers,
            json=body)
        print(response.text)
        response.raise_for_status()
