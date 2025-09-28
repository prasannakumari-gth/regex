import re

# PAN regex pattern
pan_pattern = re.compile(r'^[A-Z]{3}[ABCFGHJLPT][A-Z]\d{4}[A-Z]$', re.I)

def is_valid_pan(pan: str) -> bool:
    """Check if the given string is a valid PAN number."""
    return bool(pan_pattern.match(pan.strip()))

# ---- Test cases ----
test_pans = [
    "ABCDE1234F",   # ✅ Valid
    "abcde1234f",   # ✅ Valid (case-insensitive)
    "ABCPD1234X",   # ✅ Valid
    "ABCD1234E",    # ❌ Invalid (4th letter must be type code)
    "ABCDE123F",    # ❌ Invalid (only 3 digits)
    "ABCDE12345F",  # ❌ Invalid (5 digits)
    "ABCDE1234",    # ❌ Missing last letter
]

for pan in test_pans:
    print(f"{pan:12} -> {is_valid_pan(pan)}")
