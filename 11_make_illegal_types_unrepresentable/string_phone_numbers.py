# string_phone_numbers.py
# Some problematic formats
phone_numbers: list[str] = [
    "5551234",         # No formatting – unclear area code
    "555-1234",        # US format, but without area code
    "(555) 123-4567",  # US format with punctuation
    "555.123.4567",    # Inconsistent punctuation
    "+1-555-123-4567", # International format
    "+44 20 7946 0958",# UK format – space-separated
    "5551234567",      # No formatting at all
    "555 1234",        # Ambiguous – local format?
    "555-12ab",        # Invalid characters
    "CallMeMaybe",     # Completely invalid
    "01234",           # Leading zero – looks like a zip code
    "",                # Empty string
    " 5551234 ",       # Whitespace issues
]
