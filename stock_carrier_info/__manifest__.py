# Copyright 2021 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Stock Carrier Info",
    "version": "15.0.1.0.0",
    "category": "Stock",
    "license": "AGPL-3",
    "author": "Quartile Limited",
    "website": "https://www.quartile.co/",
    "depends": ["delivery","stock"],
    "data": [
        "security/ir.model.access.csv",
        "views/stock_carrier_info_views.xml",
        "views/stock_picking_view.xml",
    ],
    "installable": True,
}
