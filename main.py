from datetime import date, datetime, timedelta
from collections import deque


def get_birthdays_per_week(users):
    result = {}
    date_today = date.today()
    if len(users) < 1:
        print("Users list is empty")
        return result
    else:
        pass

    if date_today.weekday() == 0:
        start_day = -2
        end_day = 5
    else:
        start_day = 0
        end_day = 7
    
    # 2)creating 2 lists of workweek: full dtes and no-year-dates:
    list_of_dates_no_year = create_list_of_actual_dates(date_today, start_day, end_day)

    # 3)sorting_birhdys_per_day
    monday_preliminary, tuesday, wednesday, thursday, friday, saturday, sunday = sorting_birhdys_per_days(users, date_today, list_of_dates_no_year)

    # 4) finalization of Monday list
    monday_deque = deque()
    for each in monday_preliminary:
        monday_deque.append(each)
    for each in sunday:
        monday_deque.appendleft(each)
    for elem in saturday:
        monday_deque.appendleft(elem)
    monday = list(monday_deque)

    # 5) adding all days lists to final result
    lists = {"Monday" : monday, "Tuesday" : tuesday, "Wednesday" : wednesday, "Thursday" : thursday, "Friday" : friday}
    for key, value in lists.items():
        if len(value) >= 1:
            result[key] = value
    return result


def create_list_of_actual_dates(date_today, start_day, end_day):
    list_of_dates_in_week = []
    list_of_dates_no_year = []
    for days in range (start_day, end_day): #creating list of days to take into account
        day_interval = timedelta(days)
        today_plus_days = date_today + day_interval
        list_of_dates_in_week.append(today_plus_days)
    for each_date in list_of_dates_in_week: #transforming week dates to dates with no year
        day_strftime = datetime.strftime(each_date, "%m-%d")
        day_no_year = datetime.strptime(day_strftime, "%m-%d")
        list_of_dates_no_year.append(day_no_year)
    return list_of_dates_no_year


def sorting_birhdys_per_days(users, date_today, list_of_dates_no_year):
    monday_preliminary = []
    tuesday = []
    wednesday = []
    thursday = []
    friday = []
    saturday = []
    sunday = []
    for person in users:
        date_birthday = person["birthday"]
        date_birthday_strftime = datetime.strftime(date_birthday, "%m-%d")
        date_birthday_no_year = datetime.strptime(date_birthday_strftime, "%m-%d")
        for each_day in list_of_dates_no_year:
            delta = each_day - date_birthday_no_year
            delta_days = delta.days
            if delta_days == 0:
                bd_replaced_year = date_birthday.replace(year = date_today.year)
                if date_birthday_no_year < list_of_dates_no_year[0]:
                    bd_replaced_year = date_birthday.replace(year = date_today.year+1)
                bd_name = person["name"]
                weekday_this_day = bd_replaced_year.weekday()
                if weekday_this_day == 0:
                    monday_preliminary.append(bd_name)
                elif weekday_this_day == 1:
                    tuesday.append(bd_name)
                elif weekday_this_day == 2:
                    wednesday.append(bd_name)
                elif weekday_this_day == 3:
                    thursday.append(bd_name)
                elif weekday_this_day == 4:
                    friday.append(bd_name)
                elif weekday_this_day == 5:
                    saturday.append(bd_name)
                elif weekday_this_day == 6:
                    sunday.append(bd_name)
                else:
                    print("smth went wrong")
            else:
                continue
    return monday_preliminary, tuesday, wednesday, thursday, friday, saturday, sunday


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 18).date()}
    ]


    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
