# Copyright (c) 2026, Sri Ragul and Contributors
# See license.txt

# import frappe
from frappe.tests import IntegrationTestCase


# On IntegrationTestCase, the doctype test records and all
# link-field test record dependencies are recursively loaded
# Use these module variables to add/remove to/from that list
EXTRA_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]
IGNORE_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]



class IntegrationTestProductstest(IntegrationTestCase):
	"""
	Integration tests for Productstest.
	Use this class for testing interactions between multiple components.
	"""

	pass
