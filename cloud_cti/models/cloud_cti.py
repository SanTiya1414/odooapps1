import requests
from odoo import models, fields, api

class CloudCTI(models.Model):
    _name = 'cloud.cti'
    _description = 'Cloud CTI Integration'

    name = fields.Char(string="CTI Name", required=True)
    api_key = fields.Char(string="API Key", required=True)
    phone_number = fields.Char(string="Phone Number", required=True)
    iframe_url = fields.Char(string="Iframe URL", default="https://sf-sandbox.doocti.com/")

    @api.model
    def initiate_call(self, phone_number):
        url = "https://api.yourcti.com/initiate_call"
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        payload = {
            'phone_number': phone_number,
            'from': self.phone_number
        }
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            return True
        else:
            return False

    @api.model
    def log_call(self, call_data):
        # Log call details in Odoo
        pass

