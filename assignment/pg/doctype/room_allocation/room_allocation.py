# Copyright (c) 2026, Sri Ragul and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class RoomAllocation(Document):
	def validate(self):

		room = frappe.db.get_doc("Room", self.room)

		allocated = frappe.db.count("Room Allocation",{
			"room" : self.room,
			"docstatus": 1,
			"allocation_status": "Active"

		})

		if room.capacity == allocated:
			frappe.throw("Room is fully occupied")
