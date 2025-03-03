"""
This script is created load the config.html as the Python REST frontend. The script will supply the JSON as the response to certain endpoints.

Usage

    python config_html_rest_test.py

Dependencies from pip:
 - flask
"""

import json
from flask import Flask
import os


script_directory = os.path.dirname(os.path.realpath(__file__))
config_html_path = os.path.join(script_directory, '..', 'src', 'html', 'config.html')
dashboard_html_path = os.path.join(script_directory, '..', 'src', 'html', 'dashboard.html')
static_folder = os.path.join(script_directory, '..', 'src', 'html')

app = Flask(__name__,
            static_url_path='',
            static_folder=static_folder)


@app.route('/rest/scale_config')
def rest_scale_config():
    return '{"unit":"gram"}'


@app.route('/rest/charge_mode_config')
def rest_charge_mode_config():
    return '{"coarse_kp":0.200000,"coarse_ki":0.000000,"coarse_kd":1.000000,"fine_kp":5.000000,"fine_ki":0.000000,"fine_kd":20.000000,"error_margin_grain":0.030000,"zero_sd_margin_grain":0.020000,"zero_mean_stability_grain":0.040000}'


@app.route('/rest/wireless_config')
def rest_wireless_config():
    return '{"ssid":"YYYY","pw":"xxx","auth":"CYW43_AUTH_WPA2_AES_PSK","timeout_ms":30000,"configured":true}'

@app.route('/rest/eeprom_config')
def rest_eeprom_config():
    return '{"unique_id":"4C64A49","save_to_eeprom":false}'


@app.route('/rest/fine_motor_config')
def rest_fine_motor_config():
    return """{"accel":100.000000,"full_steps_per_rotation":200,"current_ma":800,"microsteps":256,"max_speed_rps":5,"r_sense":110,"min_speed_rps":0.080,"inv_en":false,"inv_dir":false}"""


@app.route('/rest/coarse_motor_config')
def rest_coarse_motor_config():
    return """{"accel":100.000000,"full_steps_per_rotation":200,"current_ma":800,"microsteps":256,"max_speed_rps":3,"r_sense":110,"min_speed_rps":0.020,"inv_en":false,"inv_dir":false}"""


@app.route('/rest/system_control')
def rest_system_control():
    return """{"unique_id":"8178C61","save_to_eeprom":false,"software_reset":false,"erase_eeprom":false}"""


@app.route('/rest/neopixel_led_config')
def rest_neopixel_led_config():
    return """{"12864bl":"#ffffff","led1_c1":"#0f0f0f","led1_c2":"#ffff00","led2_c1":"#0f0f0f","led2_c2":"#00ffff"}"""


@app.route("/config")
def config():
    with open(config_html_path) as fp:
        config_page = fp.read()
    return config_page


@app.route('/')
def dashboard():
    with open(dashboard_html_path) as fp:
        dashboard_page = fp.read()
    return dashboard_page


app.run(debug=True)
