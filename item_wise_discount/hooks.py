app_name = "item_wise_discount"
app_title = "Item Wise Discount"
app_publisher = "Aerele Technologies"
app_description = "Custom app for applying multiple item wise discount"
app_email = "venkatesh@aerele.in"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/item_wise_discount/css/item_wise_discount.css"
# app_include_js = "/assets/item_wise_discount/js/item_wise_discount.js"

# include js, css files in header of web template
# web_include_css = "/assets/item_wise_discount/css/item_wise_discount.css"
# web_include_js = "/assets/item_wise_discount/js/item_wise_discount.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "item_wise_discount/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Sales Order": "public/custom_script/sales_order.js"
    # "Sales Invoice": "public/custom_script/sales_invoice.js",
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "item_wise_discount/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "item_wise_discount.utils.jinja_methods",
# 	"filters": "item_wise_discount.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "item_wise_discount.install.before_install"
after_install = "item_wise_discount.install.after_install"
after_migrate = "item_wise_discount.migrate.after_migrate"


# Uninstallation
# ------------

# before_uninstall = "item_wise_discount.uninstall.before_uninstall"
# after_uninstall = "item_wise_discount.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "item_wise_discount.utils.before_app_install"
# after_app_install = "item_wise_discount.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "item_wise_discount.utils.before_app_uninstall"
# after_app_uninstall = "item_wise_discount.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "item_wise_discount.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"item_wise_discount.tasks.all"
# 	],
# 	"daily": [
# 		"item_wise_discount.tasks.daily"
# 	],
# 	"hourly": [
# 		"item_wise_discount.tasks.hourly"
# 	],
# 	"weekly": [
# 		"item_wise_discount.tasks.weekly"
# 	],
# 	"monthly": [
# 		"item_wise_discount.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "item_wise_discount.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "item_wise_discount.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "item_wise_discount.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["item_wise_discount.utils.before_request"]
# after_request = ["item_wise_discount.utils.after_request"]

# Job Events
# ----------
# before_job = ["item_wise_discount.utils.before_job"]
# after_job = ["item_wise_discount.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"item_wise_discount.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }
