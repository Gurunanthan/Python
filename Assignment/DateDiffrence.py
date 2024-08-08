from datetime import date

date1 = date(2020, 7, 2)
date2 = date(2024, 7, 11)

diff = date2 - date1

print(f"{diff.days} days")
