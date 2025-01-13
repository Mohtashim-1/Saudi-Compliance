import frappe
from frappe import _

def execute(filters=None):
    columns = [
        _("DEST-ID") + ":Data:120",
        _("ESTB-ID") + ":Data:120",
        _("BANK-ACC") + ":Data:120",
        _("32A-CCY") + ":Data:120",
        _("32A-VAL") + ":Date:120",
        _("32A-AMT") + ":Currency:120",
        _("D-DATE") + ":Date:120",
        _("FILE-REF") + ":Data:120",
        _("FILE-REJCDE") + ":Data:120",
        _("MOL-ESTBID") + ":Data:120"
    ]

    # Form the SQL query to fetch the data
    query = """
    SELECT
        e.bank_ac_no AS dest_id,  -- Bank account number from Employee doctype
        e.bank_ac_no AS dest_id,  -- Bank account number from Employee doctype
		e.bank_ac_no AS dest_id,  -- Bank account number from Employee doctype
        # b.custom_established_id AS bank_acc,
        ss.currency AS 32a_ccy,
        ss.posting_date AS 32a_val,
        ss.net_pay AS 32a_amt,
        NULL AS d_date,
        NULL AS file_ref,
        NULL AS file_rej,
        NULL AS mol_established
    FROM `tabSalary Slip` ss
    LEFT JOIN `tabEmployee` e ON e.name = ss.employee
    WHERE ss.docstatus = 0
    AND ss.posting_date = %(posting_date)s
    """
    
    # Fix indentation here:
    data = frappe.db.sql(query, values={"posting_date": filters.get("posting_date")}, as_dict=True)

    return columns, data
