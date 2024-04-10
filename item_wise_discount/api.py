import frappe
from json import loads

@frappe.whitelist()
def get_item_discount(customer, date, items):
	items = loads(items)
	res_data = {}
	discount_list = frappe.db.get_all("Item Discount Scheme", {"customer": customer, "disable": 0, "start_date":["<=", date], 'end_date':[">=", date]}, pluck='name')

	if not discount_list:
		return res_data

	for item in items:

		percentage_list = frappe.db.sql(f""" select discount_percentage from `tabDiscount Scheme Item` where item_code='{item}' and parent in ('{"', '".join(discount_list)}') """)
		if not percentage_list:
			continue

		discount_percentage = 1
		for percent in percentage_list:
			discount_percentage *= 1-(percent[0]/100)

		res_data[item] = {}
		res_data[item]["value"] = (1 - discount_percentage) * 100
		res_data[item]["discount_list"] = ["{0}%".format(i[0]) for i in percentage_list]
	return res_data