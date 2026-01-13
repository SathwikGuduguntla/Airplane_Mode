import frappe 
import random


import frappe
import random

def execute():
    tickets = frappe.get_all(
        "Airplane Ticket",
        filters={"seat": ["is", "not set"]},
        pluck="name"
    )

    for ticket in tickets:
        random_num = random.randint(10, 99)
        random_str = random.choice("ABCDE")
        seat = f"{random_num}{random_str}"

        frappe.db.set_value(
            "Airplane Ticket",
            ticket,
            "seat",
            seat
        )
