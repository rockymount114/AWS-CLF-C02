from datetime import datetime, timezone
from zoneinfo import ZoneInfo

NY_TZ = ZoneInfo('America/New_York')

def get_ny_now():
    """Returns current naive UTC datetime for standardized database storage."""
    return datetime.now(timezone.utc)

def format_ny_date(dt, fmt=None):
    """Converts naive UTC or timezone-aware datetime to America/New_York (EDT/EST) and formats it."""
    if not dt:
        return 'N/A'
    if isinstance(dt, str):
        try:
            dt = datetime.fromisoformat(dt)
        except Exception:
            return dt
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    ny_dt = dt.astimezone(NY_TZ)
    tz_name = ny_dt.strftime('%Z')
    if fmt:
        return ny_dt.strftime(fmt)
    return ny_dt.strftime(f'%b %d, %Y %H:%M {tz_name}')
