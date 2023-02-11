# Automated Request Management for Odoo

## Introduction

This module for Odoo adds the ability to automate the submission of requests with email notifications.
It streamlines the request process and saves time and effort for both the requester and the recipient. 
The principle of operation of the module is based on the use of a data model **_'rent.requests'_**, which have a method
save data of a customer and send notification on email.
The module implements a server _action_ ***_action_create_request_*** that requires mandatory parameters:
* _custom_name_
* _custom_description_
* _custom_email_tl_
* _custom_name_tl_
* _custom_phone_

With the help of this _action_ a request is created and sent to the mail.

Also, this module has basic html template for create message based on rent model.

## Features

- Automated submission of requests
- Email notifications for requesters and recipients


## Installation Guide

To install the module, follow these steps:

1. Clone the repository from GitHub to directory

2. Restart the Odoo service to apply the changes.

3. Go to the Odoo Apps menu, search for “Automatic acceptance of applications”, and install the module.

4. Configuration options, such as email templates, actions, can be found in the Settings menu in the  _'Technical'_ Section.


## Example usage

To automate the application process in a specific data model, you can use the following ***action***
<body>

    <record id="example_action" model="ir.actions.server">
            <field name="name">Example of send email</field>
            <field name="model_id" ref="model_your_model"/>
            <field name="state">code</field>
             <field name="code">
                 action = env.ref('module_for_test.action_create_request').with_context({
                     'custom_name': "Name",
                     'custom_description': "Description",
                     'custom_email_tl': "Email TL",
                     'custom_name_tl': "Name TL",
                     'custom_phone': "Phone",
                 }).run()
    </field>
    </record>

</body>

where **your_model** is a model, which call this action from. 

Example of request button
<div>

    <menuitem id="menu_send_test_root_yet"
                  name="Example Action"
                  action="example_action"
                  sequence="0"/>

</div>




