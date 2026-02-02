# 🗄️ Schema Report: Lead-To-Order System
**Generated:** 2026-02-02 16:04

---

## 📋 Table: `laddle_checklist`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `INTEGER` | True |
| **sample_timestamp** | `TIMESTAMP` | True |
| **sample_date** | `DATE` | False |
| **laddle_number** | `INTEGER` | False |
| **slag_cleaning_top** | `TEXT` | True |
| **slag_cleaning_bottom** | `TEXT` | True |
| **nozzle_proper_lancing** | `TEXT` | True |
| **pursing_plug_cleaning** | `TEXT` | True |
| **sly_gate_check** | `TEXT` | True |
| **nozzle_check_cleaning** | `TEXT` | True |
| **sly_gate_operate** | `TEXT` | True |
| **nfc_proper_heat** | `TEXT` | True |
| **nfc_filling_nozzle** | `TEXT` | True |
| **plate_life** | `INTEGER` | True |
| **timber_man_name** | `TEXT` | True |
| **laddle_man_name** | `TEXT` | True |
| **laddle_foreman_name** | `TEXT` | True |
| **supervisor_name** | `TEXT` | True |
| **unique_code** | `TEXT` | False |
| **created_at** | `TIMESTAMP` | True |




### 🏷️ Categorical / Allowed Values:
_No categorical columns detected_


### 🔍 Sample Data (First 3 rows):
_No data_

---

## 📋 Table: `hot_coil`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `INTEGER` | False |
| **sample_timestamp** | `TIMESTAMP` | True |
| **sms_short_code** | `TEXT` | True |
| **submission_type** | `TEXT` | True |
| **size** | `TEXT` | True |
| **mill_incharge** | `TEXT` | True |
| **quality_supervisor** | `TEXT` | True |
| **picture** | `TEXT` | True |
| **electrical_dc_operator** | `TEXT` | True |
| **remarks** | `TEXT` | True |
| **strand1_temperature** | `TEXT` | True |
| **strand2_temperature** | `TEXT` | True |
| **shift_supervisor** | `TEXT` | True |
| **unique_code** | `TEXT` | True |
| **created_at** | `TIMESTAMP` | True |
| **updated_at** | `TIMESTAMP` | True |
| **update_link** | `TEXT` | True |




### 🏷️ Categorical / Allowed Values:
_No categorical columns detected_


### 🔍 Sample Data (First 3 rows):
_No data_

---

## 📋 Table: `pipe_mill`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `BIGINT` | False |
| **sample_timestamp** | `TIMESTAMP` | False |
| **size** | `VARCHAR(20)` | True |
| **shift** | `VARCHAR(20)` | True |
| **pipe_mill** | `VARCHAR(30)` | True |
| **turbuse_name** | `VARCHAR(60)` | True |
| **turbine_is_ok** | `VARCHAR(10)` | True |
| **gas_flow_reading** | `VARCHAR(20)` | True |
| **blower_name** | `VARCHAR(60)` | True |
| **blower_is_ok** | `VARCHAR(10)` | True |
| **helper** | `VARCHAR(60)` | True |
| **unique_code** | `VARCHAR(40)` | True |
| **created_at** | `TIMESTAMP` | True |
| **jobtime** | `VARCHAR(20)` | True |
| **production** | `INTEGER` | True |
| **time_start** | `VARCHAR(20)` | True |
| **time_end** | `VARCHAR(20)` | True |
| **section** | `VARCHAR(50)` | True |
| **item_type** | `VARCHAR(50)` | True |
| **thickness** | `VARCHAR(30)` | True |
| **picture** | `TEXT` | True |
| **recoiler_short_code** | `VARCHAR(50)` | True |
| **mill_number** | `VARCHAR(100)` | True |
| **quality_supervisor** | `VARCHAR(100)` | True |
| **mill_incharge** | `VARCHAR(100)` | True |
| **forman_name** | `VARCHAR(100)` | True |
| **fitter_name** | `VARCHAR(100)` | True |
| **remarks** | `TEXT` | True |




### 🏷️ Categorical / Allowed Values:
_No categorical columns detected_


### 🔍 Sample Data (First 3 rows):
_No data_

---

## 📋 Table: `qc_lab_samples`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `BIGINT` | False |
| **sample_timestamp** | `TIMESTAMP` | False |
| **sms_batch_code** | `VARCHAR(20)` | True |
| **furnace_number** | `VARCHAR(20)` | True |
| **sequence_code** | `VARCHAR(5)` | True |
| **laddle_number** | `SMALLINT` | True |
| **shift_type** | `VARCHAR(20)` | True |
| **final_c** | `NUMERIC(5, 3)` | True |
| **final_mn** | `NUMERIC(5, 3)` | True |
| **final_s** | `NUMERIC(5, 3)` | True |
| **final_p** | `NUMERIC(5, 3)` | True |
| **tested_by** | `VARCHAR(60)` | True |
| **remarks** | `TEXT` | True |
| **report_picture** | `TEXT` | True |
| **unique_code** | `VARCHAR(30)` | True |
| **created_at** | `TIMESTAMP` | True |




### 🏷️ Categorical / Allowed Values:
_No categorical columns detected_


### 🔍 Sample Data (First 3 rows):
_No data_

---

## 📋 Table: `fms_leads`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `BIGINT` | False |
| **created_at** | `TIMESTAMP` | True |
| **updated_at** | `TIMESTAMP` | True |
| **lead_no** | `VARCHAR(50)` | True |
| **lead_receiver_name** | `TEXT` | True |
| **lead_source** | `TEXT` | True |
| **company_name** | `TEXT` | True |
| **phone_number** | `TEXT` | True |
| **salesperson_name** | `TEXT` | True |
| **location** | `TEXT` | True |
| **email_address** | `TEXT` | True |
| **state** | `TEXT` | True |
| **address** | `TEXT` | True |
| **nob** | `TEXT` | True |
| **additional_notes** | `TEXT` | True |
| **planned** | `DATE` | True |
| **actual** | `DATE` | True |
| **delay** | `INTEGER` | True |
| **status** | `TEXT` | True |
| **customer_feedback** | `TEXT` | True |
| **enquiry_received_status** | `TEXT` | True |
| **enquiry_received_date** | `DATE` | True |
| **enquiry_approach** | `TEXT` | True |
| **project_approx_value** | `NUMERIC(14, 2)` | True |
| **item_qty** | `TEXT` | True |
| **total_qty** | `INTEGER` | True |
| **next_action** | `TEXT` | True |
| **next_call_date** | `DATE` | True |
| **next_call_time** | `TEXT` | True |
| **planned1** | `DATE` | True |
| **actual1** | `DATE` | True |
| **delay1** | `INTEGER` | True |
| **enquiry_status** | `TEXT` | True |
| **customer_say** | `TEXT` | True |
| **current_stage** | `TEXT` | True |
| **followup_status** | `TEXT` | True |
| **followup_next_call_date** | `DATE` | True |
| **followup_next_call_time** | `TEXT` | True |
| **is_order_received** | `TEXT` | True |
| **acceptance_via** | `TEXT` | True |
| **payment_mode** | `TEXT` | True |
| **payment_terms_days** | `TEXT` | True |
| **transport_mode** | `TEXT` | True |
| **remark** | `TEXT` | True |
| **not_received_reason_status** | `TEXT` | True |
| **not_received_reason_remark** | `TEXT` | True |
| **customer_order_hold_category** | `TEXT` | True |
| **hold_date** | `DATE` | True |
| **hold_remark** | `TEXT` | True |
| **sc_name** | `TEXT` | True |
| **planned_days** | `INTEGER` | True |
| **leadscallingdays** | `TEXT` | True |
| **enquirycallingdays** | `TEXT` | True |
| **orderno** | `VARCHAR(100)` | True |




