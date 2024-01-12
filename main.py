from datetime import date, datetime, timedelta


def get_birthdays_per_week(users):
    list_of_dates_in_week = []
    Monday = []
    Tuesday = []
    Wednesday = []
    Thursday = []
    Friday = []
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
    
    for days in range (start_day, end_day): 
        day_interval = timedelta(days)
        today_plus_days = date_today + day_interval
        list_of_dates_in_week.append(today_plus_days)
    
    start_day_date = date_today + timedelta(start_day)
         
    for person in users:
        for value in person.values():
            if isinstance(value, date):
                BD_replaced_year = value.replace(year=start_day_date.year)
                one_week_later = start_day_date + timedelta(days=7)
                if start_day_date <= BD_replaced_year <= one_week_later:
                    print(f"{value} - a birthday comes this week")
                    bd_name = person["name"]
                    for i in list_of_dates_in_week:
                        if BD_replaced_year == i:
                            weekday_this_day = BD_replaced_year.weekday()
                            if weekday_this_day == 0:
                                Monday.append(bd_name)
                                result["Monday"] = Monday
                            elif weekday_this_day == 1:
                                Tuesday.append(bd_name)
                                result["Tuesday"] = Tuesday
                            elif weekday_this_day == 2:
                                Wednesday.append(bd_name)
                                result["Wednesday"] = Wednesday
                            elif weekday_this_day == 3:
                                Thursday.append(bd_name)
                                result["Thursday"] = Thursday
                            elif weekday_this_day == 4:
                                Friday.append(bd_name)
                                result["Friday"] = Friday
                            elif weekday_this_day == 5:
                                Monday.append(bd_name)
                                result["Monday"] = Monday
                            elif weekday_this_day == 6:
                                Monday.append(bd_name)
                                result["Monday"] = Monday
                            else:
                                print("smth went wrong")
                        else:
                            continue
                else:
                    print("BD not this week")
            else:
                pass
    return result


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
