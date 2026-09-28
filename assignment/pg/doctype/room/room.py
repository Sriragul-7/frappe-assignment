# Copyright (c) 2026, Sri Ragul and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Room(Document):
	
	def before_insert(self): 	
		self.name = f"{self.floor}-{self.room_no}"