### 🏷️ Categorical / Allowed Values:
- **`lead_no`** (2 values): `['LD-003', 'LD-004']`
- **`lead_receiver_name`** (2 values): `['Aakash Agrawal', 'TRIPATI RANA']`
- **`lead_source`** (2 values): `['Indiamart', 'WHATSAPP']`
- **`company_name`** (2 values): `['RBP Energy', 'Sourabh Rolling MIlls']`
- **`phone_number`** (2 values): `['9022331100', '9827164305']`
- **`salesperson_name`** (2 values): `['Rakesh Verma', 'sadfsadf']`
- **`location`** (2 values): `['asfasfasf', 'Bilaspur, CG']`
- **`email_address`** (2 values): `['asdfsd@email.com', 'rbp@gmail.com']`
- **`state`** (2 values): `['Arunachal Pradesh', 'Chhattisgarh']`
- **`address`** (2 values): `['asdfasfsa', 'asfdas']`
- **`nob`** (2 values): `['Manufacturing', 'safasd']`
- **`additional_notes`** (2 values): `['asdfdasf', 'fasfasfd']`
- **`status`** (1 values): `['Hot']`
- **`enquiry_received_status`** (1 values): `['yes']`
- **`enquiry_approach`** (2 values): `['INWARD', 'Phone Call']`
- **`item_qty`** (2 values): `['[{"name":"HR STRIP","quantity":"1212"}]', '[{"name":"HR STRIP","quantity":"12121"},{"name":"Fe500D TMT Bar","quantity":"121212"}]']`
- **`next_action`** (1 values): `['awfasdfas']`
- **`next_call_time`** (2 values): `['16:33', '16:34']`
- **`enquiry_status`** (2 values): `['hot', 'open']`
- **`customer_say`** (2 values): `['Customer said quotation under review', 'Reviewing Quote']`
- **`current_stage`** (1 values): `['order-status']`
- **`is_order_received`** (1 values): `['yes']`
- **`acceptance_via`** (1 values): `['email']`
- **`payment_mode`** (2 values): `['neft', 'rtgs']`
- **`payment_terms_days`** (2 values): `['30', '7']`
- **`transport_mode`** (2 values): `['by road', 'road transport']`
- **`remark`** (2 values): `['asfasfas', 'sadfasfda']`
- **`not_received_reason_status`** (1 values): `['project on hold']`
- **`not_received_reason_remark`** (1 values): `['asdfsadf']`
- **`sc_name`** (2 values): `['Amit Pandey', 'ARUN YADAV']`
- **`orderno`** (1 values): `['DO-05']`


