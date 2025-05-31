# type_safe_date_demo.py
from book_utils import Catch
from type_safe_date import Month, Day, Year, Date

print(
    Date(Year(2025), Month.FEBRUARY, Day(28))
)

# Look up by month number
print(
    Date(Year(2025), Month.number(4), Day(30))
)

# Invalid day for February
with Catch():
    Day.of(Month.FEBRUARY, 30)

# Invalid year
with Catch():
    Year(0)
