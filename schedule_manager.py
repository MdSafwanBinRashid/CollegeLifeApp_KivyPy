import json
import os

class ScheduleManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        self.file_path = "schedule_data.json"
        self.default_data = {
            "Monday": [
                {"course": "CSC102", "time": "10:00 - 11:30 AM"},
                {"course": "MAT327", "time": "1:00 - 2:30 PM"}
            ],
            "Tuesday": [
                {"course": "PHY111", "time": "9:00 - 10:30 AM"},
                {"course": "CSC327", "time": "11:00 - 12:30 PM"},
                {"course": "ENG203", "time": "2:00 - 3:30 PM"}
            ],
            "Wednesday": [
                {"course": "CSC102", "time": "10:00 - 11:30 AM"},
                {"course": "MAT327", "time": "1:00 - 2:30 PM"},
            ],
            "Thursday": [
                {"course": "CSC411", "time": "9:00 - 10:30 AM"},
                {"course": "CHE340", "time": "11:00 - 12:30 PM"},
            ],
            "Friday": [
                {"course": "CSC327", "time": "9:00 - 10:30 AM"},
            ]
        }
        self.data = self.load_data()
    
    def load_data(self):
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r') as f:
                    return json.load(f)
            except:
                return self.default_data.copy()
        else:
            return self.default_data.copy()
    
    def save_data(self):
        try:
            with open(self.file_path, 'w') as f:
                json.dump(self.data, f, indent=2)
        except:
            print("Failed to save schedule data")
    
    def get_schedule(self):
        return self.data
    
    def add_class(self, day, course, time):
        day = day.capitalize()
        if day not in self.data:
            self.data[day] = []
        self.data[day].append({"course": course, "time": time})
        self.save_data()
    
    def delete_class(self, day, index):
        if day in self.data and 0 <= index < len(self.data[day]):
            del self.data[day][index]
            if len(self.data[day]) == 0:
                del self.data[day]
            self.save_data()
            return True
        return False