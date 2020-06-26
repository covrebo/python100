from datetime import datetime
from datetime import date
from datetime import timedelta

# Calculating the days until Christmas
today_date = date.today()

christmas = date(2020, 12, 25)

days_until_christmas = (today_date - christmas).days

# print(f'days_until_christmas = {days_until_christmas}')

# if today_date == christmas:
#     print('Today is Christmas!')
# elif days_until_christmas > 0:
#     print(f'Christmas is coming! It will be here in {days_until_christmas} days! :)')
# elif days_until_christmas < 0:
#     print(f'Christmas has passed. It was {abs(days_until_christmas)} days ago. :(')

# Calculating the days until EOL
asset_lifespan = timedelta(days=1825)
print(str(asset_lifespan))
asset_purchase_date = date(2018, 7, 1)
asset_eol = asset_purchase_date + asset_lifespan
print(f'This asset will reach end of life on {str(asset_eol)}')
print(f'There are {asset_eol - today_date} days left until replacement')