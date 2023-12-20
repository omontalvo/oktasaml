from datetime import datetime, timezone

# Get current UTC time
utc_now = datetime.now(timezone.utc)

print("Current UTC Time:", utc_now)