### 🔍 Sample Data (First 3 rows):
| id | created_at | updated_at | lead_no | lead_receiver_name | lead_source | company_name | phone_number | salesperson_name | location | email_address | state | address | nob | additional_notes | planned | actual | delay | status | customer_feedback | enquiry_received_status | enquiry_received_date | enquiry_approach | project_approx_value | item_qty | total_qty | next_action | next_call_date | next_call_time | planned1 | actual1 | delay1 | enquiry_status | customer_say | current_stage | followup_status | followup_next_call_date | followup_next_call_time | is_order_received | acceptance_via | payment_mode | payment_terms_days | transport_mode | remark | not_received_reason_status | not_received_reason_remark | customer_order_hold_category | hold_date | hold_remark | sc_name | planned_days | leadscallingdays | enquirycallingdays | orderno |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | 2025-11-25 10:08:09.308770+00:00 | 2025-11-25 11:17:37.644367+00:00 | LD-003 | TRIPATI RANA | WHATSAPP | Sourabh Rolling MIlls | 9827164305 | sadfsadf | asfasfasf | asdfsd@email.com | Arunachal Pradesh | asdfasfsa | safasd | fasfasfd | 2025-11-26 | 2025-11-25 | None | Hot | None | yes | 2025-11-24 | INWARD | 231232.00 | [{"name":"HR STRIP","quantity":"1212"}] | 1212 | awfasdfas | 2025-12-02 | 16:34 | 2025-11-26 | 2025-11-28 | None | hot | Reviewing Quote | order-status | None | None | None | yes | email | rtgs | 7 | by road | sadfasfda | project on hold | asdfsadf | None | None | None | ARUN YADAV | 1 | None | None | None |
| 4 | 2025-11-25 10:45:44.990059+00:00 | 2025-11-28 06:43:38.412729+00:00 | LD-004 | Aakash Agrawal | Indiamart | RBP Energy | 9022331100 | Rakesh Verma | Bilaspur, CG | rbp@gmail.com | Chhattisgarh | asfdas | Manufacturing | asdfdasf | 2025-11-26 | None | None | Hot | None | yes | 2025-11-27 | Phone Call | 21121.00 | [{"name":"HR STRIP","quantity":"12121"},{"name":"F | 133333 | awfasdfas | 2025-11-24 | 16:33 | 2025-11-29 | 2025-11-29 | None | open | Customer said quotation under review | order-status | None | None | None | yes | email | neft | 30 | road transport | asfasfas | None | None | None | None | None | Amit Pandey | 1 | None | None | DO-05 |

---

## 📋 Table: `size_master`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `INTEGER` | False |
| **item_type** | `VARCHAR(100)` | False |
| **size** | `VARCHAR(50)` | False |
| **thickness** | `VARCHAR(50)` | False |




### 🏷️ Categorical / Allowed Values:
- **`item_type`** (3 values): `['rectangular', 'round', 'square']`
- **`size`** (20 values): `['19X19', '20X40', '25 OD', '25X25', '25X50', '25X68', '31X31', '32 OD', '37X56', '38X38', '42 OD', '47X47', '48 OD', '60 OD', '62X62', '72X72', '76 OD', '80X40', '88 OD', '96X48']`
- **`thickness`** (11 values): `['1.2', '1.5', '1.6', '1.9', '2', '2.2', '2.5', '2.7', '2.9', '3', '3.2']`


### 🔍 Sample Data (First 3 rows):
| id | item_type | size | thickness |
| --- | --- | --- | --- |
| 1 | round | 25 OD | 1.2 |
| 2 | round | 25 OD | 1.5 |
| 3 | round | 25 OD | 1.9 |

---

## 📋 Table: `re_coiler`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `BIGINT` | False |
| **sample_timestamp** | `TIMESTAMP` | False |
| **hot_coiler_short_code** | `VARCHAR(10)` | True |
| **size** | `VARCHAR(30)` | True |
| **supervisor** | `VARCHAR(60)` | True |
| **incharge** | `VARCHAR(60)` | True |
| **contractor** | `VARCHAR(60)` | True |
| **machine_number** | `VARCHAR(20)` | True |
| **welder_name** | `VARCHAR(60)` | True |
| **unique_code** | `VARCHAR(50)` | False |
| **created_at** | `TIMESTAMP` | True |




### 🏷️ Categorical / Allowed Values:
_No categorical columns detected_


### 🔍 Sample Data (First 3 rows):
_No data_

---

## 📋 Table: `tundish_checklist`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `INTEGER` | False |
| **sample_timestamp** | `TIMESTAMP` | True |
| **tundish_number** | `INTEGER` | True |
| **nozzle_plate_check** | `TEXT` | True |
| **well_block_check** | `TEXT` | True |
| **board_proper_set** | `TEXT` | True |
| **board_sand_filling** | `TEXT` | True |
| **refractory_slag_cleaning** | `TEXT` | True |
| **tundish_mession_name** | `TEXT` | True |
| **handover_proper_check** | `TEXT` | True |
| **handover_nozzle_installed** | `TEXT` | True |
| **handover_masala_inserted** | `TEXT` | True |
| **stand1_mould_operator** | `TEXT` | True |
| **stand2_mould_operator** | `TEXT` | True |
| **timber_man_name** | `TEXT` | True |
| **laddle_operator_name** | `TEXT` | True |
| **shift_incharge_name** | `TEXT` | True |
| **forman_name** | `TEXT` | True |
| **unique_code** | `TEXT` | False |




### 🏷️ Categorical / Allowed Values:
_No categorical columns detected_


### 🔍 Sample Data (First 3 rows):
_No data_

---

## 📋 Table: `leads_tracker`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `BIGINT` | False |
| **created_at** | `TIMESTAMP` | True |
| **lead_no** | `VARCHAR(50)` | True |
| **customer_say** | `TEXT` | True |
| **lead_status** | `TEXT` | True |
| **enquiry_received_status** | `TEXT` | True |
| **enquiry_received_date** | `DATE` | True |
| **enquiry_approach** | `TEXT` | True |
| **item_qty** | `JSONB` | True |
| **total_qty** | `INTEGER` | True |
| **next_action** | `TEXT` | True |
| **next_call_date** | `DATE` | True |
| **next_call_time** | `VARCHAR(10)` | True |
| **company_name** | `TEXT` | True |
| **sales_coordinator** | `TEXT` | True |
| **calling_days** | `INTEGER` | True |




### 🏷️ Categorical / Allowed Values:
- **`lead_no`** (2 values): `['LD-003', 'LD-004']`
- **`customer_say`** (2 values): `['Customer said quotation under review', 'Reviewing Quote']`
- **`lead_status`** (1 values): `['Hot']`
- **`enquiry_received_status`** (2 values): `['expected', 'yes']`
- **`enquiry_approach`** (2 values): `['INWARD', 'Phone Call']`
- **`next_action`** (1 values): `['awfasdfas']`
- **`next_call_time`** (2 values): `['16:33', '16:34']`


### 🔍 Sample Data (First 3 rows):
| id | created_at | lead_no | customer_say | lead_status | enquiry_received_status | enquiry_received_date | enquiry_approach | item_qty | total_qty | next_action | next_call_date | next_call_time | company_name | sales_coordinator | calling_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2025-11-25 10:57:54.431151+00:00 | LD-003 | Reviewing Quote | Hot | yes | 2025-11-26 | INWARD | [{'name': 'MS BILLET', 'quantity': '1212'}] | 1212 | None | None | None | None | None | None |
| 2 | 2025-11-25 10:58:25.812082+00:00 | LD-003 | Reviewing Quote | Hot | yes | 2025-11-25 | INWARD | [{'name': 'MS PIPE1', 'quantity': '212'}] | 212 | None | None | None | None | None | None |
| 3 | 2025-11-25 11:01:15.234733+00:00 | LD-003 | Reviewing Quote | Hot | yes | 2025-11-24 | INWARD | [{'name': 'HR STRIP', 'quantity': '1212121'}] | 1212121 | None | None | None | None | None | None |

---

## 📋 Table: `dropdown`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `BIGINT` | False |
| **created_at** | `TIMESTAMP` | True |
| **lead_receiver_name** | `TEXT` | True |
| **lead_source** | `TEXT` | True |
| **state** | `TEXT` | True |
| **quotation_shared_by** | `TEXT` | True |
| **enquiry_status** | `TEXT` | True |
| **acceptance_via** | `TEXT` | True |
| **payment_mode** | `TEXT` | True |
| **not_received_reason_status** | `TEXT` | True |
| **hold_reason_category** | `TEXT` | True |
| **consignee_company_name** | `TEXT` | True |
| **consignee_client_name** | `TEXT` | True |
| **consignee_client_contact_no** | `TEXT` | True |
| **consignee_billing_address** | `TEXT` | True |
| **consignee_state** | `TEXT` | True |
| **consignee_gstin_uin** | `TEXT` | True |
| **consignee_state_code** | `TEXT` | True |
| **sp_name** | `TEXT` | True |
| **reference_contact_no1** | `TEXT` | True |
| **sp_state** | `TEXT` | True |
| **sp_state_code** | `TEXT` | True |
| **sp_pan** | `TEXT` | True |
| **consignor_bank_details** | `TEXT` | True |
| **consignor_state_code** | `TEXT` | True |
| **consignor_gstin** | `TEXT` | True |
| **consignor_msme_no** | `TEXT` | True |
| **lead_assign_to** | `TEXT` | True |
| **requirement_product_category** | `TEXT` | True |
| **sales_coordinator_name** | `TEXT` | True |
| **nob** | `TEXT` | True |
| **enquiry_approach** | `TEXT` | True |
| **requirement_product_category_codes** | `TEXT` | True |
| **live_company_name** | `TEXT` | True |
| **live_person_name** | `TEXT` | True |
| **live_mobile** | `TEXT` | True |
| **live_email_address** | `TEXT` | True |
| **live_address** | `TEXT` | True |
| **live_sc_name** | `TEXT` | True |
| **live_source** | `TEXT` | True |
| **direct_company_name** | `TEXT` | True |
| **direct_client_name** | `TEXT` | True |
| **direct_client_contact_no** | `TEXT` | True |
| **direct_state** | `TEXT` | True |
| **direct_billing_address** | `TEXT` | True |
| **item_code** | `TEXT` | True |
| **item_category** | `TEXT` | True |
| **item_name** | `TEXT` | True |
| **payment_terms_days** | `TEXT` | True |
| **transport_mode** | `TEXT` | True |
| **freight_type** | `TEXT` | True |
| **payment_terms** | `TEXT` | True |
| **enquiry_receiver_name** | `TEXT` | True |
| **enquiry_assign_to** | `TEXT` | True |
| **item_list** | `TEXT` | True |
| **rate** | `NUMERIC(12, 2)` | True |
| **description** | `TEXT` | True |
| **prepared_by** | `TEXT` | True |
| **followup_status** | `TEXT` | True |
| **reference_phone_no_2** | `TEXT` | True |
| **what_did_customer_say** | `TEXT` | True |




### 🏷️ Categorical / Allowed Values:
- **`lead_receiver_name`** (5 values): `['Amit Pandey', 'Anil Kumar Mishra', 'Rahul Sharma', 'Sheetal Patel', 'Tripati Rana']`
- **`lead_source`** (6 values): `['Direct Visit', 'Email', 'Indiamart', 'Referral', 'Telephonic', 'Whatsapp']`
- **`state`** (1 values): `['Chhattisgarh']`
- **`quotation_shared_by`** (1 values): `['Rahul Sharma']`
- **`enquiry_status`** (4 values): `['Followup', 'Hot', 'Open', 'Quotation Sent']`
- **`acceptance_via`** (1 values): `['Email']`
- **`payment_mode`** (4 values): `['Cash', 'NEFT', 'RTGS', 'UPI']`
- **`not_received_reason_status`** (5 values): `['Budget Constraints', 'Customer Busy', 'High Price', 'Low Budget', 'Need more time']`
- **`hold_reason_category`** (4 values): `['Budget Issue', 'Customer Documentation Pending', 'Not Interested', 'Project on hold']`
- **`consignee_company_name`** (1 values): `['Hamar Energy Pvt Ltd']`
- **`consignee_client_name`** (1 values): `['Prakash Sharma']`
- **`consignee_client_contact_no`** (1 values): `['9876543210']`
- **`consignee_billing_address`** (1 values): `['Raipur, Chhattisgarh - 492001']`
- **`consignee_state`** (1 values): `['Chhattisgarh']`
- **`consignee_gstin_uin`** (1 values): `['22AABCH1234Q1Z5']`
- **`consignee_state_code`** (1 values): `['22']`
- **`sp_name`** (6 values): `['Aakash', 'Harish', 'Rohit', 'S K Nayak', 'Tarun', 'Vipul']`
- **`reference_contact_no1`** (6 values): `['7723020095', '9000011111', '9876501234', '9898989898', '9993322110', '9999933333']`
- **`sp_state`** (6 values): `['Andhra Pradesh', 'Chhattisgarh', 'demo', 'Madhya Pradesh', 'Maharashtra', 'Odisha']`
- **`sp_state_code`** (5 values): `['21', '22', '23', '27', '36']`
- **`sp_pan`** (5 values): `['ABCDE1234F', 'ABCDE4455Z', 'FGHJK1234X', 'JKLPM9987D', 'MIJLP8877A']`
- **`consignor_bank_details`** (6 values): `['Account No.: 123456789012, HDFC Bank, Raipur', 'Account No.: 733605010000120 Bank Name: Union Bank of India Bank Address: MID CORP BR IFSC CODE: UBIN0573361 Email: marketing@sagartmt.com Website: www.pankajgroup.in', 'Axis Bank, Rourkela', 'Bank of Baroda, Indore', 'ICICI Bank, Nagpur Branch, A/C: 121212121212', 'Union Bank, MID CORP BR, A/C: 733605010000120']`
- **`consignor_state_code`** (5 values): `['21', '22', '23', '27', '36']`
- **`consignor_gstin`** (6 values): `['21ABCDE1111F1Z3', '22AABCH1234Q1Z5', '22AABCT1234E1Z2', '23AACCR1111R1Z2', '27ABCDE1234F1Z5', '36AAICS2367M1Z3']`
- **`consignor_msme_no`** (5 values): `['MSME123456', 'MSME1299', 'MSME55678', 'MSME908776', 'MSME9988']`
- **`lead_assign_to`** (1 values): `['Aakash Agrawal']`
- **`requirement_product_category`** (4 values): `['Angles', 'MS BILLET', 'Rod', 'TMT Bars']`
- **`sales_coordinator_name`** (5 values): `['Arun Yadav', 'Dayanand Kaiwartya', 'Jay Nirmal', 'Mohit Sinha', 'Shubham Pandey']`
- **`nob`** (5 values): `['Construction', 'Fabrication', 'Industrial', 'Manufacturing', 'Rolling']`
- **`enquiry_approach`** (3 values): `['Email', 'Phone', 'Phone Call']`
- **`requirement_product_category_codes`** (5 values): `['ANG-009', 'BLT-002', 'RBT-007', 'TMT-001', 'TMT-016']`
- **`live_company_name`** (6 values): `['Hamar Energy Pvt Ltd', 'MetalWorks India', 'Navkar Metals', 'RBP Energy', 'SRM Mining Pvt Ltd', 'Sunrise Casting']`
- **`live_person_name`** (6 values): `['Devendra Rao', 'Kaushal', 'Niraj', 'Prakash Sharma', 'Rakesh Verma', 'Santosh']`
- **`live_mobile`** (6 values): `['8888888888', '9022331100', '9090909090', '9123456780', '9876543210', '9988776655']`
- **`live_email_address`** (5 values): `['metalworks@gmail.com', 'navkar@gmail.com', 'rbp@gmail.com', 'srm@gmail.com', 'sunrise@gmail.com']`
- **`live_address`** (6 values): `['Bilaspur, CG', 'Indore, MP', 'Nagpur MIDC', 'Raipur, Chhattisgarh - 492001', 'Rourkela', 'Visakhapatnam, AP']`
- **`live_sc_name`** (5 values): `['Arun Yadav', 'Dayanand Kaiwartya', 'Jay Nirmal', 'Mohit Sinha', 'Shubham Pandey']`
- **`live_source`** (5 values): `['Email', 'Exhibition', 'Google Ads', 'Social Media', 'Whatsapp']`
- **`direct_company_name`** (5 values): `['3M Projects Pvt Ltd', 'ABC Steels Pvt Ltd', 'PQR Engineering Ltd', 'Royal Steel Traders', 'Shree Metals Pvt Ltd']`
- **`direct_client_name`** (5 values): `['Ajay Gupta', 'Dharmendra', 'Irfan Khan', 'Manoj Singh', 'Rajesh Verma']`
- **`direct_client_contact_no`** (5 values): `['9001122334', '9033442211', '9765432100', '9823111000', '9988771122']`
- **`direct_state`** (5 values): `['Andhra Pradesh', 'Chhattisgarh', 'Madhya Pradesh', 'Maharashtra', 'Odisha']`
- **`direct_billing_address`** (5 values): `['IDA Plot 4/A, Visakhapatnam', 'Indore Industrial Belt', 'Industrial Area, Raipur', 'MIDC Industrial Area, Nagpur', 'Rourkela Steel Zone']`
- **`item_code`** (6 values): `['ANG-009', 'BLT-002', 'ITM-1001', 'RBT-007', 'TMT-001', 'TMT-016']`
- **`item_category`** (5 values): `['Angles', 'MS Billet', 'Rod', 'Steel Bars', 'TMT Bars']`
- **`item_name`** (5 values): `['8mm Rod', 'Angle 65x65', 'Fe500D TMT Bar', 'Fe550 TMT Bar', 'MS Billet 100mm']`
- **`payment_terms_days`** (6 values): `['0', '1', '15', '30', '30days', '7']`
- **`transport_mode`** (4 values): `['BY ROAD', 'Road Transport', 'Self Pickup', 'Transport']`
- **`freight_type`** (3 values): `['FOR', 'NA', 'Paid']`
- **`payment_terms`** (5 values): `['100% ADVANCE', '50% Advance', 'Advance', 'Advance Payment', 'Immediate']`
- **`enquiry_receiver_name`** (5 values): `['Amit Pandey', 'Anil Kumar Mishra', 'Rahul Sharma', 'Sheetal Patel', 'Tripati Rana']`
- **`enquiry_assign_to`** (6 values): `['Abhishek', 'Akhil', 'Anshul', 'Rahul Sharma', 'Sagar TMT Sales Team', 'Vikas']`
- **`item_list`** (5 values): `['8mm Rod Qty 150', 'Angle 65x65 Qty 50', 'Fe500D TMT BAR - 12mm - Qty 500KG', 'Fe550D TMT - Qty 300KG', 'MS BILLET - 100mm']`
- **`description`** (5 values): `['High quality TMT bars suitable for construction', 'Premium grade TMT for high load', 'Standard billet for rolling mills', 'Standard rod for fabrication', 'Standard steel angle']`
- **`prepared_by`** (1 values): `['Aakash']`
- **`followup_status`** (3 values): `['Followup', 'Pending', 'Reviewing']`
- **`reference_phone_no_2`** (6 values): `['8888811111', '9000022222', '9811167788', '9898989898', '9900990099', '9998877665']`
- **`what_did_customer_say`** (5 values): `['Customer said quotation under review', 'Req: Send revised value', 'Reviewing Quote', 'Wants to negotiate', 'Will revert soon']`


### 🔍 Sample Data (First 3 rows):
| id | created_at | lead_receiver_name | lead_source | state | quotation_shared_by | enquiry_status | acceptance_via | payment_mode | not_received_reason_status | hold_reason_category | consignee_company_name | consignee_client_name | consignee_client_contact_no | consignee_billing_address | consignee_state | consignee_gstin_uin | consignee_state_code | sp_name | reference_contact_no1 | sp_state | sp_state_code | sp_pan | consignor_bank_details | consignor_state_code | consignor_gstin | consignor_msme_no | lead_assign_to | requirement_product_category | sales_coordinator_name | nob | enquiry_approach | requirement_product_category_codes | live_company_name | live_person_name | live_mobile | live_email_address | live_address | live_sc_name | live_source | direct_company_name | direct_client_name | direct_client_contact_no | direct_state | direct_billing_address | item_code | item_category | item_name | payment_terms_days | transport_mode | freight_type | payment_terms | enquiry_receiver_name | enquiry_assign_to | item_list | rate | description | prepared_by | followup_status | reference_phone_no_2 | what_did_customer_say |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | 2025-11-29 10:19:59.898706+00:00 | Rahul Sharma | Email | None | None | Hot | None | RTGS | Budget Constraints | Project on hold | None | None | None | None | None | None | None | Harish | 7723020095 | Andhra Pradesh | 36 | ABCDE4455Z | Union Bank, MID CORP BR, A/C: 733605010000120 | 36 | 36AAICS2367M1Z3 | MSME908776 | None | MS BILLET | Dayanand Kaiwartya | Rolling | Email | BLT-002 | SRM Mining Pvt Ltd | Devendra Rao | 9988776655 | srm@gmail.com | Visakhapatnam, AP | Dayanand Kaiwartya | Whatsapp | 3M Projects Pvt Ltd | Rajesh Verma | 9823111000 | Andhra Pradesh | IDA Plot 4/A, Visakhapatnam | BLT-002 | MS Billet | MS Billet 100mm | 1 | BY ROAD | FOR | 100% ADVANCE | Anil Kumar Mishra | Akhil | MS BILLET - 100mm | 42000.00 | Standard billet for rolling mills | None | Reviewing | 9900990099 | Reviewing Quote |
| 4 | 2025-11-29 10:19:59.898706+00:00 | Tripati Rana | Referral | None | None | Followup | None | UPI | Customer Busy | Customer Documentation Pending | None | None | None | None | None | None | None | Vipul | 9876501234 | Maharashtra | 27 | FGHJK1234X | ICICI Bank, Nagpur Branch, A/C: 121212121212 | 27 | 27ABCDE1234F1Z5 | MSME1299 | None | TMT Bars | Jay Nirmal | Industrial | Email | TMT-016 | Navkar Metals | Santosh | 8888888888 | navkar@gmail.com | Nagpur MIDC | Jay Nirmal | Exhibition | PQR Engineering Ltd | Ajay Gupta | 9001122334 | Maharashtra | MIDC Industrial Area, Nagpur | TMT-016 | TMT Bars | Fe550 TMT Bar | 15 | Transport | Paid | Advance | Rahul Sharma | Vikas | Fe550D TMT - Qty 300KG | 62000.00 | Premium grade TMT for high load | None | Pending | 9811167788 | Req: Send revised value |
| 5 | 2025-11-29 10:19:59.898706+00:00 | Amit Pandey | Direct Visit | None | None | Open | None | Cash | Low Budget | Not Interested | None | None | None | None | None | None | None | Rohit | 9000011111 | Madhya Pradesh | 23 | JKLPM9987D | Bank of Baroda, Indore | 23 | 23AACCR1111R1Z2 | MSME55678 | None | Angles | Mohit Sinha | Construction | Phone | ANG-009 | Sunrise Casting | Kaushal | 9123456780 | sunrise@gmail.com | Indore, MP | Mohit Sinha | Email | Royal Steel Traders | Irfan Khan | 9988771122 | Madhya Pradesh | Indore Industrial Belt | ANG-009 | Angles | Angle 65x65 | 0 | Self Pickup | NA | Immediate | Tripati Rana | Anshul | Angle 65x65 Qty 50 | 52000.00 | Standard steel angle | None | Pending | 9000022222 | Wants to negotiate |

---

## 📋 Table: `make_quotation`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `BIGINT` | False |
| **timestamp** | `TIMESTAMP` | True |
| **quotation_no** | `VARCHAR(100)` | True |
| **quotation_date** | `DATE` | True |
| **prepared_by** | `VARCHAR(255)` | True |
| **consigner_state** | `VARCHAR(150)` | True |
| **reference_name** | `VARCHAR(255)` | True |
| **consigner_address** | `TEXT` | True |
| **consigner_mobile** | `VARCHAR(20)` | True |
| **consigner_phone** | `VARCHAR(20)` | True |
| **consigner_gstin** | `VARCHAR(50)` | True |
| **consigner_state_code** | `VARCHAR(10)` | True |
| **company_name** | `VARCHAR(255)` | True |
| **consignee_address** | `TEXT` | True |
| **ship_to** | `TEXT` | True |
| **consignee_state** | `VARCHAR(150)` | True |
| **contact_name** | `VARCHAR(255)` | True |
| **contact_no** | `VARCHAR(20)` | True |
| **consignee_gstin** | `VARCHAR(50)` | True |
| **consignee_state_code** | `VARCHAR(10)` | True |
| **msme_no** | `VARCHAR(100)` | True |
| **validity** | `VARCHAR(100)` | True |
| **payment_terms** | `VARCHAR(255)` | True |
| **delivery** | `VARCHAR(255)` | True |
| **freight** | `VARCHAR(255)` | True |
| **insurance** | `VARCHAR(255)` | True |
| **taxes** | `VARCHAR(255)` | True |
| **notes** | `TEXT` | True |
| **account_no** | `VARCHAR(100)` | True |
| **bank_name** | `VARCHAR(255)` | True |
| **bank_address** | `TEXT` | True |
| **ifsc_code** | `VARCHAR(50)` | True |
| **email** | `VARCHAR(255)` | True |
| **website** | `VARCHAR(255)` | True |
| **pan** | `VARCHAR(20)` | True |
| **items** | `JSONB` | True |
| **pdf_url** | `TEXT` | True |
| **grand_total** | `NUMERIC(14, 2)` | True |




### 🏷️ Categorical / Allowed Values:
- **`quotation_no`** (5 values): `['QN-003', 'QN-004', 'QN-005', 'QN-006', 'QN-007']`
- **`prepared_by`** (2 values): `['Aakash', 'SHEETAL PATEL']`
- **`consigner_state`** (2 values): `['Andhra Pradesh', 'Chhattisgarh']`
- **`reference_name`** (3 values): `['Rohit', 'SOURABH ROLLING MILLS PVT LTD', 'Vipul']`
- **`consigner_address`** (2 values): `['', 'VILLAGE KANHERA, ACHHOLI ROAD, URLA, RAIPUR, CHHATTISHGARH , 492003, INDIA']`
- **`consigner_mobile`** (3 values): `['6266919126', '9000011111', '9876501234']`
- **`consigner_phone`** (3 values): `['7723020095', '9000022222', '9811167788']`
- **`consigner_gstin`** (3 values): `['22AAICS2367M1Z3', '23AACCR1111R1Z2', '27ABCDE1234F1Z5']`
- **`consigner_state_code`** (3 values): `['22', '23', '27']`
- **`company_name`** (2 values): `['ABC Steels Pvt Ltd', 'Select Company']`
- **`consignee_address`** (2 values): `['Industrial Area, Raipur', 'safsaf']`
- **`ship_to`** (1 values): `['safdsaf']`
- **`consignee_state`** (2 values): `['Chhattisgarh', 'sadfsaf']`
- **`contact_name`** (2 values): `['Manoj Singh', 'safas']`
- **`contact_no`** (2 values): `['1212121212', '9033442211']`
- **`consignee_gstin`** (2 values): `['221312', '22AABCH1234Q1Z5']`
- **`consignee_state_code`** (2 values): `['121', '22']`
- **`msme_no`** (3 values): `['', 'MSME123456', 'MSME908776']`
- **`validity`** (1 values): `['The above quoted prices are valid up to 5 days from date of offer.']`
- **`payment_terms`** (1 values): `['100% advance payment in the mode of NEFT, RTGS & DD']`
- **`delivery`** (1 values): `['Material is ready in our stock']`
- **`freight`** (1 values): `['Extra as per actual.']`
- **`insurance`** (1 values): `["Transit insurance for all shipment is at Buyer's risk."]`
- **`taxes`** (1 values): `['Extra as per actual.']`
- **`notes`** (1 values): `['']`
- **`account_no`** (1 values): `['733605010000120']`
- **`bank_name`** (1 values): `['Union Bank of India']`
- **`bank_address`** (1 values): `['MID CORP BR']`
- **`ifsc_code`** (1 values): `['UBIN0573361']`
- **`email`** (1 values): `['marketing@sagartmt.com']`
- **`website`** (2 values): `['www.pankajgroup.in', 'www.pankajgroup.in']`
- **`pan`** (3 values): `['AAICS2367M', 'ABCDE1234F', 'ABCDE4455Z']`
- **`pdf_url`** (3 values): `['', 'https://quotation-pdf-bucket.s3.amazonaws.com/uploads/1764517756541_Quotation_QN-006.pdf', 'https://quotation-pdf-bucket.s3.amazonaws.com/uploads/1764566844736_Quotation_QN-007.pdf']`


### 🔍 Sample Data (First 3 rows):
| id | timestamp | quotation_no | quotation_date | prepared_by | consigner_state | reference_name | consigner_address | consigner_mobile | consigner_phone | consigner_gstin | consigner_state_code | company_name | consignee_address | ship_to | consignee_state | contact_name | contact_no | consignee_gstin | consignee_state_code | msme_no | validity | payment_terms | delivery | freight | insurance | taxes | notes | account_no | bank_name | bank_address | ifsc_code | email | website | pan | items | pdf_url | grand_total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2025-11-29 08:45:48.625935+00:00 | QN-003 | 2025-11-29 | SHEETAL PATEL | Chhattisgarh | SOURABH ROLLING MILLS PVT LTD | VILLAGE KANHERA, ACHHOLI ROAD, URLA, RAIPUR, CHHAT | 6266919126 | 7723020095 | 22AAICS2367M1Z3 | 22 | Select Company | safsaf | safdsaf | sadfsaf | safas | 1212121212 | 221312 | 121 |  | The above quoted prices are valid up to 5 days fro | 100% advance payment in the mode of NEFT, RTGS & D | Material is ready in our stock | Extra as per actual. | Transit insurance for all shipment is at Buyer's r | Extra as per actual. |  | 733605010000120 | Union Bank of India | MID CORP BR | UBIN0573361 | marketing@sagartmt.com | www.pankajgroup.in  | AAICS2367M | [{'gst': 18, 'qty': 1, 'code': 'F01010000', 'name' |  | 0.00 |
| 2 | 2025-11-29 11:45:15.119642+00:00 | QN-004 | 2025-11-29 | Aakash | Chhattisgarh | Vipul |  | 9876501234 | 9811167788 | 27ABCDE1234F1Z5 | 27 | ABC Steels Pvt Ltd | Industrial Area, Raipur | None | Chhattisgarh | Manoj Singh | 9033442211 | 22AABCH1234Q1Z5 | 22 | MSME123456 | The above quoted prices are valid up to 5 days fro | 100% advance payment in the mode of NEFT, RTGS & D | Material is ready in our stock | Extra as per actual. | Transit insurance for all shipment is at Buyer's r | Extra as per actual. |  | 733605010000120 | Union Bank of India | MID CORP BR | UBIN0573361 | marketing@sagartmt.com | www.pankajgroup.in | ABCDE1234F | [{'gst': 18, 'qty': 1, 'code': 'ITM-1001', 'name': |  | 0.00 |
| 4 | 2025-11-29 11:47:07.550123+00:00 | QN-005 | 2025-11-29 | Aakash | Andhra Pradesh | Vipul |  | 9876501234 | 9811167788 | 27ABCDE1234F1Z5 | 27 | ABC Steels Pvt Ltd | Industrial Area, Raipur | None | Chhattisgarh | Manoj Singh | 9033442211 | 22AABCH1234Q1Z5 | 22 | MSME908776 | The above quoted prices are valid up to 5 days fro | 100% advance payment in the mode of NEFT, RTGS & D | Material is ready in our stock | Extra as per actual. | Transit insurance for all shipment is at Buyer's r | Extra as per actual. |  | 733605010000120 | Union Bank of India | MID CORP BR | UBIN0573361 | marketing@sagartmt.com | www.pankajgroup.in | ABCDE4455Z | [{'gst': 18, 'qty': 1, 'code': 'ITM-1001', 'name': |  | 0.00 |

---

## 📋 Table: `enquiry_tracker`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `BIGINT` | False |
| **timestamp** | `TIMESTAMP` | True |
| **enquiry_no** | `VARCHAR(100)` | True |
| **enquiry_status** | `VARCHAR(100)` | True |
| **what_did_customer_say** | `TEXT` | True |
| **current_stage** | `VARCHAR(150)` | True |
| **followup_status** | `VARCHAR(100)` | True |
| **next_call_date** | `DATE` | True |
| **next_call_time** | `TIME` | True |
| **is_order_received_status** | `VARCHAR(50)` | True |
| **acceptance_via** | `VARCHAR(100)` | True |
| **payment_mode** | `VARCHAR(100)` | True |
| **payment_terms_in_days** | `INTEGER` | True |
| **transport_mode** | `VARCHAR(100)` | True |
| **remark** | `TEXT` | True |
| **if_no_relevant_reason_status** | `VARCHAR(255)` | True |
| **if_no_relevant_reason_remark** | `TEXT` | True |
| **customer_order_hold_reason_category** | `VARCHAR(255)` | True |
| **holding_date** | `DATE` | True |
| **hold_remark** | `TEXT` | True |
| **sales_cordinator** | `VARCHAR(255)` | True |
| **calling_days** | `VARCHAR(255)` | True |
| **order_no** | `VARCHAR(100)` | True |
| **party_name** | `VARCHAR(255)` | True |
| **sales_person_name** | `VARCHAR(255)` | True |




### 🏷️ Categorical / Allowed Values:
- **`enquiry_no`** (4 values): `['ARUN YADAV', 'EN-01', 'LD-003', 'LD-004']`
- **`enquiry_status`** (3 values): `['hot', 'open', 'warm']`
- **`what_did_customer_say`** (4 values): `['Customer said quotation under review', 'Reviewing Quote', 'sadfdsaf', 'sdfds']`
- **`current_stage`** (2 values): `['order-expected', 'order-status']`
- **`followup_status`** (1 values): `['Reviewing Quote']`
- **`is_order_received_status`** (3 values): `['hold', 'no', 'yes']`
- **`acceptance_via`** (2 values): `['email', 'whatsapp']`
- **`payment_mode`** (2 values): `['neft', 'rtgs']`
- **`transport_mode`** (2 values): `['by road', 'road transport']`
- **`remark`** (8 values): `['afdasfas', 'asdfas', 'asdfasfsa', 'asdfasfsadf', 'asfasfas', 'cdsFSA', 'demoo', 'sadfasfda']`
- **`if_no_relevant_reason_status`** (1 values): `['project on hold']`
- **`if_no_relevant_reason_remark`** (1 values): `['asdfsadf']`
- **`customer_order_hold_reason_category`** (1 values): `['customer documentation pending']`
- **`hold_remark`** (1 values): `['wafasd']`
- **`order_no`** (7 values): `['DO-01', 'DO-02', 'DO-03', 'DO-04', 'DO-05', 'DO-06', 'DO-07']`


### 🔍 Sample Data (First 3 rows):
| id | timestamp | enquiry_no | enquiry_status | what_did_customer_say | current_stage | followup_status | next_call_date | next_call_time | is_order_received_status | acceptance_via | payment_mode | payment_terms_in_days | transport_mode | remark | if_no_relevant_reason_status | if_no_relevant_reason_remark | customer_order_hold_reason_category | holding_date | hold_remark | sales_cordinator | calling_days | order_no | party_name | sales_person_name |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2025-11-26 11:54:48.644062+00:00 | LD-003 | hot | Reviewing Quote | order-expected | Reviewing Quote | 2025-11-26 | 17:24:00 | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None |
| 2 | 2025-11-26 11:58:04.590322+00:00 | LD-003 | hot | Reviewing Quote | order-status | None | None | None | yes | email | rtgs | 1 | by road | asdfas | None | None | None | None | None | None | None | DO-01 | None | None |
| 4 | 2025-11-28 06:25:11.773008+00:00 | LD-003 | warm | Reviewing Quote | order-status | None | None | None | no | None | None | None | None | None | project on hold | asdfsadf | None | None | None | None | None | None | None | None |

---

## 📋 Table: `enquiry_to_order`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `BIGINT` | False |
| **timestamp** | `TIMESTAMP` | True |
| **en_enquiry_no** | `VARCHAR(100)` | True |
| **lead_source** | `VARCHAR(255)` | True |
| **company_name** | `VARCHAR(255)` | True |
| **phone_number** | `VARCHAR(50)` | True |
| **sales_person_name** | `VARCHAR(255)` | True |
| **location** | `VARCHAR(255)` | True |
| **email** | `VARCHAR(255)` | True |
| **enquiry_receiver_name** | `VARCHAR(255)` | True |
| **enquiry_date** | `DATE` | True |
| **enquiry_approach** | `VARCHAR(255)` | True |
| **item_qty** | `TEXT` | True |
| **planned** | `DATE` | True |
| **actual** | `DATE` | True |
| **delay** | `INTEGER` | True |
| **enquiry_status** | `VARCHAR(255)` | True |
| **what_did_customer_say** | `TEXT` | True |
| **current_stage** | `VARCHAR(255)` | True |
| **followup_status** | `VARCHAR(255)` | True |
| **next_call_date** | `DATE` | True |
| **next_call_time** | `TIME` | True |
| **is_order_received** | `BOOLEAN` | True |
| **status** | `VARCHAR(255)` | True |
| **acceptance_via** | `VARCHAR(255)` | True |
| **payment_mode** | `VARCHAR(255)` | True |
| **payment_terms_days** | `INTEGER` | True |
| **transport_mode** | `VARCHAR(255)` | True |
| **po_number** | `VARCHAR(255)` | True |
| **acceptance_file_upload** | `TEXT` | True |
| **remark** | `TEXT` | True |
| **if_no_relevant_reason_status** | `VARCHAR(255)` | True |
| **if_no_relevant_reason_remark** | `TEXT` | True |
| **customer_order_hold_reason_category** | `VARCHAR(255)` | True |
| **holding_date** | `DATE` | True |
| **hold_remark** | `TEXT` | True |
| **sales_coordinator_name** | `VARCHAR(255)` | True |
| **planned_days** | `INTEGER` | True |




### 🏷️ Categorical / Allowed Values:
- **`en_enquiry_no`** (4 values): `['EN-01', 'EN-02', 'EN-03', 'EN-04']`
- **`lead_source`** (4 values): `['Direct Visit', 'Google', 'Telephonic', 'TELEPHONIC']`
- **`company_name`** (4 values): `['3M Projects Pvt Ltd', 'A H ENTERPRISES', 'Choudhary Scaffolding', 'Navkar steel']`
- **`phone_number`** (4 values): `['9422533000', '9765817910', '9823111000', '9827164305']`
- **`sales_person_name`** (4 values): `['Amit Pandey', 'MR. SANDEEP SONI JI', 'Pradeep Porwar', 'Rajesh Verma']`
- **`location`** (4 values): `['B3/1106 mm Vally, Nr Tihama Complex, Mumbra, Mumbra Kausa Thane, Tihama Complex,', 'IDA Plot 4/A, Visakhapatnam', 'Pachora Road near Yes Bank, Jamner', 'Sambhaji Nagar,Pune']`
- **`email`** (3 values): `['', 'choudharyscaffolding@yahoo.com', 'vikashchaudhari103@gmail.com']`
- **`enquiry_receiver_name`** (3 values): `['Amit Pandey', 'Manish', 'TRIPATI RANA']`
- **`enquiry_approach`** (3 values): `['INWARD', 'Phone', 'Phone Call']`
- **`item_qty`** (4 values): `['[{"id":"1","name":"Angle 65x65","quantity":"1212"}]', '[{"id":"1","name":"MS BILLET","quantity":"12121"}]', '[{"id":"1","name":"MS PIPE","quantity":""}]', '[{"id":"1","name":"Ms pipe ","quantity":"30"}]']`
- **`enquiry_status`** (1 values): `['open']`
- **`what_did_customer_say`** (1 values): `['Customer said quotation under review']`
- **`current_stage`** (1 values): `['order-status']`
- **`followup_status`** (1 values): `['Reviewing Quote']`
- **`acceptance_via`** (1 values): `['email']`
- **`payment_mode`** (1 values): `['neft']`
- **`transport_mode`** (1 values): `['road transport']`
- **`remark`** (1 values): `['cdsFSA']`
- **`sales_coordinator_name`** (2 values): `['Amit Pandey', 'Jay Nirmal']`


### 🔍 Sample Data (First 3 rows):
| id | timestamp | en_enquiry_no | lead_source | company_name | phone_number | sales_person_name | location | email | enquiry_receiver_name | enquiry_date | enquiry_approach | item_qty | planned | actual | delay | enquiry_status | what_did_customer_say | current_stage | followup_status | next_call_date | next_call_time | is_order_received | status | acceptance_via | payment_mode | payment_terms_days | transport_mode | po_number | acceptance_file_upload | remark | if_no_relevant_reason_status | if_no_relevant_reason_remark | customer_order_hold_reason_category | holding_date | hold_remark | sales_coordinator_name | planned_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 2025-11-29 07:36:42.955406+00:00 | EN-01 | TELEPHONIC | A H ENTERPRISES | 9827164305 | MR. SANDEEP SONI JI | B3/1106 mm Vally, Nr Tihama Complex, Mumbra, Mumbr | vikashchaudhari103@gmail.com | TRIPATI RANA | 2025-11-29 | INWARD | [{"id":"1","name":"MS BILLET","quantity":"12121"}] | 2025-11-30 | 2025-11-29 | None | open | Customer said quotation under review | order-status | Reviewing Quote | 2025-11-29 | 13:12:00 | None | None | email | neft | 30 | road transport | None | None | cdsFSA | None | None | None | None | None | None | 1 |
| 3 | 2025-12-01 09:45:17.417176+00:00 | EN-02 | Google | 3M Projects Pvt Ltd | 9823111000 | Rajesh Verma | IDA Plot 4/A, Visakhapatnam |  | Manish | 2025-12-02 | Phone Call | [{"id":"1","name":"Angle 65x65","quantity":"1212"} | 2025-12-02 | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | Amit Pandey | 1 |
| 4 | 2026-01-28 05:35:15.651246+00:00 | EN-03 | Telephonic | Choudhary Scaffolding  | 9765817910 | Amit Pandey | Sambhaji Nagar,Pune | choudharyscaffolding@yahoo.com | Amit Pandey | 2026-01-28 | Phone Call | [{"id":"1","name":"Ms pipe ","quantity":"30"}] | 2026-01-29 | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | Jay Nirmal | 1 |

---

## 📋 Table: `laddle_return`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `BIGINT` | False |
| **sample_timestamp** | `TIMESTAMP` | False |
| **laddle_return_date** | `DATE` | False |
| **laddle_return_time** | `TIME` | False |
| **poring_temperature** | `VARCHAR(100)` | True |
| **poring_temperature_photo** | `TEXT` | True |
| **furnace_shift_incharge** | `VARCHAR(60)` | True |
| **furnace_crane_driver** | `VARCHAR(60)` | True |
| **ccm_temperature_before_pursing** | `VARCHAR(100)` | True |
| **ccm_temp_before_pursing_photo** | `TEXT` | True |
| **ccm_temp_after_pursing_photo** | `TEXT` | True |
| **ccm_crane_driver** | `VARCHAR(60)` | True |
| **stand1_mould_operator** | `VARCHAR(60)` | True |
| **stand2_mould_operator** | `VARCHAR(60)` | True |
| **shift_incharge** | `VARCHAR(60)` | True |
| **timber_man** | `VARCHAR(60)` | True |
| **operation_incharge** | `VARCHAR(60)` | True |
| **laddle_return_reason** | `TEXT` | True |
| **unique_code** | `VARCHAR(20)` | False |
| **created_at** | `TIMESTAMP` | True |




### 🏷️ Categorical / Allowed Values:
_No categorical columns detected_


### 🔍 Sample Data (First 3 rows):
_No data_

---

## 📋 Table: `client_followups`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **followup_id** | `INTEGER` | False |
| **client_name** | `VARCHAR(150)` | False |
| **sales_person** | `VARCHAR(150)` | False |
| **actual_order** | `NUMERIC(15, 2)` | True |
| **actual_order_date** | `DATE` | True |
| **date_of_calling** | `DATE` | False |
| **next_calling_date** | `DATE` | True |
| **created_at** | `TIMESTAMP` | True |
| **updated_at** | `TIMESTAMP` | True |




### 🏷️ Categorical / Allowed Values:
- **`sales_person`** (7 values): `['admin', 'Amit Pandey', 'Anil Kumar Mishra', 'DC Gautam', 'Rahul Sharma', 'Sheetal Patel', 'Tripati Rana']`


### 🔍 Sample Data (First 3 rows):
| followup_id | client_name | sales_person | actual_order | actual_order_date | date_of_calling | next_calling_date | created_at | updated_at |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 121 | AARNA STEELS | Tripati Rana | None | None | 2026-01-01 | None | 2026-01-30 08:58:58.108294 | 2026-01-30 08:58:58.108294 |
| 122 | AGRAWAL STEEL CHHATARPUR | Tripati Rana | None | None | 2026-01-01 | None | 2026-01-30 08:58:58.108294 | 2026-01-30 08:58:58.108294 |
| 123 | AJ STEEL | Tripati Rana | None | None | 2026-01-01 | None | 2026-01-30 08:58:58.108294 | 2026-01-30 08:58:58.108294 |

---

## 📋 Table: `sms_register`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `BIGINT` | False |
| **sample_timestamp** | `TIMESTAMP` | False |
| **sequence_number** | `VARCHAR(10)` | False |
| **laddle_number** | `SMALLINT` | False |
| **sms_head** | `VARCHAR(60)` | True |
| **furnace_number** | `VARCHAR(20)` | True |
| **remarks** | `TEXT` | True |
| **picture** | `TEXT` | True |
| **shift_incharge** | `VARCHAR(60)` | True |
| **temperature** | `VARCHAR(50)` | True |
| **unique_code** | `INTEGER` | True |
| **created_at** | `TIMESTAMP` | True |
| **prefilled_link** | `TEXT` | True |
| **update_link** | `TEXT` | True |




### 🏷️ Categorical / Allowed Values:
_No categorical columns detected_


### 🔍 Sample Data (First 3 rows):
_No data_

---

## 📋 Table: `login`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **username** | `VARCHAR(100)` | False |
| **password** | `VARCHAR(255)` | False |
| **usertype** | `VARCHAR(50)` | True |




### 🏷️ Categorical / Allowed Values:
- **`username`** (8 values): `['admin', 'Ajit Kumar Gupta', 'Amit Pandey', 'Anil Kumar Mishra', 'Rahul Sharma', 'Sandeep Kumar Dubey', 'Sheelesh Marele', 'Tripati Rana']`
- **`password`** (8 values): `['a1981', 'user18', 'user2025', 'user29', 'user30', 'user31', 'user57', 'Welcome@1234d']`
- **`usertype`** (2 values): `['admin', 'user']`


### 🔍 Sample Data (First 3 rows):
| username | password | usertype |
| --- | --- | --- |
| admin | Welcome@1234d | admin |
| Anil Kumar Mishra | user29 | admin |
| Tripati Rana | user30 | admin |

---

## 📋 Table: `users`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `BIGINT` | False |
| **user_name** | `TEXT` | True |
| **password** | `TEXT` | True |
| **email_id** | `TEXT` | True |
| **number** | `BIGINT` | True |
| **department** | `TEXT` | True |
| **role** | `VARCHAR(50)` | True |
| **status** | `VARCHAR(50)` | True |
| **user_access** | `TEXT` | True |
| **remark** | `TEXT` | True |
| **employee_id** | `TEXT` | True |
| **page_access** | `TEXT` | True |
| **system_access** | `TEXT` | True |
| **created_at** | `TIMESTAMP` | False |
| **given_by** | `VARCHAR(255)` | True |




### 🏷️ Categorical / Allowed Values:
- **`role`** (2 values): `['admin', 'user']`
- **`status`** (1 values): `['active']`
- **`remark`** (1 values): `['sfdfsdsdf']`
- **`page_access`** (10 values): `['/lead-to-order/dashboard,/lead-to-order/leads,/lead-to-order/follow-up,/lead-to-order/follow-up/new,/lead-to-order/call-tracker,/lead-to-order/call-tracker/new', '/o2d/dashboard,/o2d/orders,/o2d/gate-entry,/o2d/first-weight,/o2d/load-vehicle,/o2d/second-weight,/o2d/generate-invoice,/o2d/gate-out,/o2d/payment,/o2d/process,/o2d/complaint-details,/o2d/party-feedback,/lead-to-order/dashboard,/lead-to-order/leads,/lead-to-order/follow-up,/lead-to-order/follow-up/new,/lead-to-order/call-tracker,/lead-to-order/call-tracker/new,/', '/o2d/dashboard,/o2d/orders,/o2d/generate-invoice,/o2d/payment,/o2d/process,/o2d/complaint-details,/o2d/party-feedback,/lead-to-order/dashboard,/lead-to-order/leads,/lead-to-order/follow-up,/lead-to-order/follow-up/new,/lead-to-order/call-tracker,/lead-to-order/call-tracker/new,/', '/o2d/load-vehicle', '/o2d/orders,/o2d/complaint-details,/o2d/party-feedback,/lead-to-order/dashboard,/lead-to-order/leads,/lead-to-order/follow-up,/lead-to-order/follow-up/new,/lead-to-order/call-tracker,/lead-to-order/call-tracker/new', '/o2d/orders,/o2d/dashboard,/o2d/complaint-details,/o2d/party-feedback', '/o2d/orders,/o2d/gate-entry,/o2d/first-weight,/batchcode/qc-lab,/batchcode/sms-register,/batchcode/recoiler', '/o2d/orders,/o2d/process,/o2d/complaint-details,/o2d/party-feedback', '/o2d/process', '/o2d/process,/o2d/party-feedback,/o2d/complaint-details,/o2d/payment,/o2d/load-vehicle,/lead-to-order/dashboard,/lead-to-order/leads,/lead-to-order/follow-up,/lead-to-order/follow-up/new,/lead-to-order/call-tracker,/lead-to-order/call-tracker/new,/o2d/orders,/o2d/dashboard,/o2d/generate-invoice,/o2d/gate-out,/o2d/second-weight,/o2d/first-weight,/o2d/gate-entry']`
- **`system_access`** (5 values): `['lead-to-order', 'lead-to-order,o2d', 'o2d', 'o2d,batchcode', 'o2d,lead-to-order']`


### 🔍 Sample Data (First 3 rows):
| id | user_name | password | email_id | number | department | role | status | user_access | remark | employee_id | page_access | system_access | created_at | given_by |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | admin | Welcome@1234d | abc@gmail.com | 123 | NULL | admin | active | None | None | NULL | None | None | 2025-08-28 06:00:35.902673+00:00 | None |
| 2 | Process Co-Ordinator | 123456 | pc@sagartmt.com | 9770909919 | ADMIN | admin | active | None | None | S99999 | None | None | 2025-11-27 11:46:18.011547+00:00 | None |
| 3 | Mukesh Jain | user23 | it@sagartmt.com | 9770909924 | AUTOMATION | user | active | None | None | S00311 | None | None | 2025-08-28 06:00:35.902673+00:00 | None |

---

## 📋 Table: `enq_erp`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `BIGINT` | False |
| **item_type** | `VARCHAR(50)` | False |
| **size** | `VARCHAR(50)` | False |
| **thickness** | `NUMERIC(5, 2)` | False |
| **enquiry_date** | `DATE` | False |
| **customer** | `VARCHAR(150)` | False |
| **quantity** | `INTEGER` | False |
| **created_at** | `TIMESTAMP` | True |




### 🏷️ Categorical / Allowed Values:
- **`item_type`** (3 values): `['rectangular', 'round', 'square']`
- **`size`** (21 values): `['19X19', '20X40', '25OD', '25 OD', '25X25', '25X50', '25X68', '31X31', '32OD', '32 OD', '37X56', '38X38', '42OD', '47X47', '48OD', '60OD', '62X62', '72X72', '76OD', '80X40', '96X48']`


### 🔍 Sample Data (First 3 rows):
| id | item_type | size | thickness | enquiry_date | customer | quantity | created_at |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | square | 38X38 | 1.50 | 2026-01-01 | VISHWA GEETA ISPAT | 3 | 2026-01-31 12:15:47.122731 |
| 2 | rectangular | 25X50 | 1.50 | 2026-01-01 | VISHWA GEETA ISPAT | 5 | 2026-01-31 12:15:47.122731 |
| 3 | rectangular | 25X50 | 1.90 | 2026-01-01 | VISHWA GEETA ISPAT | 5 | 2026-01-31 12:15:47.122731 |

---

## 📋 Table: `clients`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **client_id** | `INTEGER` | False |
| **client_name** | `VARCHAR(150)` | False |
| **city** | `VARCHAR(100)` | True |
| **contact_person** | `VARCHAR(150)` | True |
| **contact_details** | `VARCHAR(200)` | True |
| **sales_person_id** | `INTEGER` | True |
| **client_type** | `VARCHAR(50)` | True |
| **status** | `VARCHAR(20)` | True |
| **created_at** | `TIMESTAMP` | True |
| **updated_at** | `TIMESTAMP` | True |




### 🏷️ Categorical / Allowed Values:
- **`client_type`** (3 values): `['CRR', 'NBD', 'PCRR']`
- **`status`** (1 values): `['active']`


### 🔍 Sample Data (First 3 rows):
| client_id | client_name | city | contact_person | contact_details | sales_person_id | client_type | status | created_at | updated_at |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | AAKASH INFRATECH,MUNGELI | MUNGELI | AKASH JI | 8103622228 | 322 | CRR | active | 2026-01-30 07:50:35.922719 | 2026-01-30 07:50:35.922719 |
| 3 | AARADHYA STEEL | MAIHAR | GANESH JI | 8962109701 | 26 | CRR | active | 2026-01-30 07:50:35.922719 | 2026-01-30 07:50:35.922719 |
| 4 | AARADHYA STEEL HYD | HYDERABAD | PRASAD REDDY | 8106886732 | 10 | NBD | active | 2026-01-30 07:50:35.922719 | 2026-01-30 07:50:35.922719 |

---
