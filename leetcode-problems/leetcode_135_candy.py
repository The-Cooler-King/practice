ratings = [1,3,2,2,1,3,3,3,1]

def identify_trend(current_rating, previous_rating, previous_trend):
    if current_rating > previous_rating:
        return "ascending"
    elif current_rating < previous_rating:
        return "descending"
    else:
        if previous_trend in ["descending", "valley_floor"]:
            return "valley_floor"
        else:
            return "descending"



last_child = len(ratings) - 1

for child, rating in enumerate(ratings):

    if child == 0:
        previous_rating = rating
        previous_trend = "descending"
        print(f"At child index {child} the current trend is descending.")
    elif child == last_child:
        trend = identify_trend(current_rating=rating,
                             previous_rating=previous_rating,
                             previous_trend=previous_trend)
        print(f"At child index {child} the current trend is {trend}.")
        previous_trend = trend
        previous_rating = rating
    else:
        trend = identify_trend(current_rating=rating,
                               previous_rating=previous_rating,
                               previous_trend=previous_trend)
        print(f"At child index {child} the current trend is {trend}.")
        previous_trend = trend
        previous_rating = rating