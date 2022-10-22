"""Constants for rako."""
# Base component constants
NAME = "Rako"
DOMAIN = "rako"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.0.1"
ISSUE_URL = "https://github.com/boshjosh1918/hacs-rako/issues"

# Device classes
BINARY_SENSOR_DEVICE_CLASS = "connectivity"

# Platforms
LIGHT = "light"
PLATFORMS = [LIGHT]


# Configuration and options
CONF_ENABLED = "enabled"
CONF_USERNAME = "username"
CONF_PASSWORD = "password"

# Defaults
DEFAULT_NAME = DOMAIN


STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""
