frappe.ui.form.on('Sales Invoice', {
	custom_apply_discount(frm) {
	    let item_list = frm.doc.items.map((row)=>row.item_code);
	    if(!item_list) return;

		frappe.call({
		    method: "item_wise_discount.api.get_item_discount",
		    args:{
		        "customer": frm.doc.customer,
		        "date": frm.doc.posting_date,
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
})

frappe.ui.form.on('Sales Invoice Item', {
	item_code(frm, cdt, cdn) {
		let row = locals[cdt][cdn];
		frappe.model.trigger("qty", frm.doc.name, row)
	},

	qty(frm, cdt, cdn) {
	    let row = locals[cdt][cdn];
	    if(row.item_code){
	        frappe.call({
	            method: "item_wise_discount.api.get_item_discount",
	            args:{
	                "customer": frm.doc.customer,
	                "date": frm.doc.posting_date,
	                "items": [row.item_code]
	            },
				async: false,
	            callback(res){
	                if(res.exc)return;
					if(!res.message)return;

					if(!row.custom_applied_discounts){
						setTimeout(() => {
							frappe.model.set_value(row.doctype, row.name, "discount_percentage", res.message[row.item_code].value);
							frappe.model.set_value(row.doctype, row.name, "custom_applied_discounts", res.message[row.item_code].discount_list.join(', '))
						}, 1000)
					}
	            }
	        })
	    }
	}
})