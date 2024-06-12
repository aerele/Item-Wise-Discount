frappe.ui.form.on('Sales Order', {
	custom_apply_discount(frm) {
		if(cur_frm.doc.ignore_pricing_rule){
			let item_list = frm.doc.items.map((row)=>row.item_code);
			if(!item_list) return;
			if (frm.doc.customer){
				frappe.call({
					method: "item_wise_discount.api.get_item_discount",
					args:{
						"customer": frm.doc.customer,
						"date": frm.doc.transaction_date,
						"items": item_list
					},
					callback(res){
						if(res.exc)return;
						if(!res.message)return;

						for(let row of frm.doc.items){
							if(row.item_code in res.message){
								frappe.model.set_value(row.doctype, row.name, "discount_percentage", res.message[row.item_code].value);
								frappe.model.set_value(row.doctype, row.name, "custom_applied_discounts", res.message[row.item_code].discount_list.join(', '));
							}
						}
					}
				})
			}
		}
	}
})

frappe.ui.form.on('Sales Order Item', {
	item_code(frm, cdt, cdn) {
		let row = locals[cdt][cdn];
		if(cur_frm.doc.ignore_pricing_rule){
			frappe.model.trigger("qty", frm.doc.name, row)
		}
	},

	qty: function(frm, cdt, cdn){
		let row = locals[cdt][cdn];
		if (frm.doc.customer){
			frappe.call({
				method: "item_wise_discount.api.get_item_discount",
				args:{
					"customer": frm.doc.customer,
					"date": frm.doc.transaction_date,
					"items": [row.item_code]
				},
				callback(res){
					if(res.exc)return;
					if(!res.message)return;
					setTimeout(() => {
						frappe.model.set_value(row.doctype, row.name, "discount_percentage", res.message[row.item_code].value);
						frappe.model.set_value(row.doctype, row.name, "custom_applied_discounts", res.message[row.item_code].discount_list.join(', '))
					}, 1000)
				}
			})
		}
	}
})