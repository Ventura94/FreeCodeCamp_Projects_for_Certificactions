def add_time(start, duration, day=None):
    days = ["Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"]
    days_later = 0
    split_start = start.split(':')
    split_start = split_start[0] + " " + split_start[1]
    split_start = split_start.split(" ")
    start_hours = int(split_start[0])
    start_minutes = int(split_start[1])
    am_or_pm = split_start[2]
    is_am = False
    is_pm = False
    if am_or_pm == "AM":
        is_am = True
    elif am_or_pm == "PM":
        is_pm = True
    split_duration = duration.split(":")
    duration_hours = int(split_duration[0])
    duration_minutes = int(split_duration[1])
    total_minutes = start_minutes + duration_minutes
    total_hours = start_hours + duration_hours
    while total_minutes > 60:
        total_minutes = total_minutes - 60
        total_hours = total_hours + 1
    if day is not None:
        index_day = days.index(day.capitalize())
        while total_hours > 12:
            total_hours = total_hours - 12
            if is_am:
                is_am = False
                is_pm = True
                am_or_pm = "PM"
                index_day = index_day + 1
                days_later = days_later + 1
            elif is_pm:
                is_pm = False
                is_am = True
                am_or_pm = "AM"
        if total_hours == 12:
            if is_am:
                am_or_pm = "PM"
                index_day = index_day + 1
                days_later = days_later + 1
            elif is_pm:
                am_or_pm = "AM"

        while (index_day + 1) > len(days):
            index_day = index_day - len(days)
        if len(str(total_minutes)) == 1:
            total_minutes = "0" + str(total_minutes)
            new_time = str(total_hours) + ":" + total_minutes + " " + am_or_pm + ", " + str(days[index_day])
        else:
            new_time = str(total_hours) + ":" + str(total_minutes) + " " + am_or_pm + ", " + str(days[index_day])
        if days_later == 1:
            new_time = new_time + " (next day)"
        elif days_later > 1:
            new_time = new_time + " (" + str(days_later) + " days later)"
        return new_time

    else:
        while total_hours > 12:
            total_hours = total_hours - 12

            if is_am:
                is_am = False
                is_pm = True
                am_or_pm = "PM"

            elif is_pm:
                is_pm = False
                is_am = True
                am_or_pm = "AM"
                days_later = days_later + 1

        if total_hours == 12:
            if is_am:
                am_or_pm = "PM"

            elif is_pm:
                am_or_pm = "AM"
                days_later = days_later + 1

        if len(str(total_minutes)) == 1:
            total_minutes = "0" + str(total_minutes)
            new_time = str(total_hours) + ":" + total_minutes + " " + am_or_pm

        else:
            new_time = str(total_hours) + ":" + str(total_minutes) + " " + am_or_pm

        if days_later == 1:
            new_time = new_time + " (next day)"
        elif days_later > 1:
            new_time = new_time + " (" + str(days_later) + " days later)"

        return new_time
