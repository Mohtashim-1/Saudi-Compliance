// Copyright (c) 2025, mohtashim and contributors
// For license information, please see license.txt

frappe.query_reports["WPS Report"] = {
	"filters": [
		{
            "fieldname": "posting_date",
            "label": __("Posting Date"),
            "fieldtype": "Date",
            "default": frappe.datetime.get_today(),
            "reqd": 1,
        }
	]
};
