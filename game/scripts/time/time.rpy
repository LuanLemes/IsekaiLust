label start_time_variables:
    $ week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    $ day_time = ["Morning", "Afternoon", "Evening", "Dawn", "Late Down"]
    $ current_week_day = 0
    $ current_day_time = 0
    $ current_day = 1
    $ calendar = Calendar(0, week_days, day_time, 1, 0)
    $ event_one = Event(-1, -1, 10, "event_one", True)
    $ Events[0] = event_one
    $ c = 0
    $ show_calendar = True
    return

label time_next():
    if calendar.current_day_time > 3:
        return
    $ calendar.add_current_day_time(1)
    window hide
    return

label day_next():
    $ calendar.add_current_day(1)
    window hide
    return
