# type_safe_date_demo.py
from book_utils import Catch
from type_safe_date import Month, Day, Year, Date

print(Date(Year(2025), Month.FEBRUARY, Day(28)))
## 2025-02-28

# Look up by month number
print(Date(Year(2025), Month(4), Day(30)))
## 2025-04-30

with Catch():
    Day.of(Month.FEBRUARY, 30)
## Error: Invalid day 30 for FEBRUARY

with Catch():
    Year(0)
## Error: Invalid year: 0
