from datetime import datetime, timedelta
import inflect

def number_to_words(number):
    p = inflect.engine()
    return p.number_to_words(number).capitalize()

def lookback(days):
    p = inflect.engine()
    days_in_words = p.number_to_words(days).capitalize()

    start_date = datetime.now() - timedelta(days=days)
    end_date = datetime.now()

    # Generate all dates in the range
    dates_in_range = [start_date + timedelta(days=x) for x in range((end_date-start_date).days + 1)]

    # Format dates and join them with '%20OR%20'
    range_uuid = '%20OR%20'.join(date.strftime('%Y%m%d') for date in dates_in_range)

    range_file_name = f'{range_uuid}'  # replace with your actual file naming convention
    range_link = ("[" + days_in_words + "-Day Look back at ZK](thearchive://match/%23proofing%20" + range_file_name + ")")
    return range_link

if __name__ == "__main__":
    print(lookback(3))