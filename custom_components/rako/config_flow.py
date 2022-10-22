from homeassistant import config_entries
from homeassistant.helpers.selector import selector
from .const import DOMAIN


class RakoConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Rako config flow."""

    async def async_step_user(self, user_input=None):
        # Specify items in the order they are to be displayed in the UI
        data_schema = {
            vol.Required("ip"): str,
            vol.Required("username", default="admin"): str,
            vol.Required("password", default="microchip"): str,
        }

        if self.show_advanced_options:
            data_schema["allow_groups"] = selector({
                "select": {
                    "options": ["all", "light", "switch"],
                }
            })

        return self.async_show_form(step_id="init", data_schema=vol.Schema(data_schema))
