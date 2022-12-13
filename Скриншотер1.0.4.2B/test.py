import random
from datetime import datetime, timedelta, time

# min_year=1900
# max_year=datetime.now().year

# start = datetime(min_year, 1, 1, 00, 00, 00)
# years = max_year - min_year+1
# end = start + timedelta(days=365 * years)

# for i in range(10):
#     random_date = start + (end - start) * random.random()
#     print(random_date)

#done

# or a function


print(gen_datetime().strftime('%H:%M'))