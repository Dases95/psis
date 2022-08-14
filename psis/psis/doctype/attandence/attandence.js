// Copyright (c) 2022, dases and contributors
// For license information, please see license.txt

frappe.ui.form.on('Attandence', {
	// refresh: function(frm) {

	// }
	groupe: function (frm) {
		 frm.call({
			method: 'get_student',
			args:{group_name:frm.doc.groupe}
		}).then(r=>{			
			for(let row of r.message){
				var child = frm.add_child('attandence_item')
				child.etudiant = row.student;
				child.course_number = row.not_payed;	

			}
			console.log(r.message);
			frm.refresh_field('attandence_item')
		})		
	}
});
