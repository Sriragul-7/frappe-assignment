// Copyright (c) 2026, Sri Ragul and contributors
// For license information, please see license.txt

frappe.ui.form.on("Room", {
	room_type(frm) {
        if(!frm.doc.room_type) return;

        frappe.db.get_doc("Room Type",frm.doc.room_type)
        .then(room_type =>{
            frm.set_value("capacity",room_type.capacity)
        })
	},
});


