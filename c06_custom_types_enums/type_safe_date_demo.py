# type_safe_date_demo.py
from type_safe_date import Month, Date

d1 = Date(2025, Month.JANUARY, 31)
print(d1)  # 2025-01-31

d2 = Date(2025, Month.FEBRUARY, 28)
print(d2)  # 2025-02-28
# Invalid day for February
try:
    Date(2025, Month.FEBRUARY, 30)
except ValueError as e:
    print(e)  # Invalid day 30 for month 2

# Invalid year
try:
    Date(0, Month.JANUARY, 1)
except ValueError as e:
    print(e)  # Invalid year: 0

# Lookup by month number
month = Month.number(4)
d3 = Date(2025, month, 30)
print(d3)  # 2025-04-30
