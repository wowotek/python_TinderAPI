import json

import requests

import tinder_api.utils.fb_auth

fb_email = "fb_name"
fb_password = "fb_pass"
#fb_auth_token = utils.fb_auth.get_fb_access_token(fb_email, fb_password)
#fb_user_id = utils.fb_auth.get_fb_id(fb_auth_token)

tinder_token = "30c03661-e03b-4aa0-ac63-62b32755a2c3"

headers = {
    'app_version': '6.9.4',
    'platform': 'ios',
    'content-type': 'application/json',
    'User-agent': 'Tinder/7.5.3 (iPohone; iOS 10.3.2; Scale/2.00)',
    'X-Auth-Token': tinder_token,
}

host = 'https://api.gotinder.com'