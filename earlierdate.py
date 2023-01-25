def compare_dates(month1, day1, year1, month2, day2, year2):

    if year1 < year2:
        return "before"
    elif year1 > year2:
        return "after"
    else:
        if month1 < month2:
            return "before"
        elif month1 > month2:
            return "after"
        else:
            if day1 < day2:
                return "before"
            elif day1 > day2:
                return "after"
            else:
                return "same"
