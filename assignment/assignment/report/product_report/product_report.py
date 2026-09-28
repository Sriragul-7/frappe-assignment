import frappe


def execute(filters=None):
    columns = [
        {
            "label": "Product Name",
            "fieldname": "product_name",
            "fieldtype": "Data"
        },
        {
            "label": "Product Code",
            "fieldname": "product_code",
            "fieldtype": "Data"
        },
        {
            "label": "Price",
            "fieldname": "price",
            "fieldtype": "Currency"
        },
        {
            "label": "Category",
            "fieldname": "category",
            "fieldtype": "Data"
        }
    ]

    data = frappe.db.sql("""
        SELECT
            product_name,
            product_code,
            price,
            category
        FROM `tabProduct`
        WHERE price > 100
        LIMIT 10
    """, as_dict=True)

    return columns, data