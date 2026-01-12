# Copyright (c) 2026, sathwik and contributors
# For license information, please see license.txt

import frappe
import random
from frappe.model.document import Document

class AirplaneTicket(Document):

    def before_insert(self):

        random_num = random.randint(10, 99)
        random_str = random.choice("ABCDE")
        self.seat = f"{random_num}{random_str}"

    def validate(self):
     
        self.calculate_total_price()
        self.ensure_unique_addons()

    def calculate_total_price(self):
        add_ons_cost = 0
        for row in self.add_ons:
            add_ons_cost += row.amount
        
        self.total_amount = (self.flight_price or 0) + add_ons_cost

    def ensure_unique_addons(self):
      
        existing_addons = []
        for row in self.add_ons:
            if row.item in existing_addons:
                frappe.throw(f"Add-on {row.item} is already added!")
            existing_addons.append(row.item)