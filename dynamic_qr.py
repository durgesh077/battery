import os
import tempfile
import obspython as obs
from zepto_qr.qr_funcs import generate_dynamic_qr_code_img

# Global variables
source_name = "dynamicQR"
update_interval =  0.1 # Seconds
temp_qr_code_path = ""

def script_description():
    return "This script generates a live QR code containing the current date and time and displays it on an OBS source."

def script_properties():
    props = obs.obs_properties_create()
    
    # Add a text field for the source name with the default value
    source_name_prop = obs.obs_properties_add_text(props, "source_name", "Source Name", obs.OBS_TEXT_DEFAULT)
    obs.obs_property_set_description(source_name_prop, "Enter the name of the image source to display the QR code.")
    obs.obs_property_set_long_description(source_name_prop, "Default is 'dynamicQR'")
    # obs.obs_property_set_string(source_name_prop, source_name)  # Set the default value
    
    return props


def script_update(settings):
    global source_name, update_interval, temp_qr_code_path
    source_name = obs.obs_data_get_string(settings, "source_name")
    # Generate a temporary file path for the QR code
    temp_qr_code_path = os.path.join(tempfile.gettempdir(), "live_dynamic_qr_code.png")
    
    # Start the timer for live updates
    obs.timer_remove(update_qr_code)  # Remove any existing timers
    obs.timer_add(update_qr_code, int(update_interval * 1000))

def script_load(settings):
    """Called when the script is loaded into OBS."""
    global temp_qr_code_path
    obs.obs_data_set_default_string(settings, "source_name", "dynamicQR")
    temp_qr_code_path = os.path.join(tempfile.gettempdir(), "live_dynamic_qr_code.png")
    print("Live QR Code script loaded.")

def script_unload():
    # Remove the timer and clean up temporary files
    obs.timer_remove(update_qr_code)
    # if os.path.exists(temp_qr_code_path):
    #     os.remove(temp_qr_code_path)

def update_qr_code():
    global temp_qr_code_path, source_name
    if not source_name:
        if not temp_qr_code_path:
            source_name = "dynamicQR"
        else:
            print(f"Error: Source name not specified.")
            return

    qr_image = generate_dynamic_qr_code_img()
    
    # Save the QR code to the temporary file
    qr_image.save(temp_qr_code_path)
    
    # Update the OBS source with the new QR code
    source = obs.obs_get_source_by_name(source_name)
    if source:
        settings = obs.obs_source_get_settings(source)
        obs.obs_data_set_string(settings, "file", temp_qr_code_path)
        obs.obs_source_update(source, settings)
        obs.obs_data_release(settings)
        obs.obs_source_release(source)
    else:
        print(f"Error: Source '{source_name}' not found. Bye...")
