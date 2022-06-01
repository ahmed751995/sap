# Copyright (c) 2022, ahmed and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from sap.qr_generator import get_qr

class ProductOrder(Document):
	def before_save(self):
            self.selected_product = []
            for item in self.product_details:
                data = {
                    'document_no': self.document_no,
                    'customer_no': self.customer_no,
                    'customer_name': self.customer_name,
                    'quantity': item.item_quantity,
                    'length': self.length
                }
                
                item.qr_code = get_qr(data)
