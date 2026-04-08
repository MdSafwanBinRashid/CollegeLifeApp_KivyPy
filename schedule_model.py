from schedule_manager import ScheduleManager

class ScheduleModel:
    def __init__(self):
        self.manager = ScheduleManager()
        self.days_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    def get_schedule_data(self):
        return self.manager.get_schedule()
    
    def get_days_order(self):
        return self.days_order
    
    def add_class(self, course, day, time):
        if course and day and time:
            self.manager.add_class(day, course, time)
            return True
        return False
    
    def delete_class(self, day, index):
        return self.manager.delete_class(day, index)