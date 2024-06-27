# /usr/bin/python3
# encoding: utf-8
from datetime import datetime, timedelta

def lookback(days):
    start_date = datetime.now() - timedelta(days=days)
    end_date = datetime.now()
    
    # Ensure dates_in_range is a list of datetime objects
    dates_in_range = [start_date + timedelta(days=x) for x in range((end_date - start_date).days + 1)]

    # Format dates and join them with '%20OR%20'
    range_uuid = ' OR '.join(date.strftime('%Y%m%d') for date in dates_in_range)
    range_file_name = f'{range_uuid}'  # replace with your actual file naming convention
    range_link = ("#proofing " + range_file_name )

    return range_link

# Test the function 
if __name__ == "__main__":
    print(lookback(5))