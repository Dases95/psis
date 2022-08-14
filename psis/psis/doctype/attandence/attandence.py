# Copyright (c) 2022, dases and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Attandence(Document):
	def before_save(self):
		for i,student in enumerate( self.attandence_item):
			if student.is_present == 1: 
				number = 1
				if student.paye_today == 1:
					number = -4
				frappe.db.sql("""
					update `tabEtudiant Item` 
						set not_payed = %(number)s 
					where parent = %(parent)s
							and student = %(student)s
								""",
					{
							'number' : student.course_number + number,
							'parent': self.groupe,
							'student': student.etudiant
					})


	
@frappe.whitelist()	
def get_student(group_name):
	return frappe.get_doc('Groupe',group_name).students