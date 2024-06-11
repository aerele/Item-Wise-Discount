
import frappe

def after_migrate():
    remove_custom_fields()

def remove_custom_fields():
	try:
		frappe.db.delete("Custom Field", "Sales Invoice-custom_apply_discount")
	except Exception as e:
		pass