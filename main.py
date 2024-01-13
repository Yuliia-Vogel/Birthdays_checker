from datetime import date, datetime, timedelta
from collections import deque

 
def get_birthdays_per_week(users):
    list_of_dates_in_week = []
    Monday_preliminary = []
    Tuesday = []
    Wednesday = []
    Thursday = []
    Friday = []
    Saturday = []
    Sunday = []
    result = {}
    date_today = date.today()
    # date_today = datetime(2024, 1, 1).date()
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
    
    for days in range (start_day, end_day): 
        day_interval = timedelta(days)
        today_plus_days = date_today + day_interval
        list_of_dates_in_week.append(today_plus_days)
    
    start_day_date = date_today + timedelta(start_day)
    end_day_date = start_day_date + timedelta(days=7)
         
    for person in users:
        date_birthday = person["birthday"]
        BD_replaced_year = date_birthday.replace(year=date_today.year)
        if BD_replaced_year == datetime(year=date_today.year, month = 12, day = 30).date() or BD_replaced_year == datetime(year=date_today.year, month = 12, day = 31).date():
            print("try this")
            BD_replaced_year = date_birthday.replace(year=date_today.year - 1)
        else:
            pass
        if start_day_date <= BD_replaced_year <= end_day_date:
            print(f"{date_birthday} - a birthday comes this week")
            bd_name = person["name"]
            for i in list_of_dates_in_week:
                if BD_replaced_year == i:
                    weekday_this_day = BD_replaced_year.weekday()
                    if weekday_this_day == 0:
                        Monday_preliminary.append(bd_name)
                    elif weekday_this_day == 1:
                        Tuesday.append(bd_name)
                    elif weekday_this_day == 2:
                        Wednesday.append(bd_name)
                    elif weekday_this_day == 3:
                        Thursday.append(bd_name)
                    elif weekday_this_day == 4:
                        Friday.append(bd_name)
                    elif weekday_this_day == 5:
                        Saturday.append(bd_name)
                    elif weekday_this_day == 6:
                        Sunday.append(bd_name)
                    else:
                        print("smth went wrong")
                else:
                    continue
        else:
            print(f"{date_birthday} not now")
    print(f"{Monday_preliminary} is Mon-pre")
    print(f"{Saturday} is Sat")
    print(f"{Sunday} is Sun")
    Monday_deque = deque()
    for each in Monday_preliminary:
        Monday_deque.append(each)
    for each in Sunday:
        Monday_deque.appendleft(each)
    for elem in Saturday:
        Monday_deque.appendleft(elem)
    Monday = list(Monday_deque)
    lists = {"Monday" : Monday, "Tuesday" : Tuesday, "Wednesday" : Wednesday, "Thursday" : Thursday, "Friday" : Friday}
    for key, value in lists.items():
        if len(value) >= 1:
            result[key] = value


    return result


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
        {"name": "Bill Gates", "birthday": datetime(1955, 1, 3).date()},
        {"name": "Yuliia Melnychenko", "birthday": datetime(1988, 9, 14).date()},
        {"name": "Serhii Morozov", "birthday": datetime(1981, 1, 2).date()},
        {"name": "Marharyta Morozova", "birthday": datetime(2020, 12, 25).date()},
        {"name": "Richard Cat", "birthday": datetime(2022, 12, 31).date()},
        {"name": "Other Cat", "birthday": datetime(2021, 12, 31).date()},
        {"name": "OneMoreCat Cat", "birthday": datetime(2014, 12, 30).date()}
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
