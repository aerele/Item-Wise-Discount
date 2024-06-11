import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def after_install():
	make_custom_fields()

def make_custom_fields():
	custom_fields = {
		"Sales Order Item": [
			dict(
				fieldname="custom_applied_discounts",
				label="Applied Discounts",
				fieldtype="Small Text",
				insert_after="discount_percentage",
				read_only=1
			)
		],
		"Sales Invoice Item": [
			dict(
				fieldname="custom_applied_discounts",
				label="Applied Discounts",
				fieldtype="Small Text",
				insert_after="discount_percentage",
				read_only=1
			)
		],
	}
	create_custom_fields(custom_fields)