# 🗄️ Schema Report: Checklist & Delegation System
**Generated:** 2026-03-10 16:30

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
- **`en_enquiry_no`** (7 values): `['EN-01', 'EN-02', 'EN-03', 'EN-04', 'EN-05', 'EN-06', 'EN-07']`
- **`lead_source`** (4 values): `['Direct Visit', 'Google', 'Telephonic', 'TELEPHONIC']`
- **`company_name`** (7 values): `['3M Projects Pvt Ltd', 'A H ENTERPRISES', 'Ascon Steel Traders', 'Choudhary Scaffolding', 'Lotus Infracon', 'Navkar steel', 'Yash Enterprises']`
- **`phone_number`** (7 values): `['08048602961', '08999251967', '9422533000', '9731872844', '9765817910', '9823111000', '9827164305']`
- **`sales_person_name`** (7 values): `['Abhishek Ji', 'Amit Pandey', 'Bashir', 'MR. SANDEEP SONI JI', 'Pradeep Porwar', 'Rajesh Verma', 'Yash ji']`
- **`location`** (6 values): `['B3/1106 mm Vally, Nr Tihama Complex, Mumbra, Mumbra Kausa Thane, Tihama Complex,', 'Gulbarga', 'IDA Plot 4/A, Visakhapatnam', 'Pachora Road near Yes Bank, Jamner', 'Pune', 'Sambhaji Nagar,Pune']`
- **`email`** (6 values): `['', 'ascon ste@gmail.com', 'choudharyscaffolding@yahoo.com', 'lotusinfracon@gmail.com', 'vikashchaudhari103@gmail.com', 'yash.enterprise @gmail.com']`
- **`enquiry_receiver_name`** (3 values): `['Amit Pandey', 'Manish', 'TRIPATI RANA']`
- **`enquiry_approach`** (3 values): `['INWARD', 'Phone', 'Phone Call']`
- **`item_qty`** (7 values): `['[{"id":"1","name":"Angle 65x65","quantity":"1212"}]', '[{"id":"1","name":"MS BILLET","quantity":"12121"}]', '[{"id":"1","name":"MS PIPE","quantity":""}]', '[{"id":"1","name":"MS PIPE","quantity":"15mt"}]', '[{"id":"1","name":"Ms PIPE ","quantity":"25"}]', '[{"id":"1","name":"MS PIPE","quantity":"25"}]', '[{"id":"1","name":"Ms pipe ","quantity":"30"}]']`
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

## 📋 Table: `delegation_done`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **task_id** | `BIGINT` | True |
| **created_at** | `TIMESTAMP` | False |
| **status** | `VARCHAR(11)` | True |
| **next_extend_date** | `TIMESTAMP` | True |
| **reason** | `TEXT` | True |
| **image_url** | `TEXT` | True |
| **name** | `TEXT` | True |
| **task_description** | `TEXT` | True |
| **given_by** | `TEXT` | True |
| **id** | `UUID` | False |




### 🏷️ Categorical / Allowed Values:
- **`status`** (3 values): `['completed', 'done', 'extend']`
- **`reason`** (20 values): `['', 'asdf', 'asdfgh', 'asdfsadf', 'botivate walo se hoha ham log nahi kar payege', 'done', 'Done', 'Done', 'fghjkl', 'follow up by ramesh bhaiya', 'have another work', 'mnvhj', 'not possible without bank api', 'ok', 'task_complete', 'Work Completed', 'Work Completed', 'Work Done', 'work Done and training start', 'Working']`
- **`given_by`** (16 values): `['AAKASH AGRAWAL', 'AK GUPTA', 'ANUP KUMAR BOPCHE', 'ccvgdff', 'DANVEER SINGH', 'DEEPAK BHALLA', 'DM', 'MD Sir', 'nchf', 'RAJNISH BHARDWAJ', 'Rinku Gautam', 'RINKU SINGH', 'SANDEEP DUBEY', 'SHAILESH CHITRE', 'SHEELESH MARELE', 'Shree Ram Patle']`


### 🔍 Sample Data (First 3 rows):
| task_id | created_at | status | next_extend_date | reason | image_url | name | task_description | given_by | id |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 51 | 2025-09-22 12:18:27.685699+00:00 | done | None | None | None | Dinesh Kumar Bandhe | Maintenance module तैयार हो चुका है, कृपया यूज़र्स | AAKASH AGRAWAL | 04daf1ef-6000-4c51-868b-7d8ab75a3c90 |
| 64 | 2025-09-19 04:21:00.965202+00:00 | done | None | None | None | admin | Boundry rounding  | Rinku Gautam | 07db9bf4-dfd8-49fc-986c-1d56e5bf62d1 |
| 44 | 2025-09-19 04:01:56.317176+00:00 | extend | 2025-09-27 00:00:00 | None | None | admin | Maintenance module तैयार हो चुका है, कृपया यूज़र्स | AAKASH AGRAWAL | 082eb679-6071-40b3-96d8-9eaa75f97351 |

---

## 📋 Table: `users`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `BIGINT` | False |
| **created_at** | `TIMESTAMP` | False |
| **user_name** | `TEXT` | True |
| **password** | `TEXT` | True |
| **email_id** | `TEXT` | True |
| **number** | `BIGINT` | True |
| **department** | `TEXT` | True |
| **given_by** | `TEXT` | True |
| **role** | `VARCHAR(8)` | True |
| **status** | `VARCHAR(10)` | True |
| **user_access** | `TEXT` | True |
| **leave_date** | `TIMESTAMP` | True |
| **remark** | `TEXT` | True |
| **leave_end_date** | `TIMESTAMP` | True |
| **employee_id** | `TEXT` | True |
| **last_punch_time** | `TIMESTAMP` | True |
| **last_punch_device** | `TEXT` | True |
| **page_access** | `TEXT` | True |
| **system_access** | `TEXT` | True |
| **subscription_access_system** | `JSONB` | True |
| **user_access1** | `TEXT` | True |
| **store_access** | `TEXT` | True |
| **emp_image** | `TEXT` | True |
| **verify_access** | `VARCHAR(20)` | True |
| **verify_access_dept** | `TEXT` | True |
| **store_role_access** | `TEXT` | True |
| **designation** | `TEXT` | True |
| **profile_img** | `TEXT` | True |
| **document_img** | `TEXT` | True |
| **division** | `VARCHAR(300)` | True |
| **session_token** | `TEXT` | True |




### 🏷️ Categorical / Allowed Values:
- **`given_by`** (19 values): `['AAKASH AGRAWAL', 'AK GUPTA', 'Amit Tiwari', 'ANIL KUMAR MISHRA', 'ANUP KUMAR BOPCHE', 'DC GOUTAM', 'DEEPAK BHALLA', 'G RAM MOHAN RAO', 'GUNJAN TIWARI', 'HULLAS PASWAN', 'MRIGENDRA NARAYAN BEPARI', 'MUKESH PATLE', 'RAJNISH BHARDWAJ', 'RAVI KUMAR SINGH', 'RINKU GAUTAM', 'ROSHAN RAJAK', 'SHAILESH CHITRE', 'SHEELESH MARELE', 'SUMAN JHA']`
- **`role`** (2 values): `['admin', 'user']`
- **`status`** (1 values): `['active']`
- **`remark`** (1 values): `['']`
- **`last_punch_device`** (2 values): `['E03C1CB34D83AA02', 'E03C1CB36042AA02']`
- **`user_access1`** (18 values): `['', 'Admin Office - First Floor', 'Admin Office - First Floor, Admin Office - Ground Floor, Back Office, Cabins ग्राउंड फ्लोर: and first floor, Canteen Area 1 & 2, Car Parking Area, CCM, CCM Office, CCM Panel Room, CCM PLC Panel Room, CCM SBO Panel Room, Container Office, Labour Colony & Bathroom, Main Gate, Main Gate Front Area, Mandir, New Lab, Patra Mill AC Panel Room, Patra Mill DC Panel Room, Patra Mill Foreman Office, Patra Mill Pump Room, Patra Mill SBO Panel, Pipe Mill, Plant Area, SMS Electrical Room, SMS Maintenance Office, SMS Office, SMS Panel Room, Store Office, Weight Office & Kata In/Out, Workshop', 'Admin Office - First Floor, Admin Office - Ground Floor, Car Parking Area', 'Admin Office - Ground Floor, Car Parking Area', 'Back Office, Container Office,TMT Foreman Office,Patra Mill Foreman Office', 'Canteen Area 1 & 2, Labour Colony & Bathroom, Main Gate, Main Gate Front Area, Mandir, Plant Area', 'Canteen Area 1 & 2, Labour Colony, Main Gate, Main Gate Front Area, Mandir, Plant Area', 'CCM PLC Panel Room, CCM SBO Panel Room', 'New Lab', 'Patra Mill AC Panel Room, Patra Mill DC Panel Room', 'Patra Mill SBO Panel', 'Pipe Mill', 'SMS Electrical Store Room, SMS Office, SMS Panel Room', 'SMS Panel Room, SMS Electrical Store Room', 'Store Office', 'Weight Office & Kata In/Out', 'Workshop']`
- **`store_access`** (11 values): `['APPROVE INDENT DATA', 'APPROVE INDENT DATA,APPROVE INDENT GM', 'APPROVE INDENT DATA,COMPLETED ITEMS,STORE OUT APPROVAL', 'APPROVE INDENT HOD', 'INDENT,PURCHASE ORDER,INVENTORY,REPAIR GATE PASS,REPAIR FOLLOW UP', 'INDENT,PURCHASE ORDER,INVENTORY,REPAIR GATE PASS,REPAIR FOLLOW UP,STORE GRN,GRN & PO,COMPLETED ITEMS,RETURNABLE', 'INDENT,PURCHASE ORDER,INVENTORY,REPAIR GATE PASS,REPAIR FOLLOW UP,STORE GRN,STORE GRN GM APPROVAL,STORE GRN CLOSE,STORE OUT APPROVAL,COMPLETED ITEMS,APPROVE INDENT HOD,APPROVE INDENT GM,RETURNABLE', 'PURCHASE ORDER', 'PURCHASE ORDER,INDENT,REPAIR GATE PASS,INVENTORY,RETURNABLE', 'STORE GRN ADMIN APPROVAL', 'STORE GRN,COMPLETED ITEMS']`
- **`verify_access`** (2 values): `['hod', 'manager']`
- **`store_role_access`** (1 values): `['hod']`
- **`profile_img`** (6 values): `['https://hrfms.sagartmt.com/uploads/employees/employee-profile-1771381828203-514717180.jpg', 'https://hrfms.sagartmt.com/uploads/employees/employee-profile-1772279687377-185619038.jpeg', 'https://hrfms.sagartmt.com/uploads/employees/employee-profile-1772529988130-234770905.jpeg', 'https://hrfms.sagartmt.com/uploads/employees/employee-profile-1772707174706-316302852.webp', 'https://hrfms.sagartmt.com/uploads/employees/employee-profile-1772824467664-177429649.webp', 'https://hrfms.sagartmt.com/uploads/employees/employee-profile-1773048088863-802960245.jpg']`
- **`division`** (6 values): `['COMMERCIAL', 'PIPE MILL', 'PROJECT', 'PROJECT,SMS', 'SMS', 'STRIP MILL']`
- **`session_token`** (2 values): `['eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjgyNCIsInVzZXJuYW1lIjoiYWRtaW4iLCJ1c2VyX25hbWUiOiJhZG1pbiIsInJvbGUiOiJhZG1pbiIsInVzZXJfYWNjZXNzIjoiQURNSU4sIEFVVE9NQVRJT04sIENDTSwgQ0NNIEVMRUNUUklDQUwsIENPTlRSQUNUT1JTIEFKQVkgR0lSSSBQSVBFIFJFUEFJUklORywgQ09OVFJBQ1RPUlMgQklSRU5EUkEgU0FMQVRJTkcsIENPTlRSQUNUT1JTIENIQU5EVSBUSVdBUkkgUElQRSBNSUxMLCBDT05UUkFDVE9SUyBDSEFORFUgVElXQVJJIFJFQ09JTEVSLCBDT05UUkFDVE9SUyBHVUREVSBLUiBZQURBViBQSVBFIFJFUEFJUklORywgQ09OVFJBQ1RPUlMgTVVNVEFaIFJFQ09JTEVSIEFORCBTQUxBVElORywgQ09OVFJBQ1RPUlMgTVVNVEFaIFJFQ09JTEVSICYgU0FMQVRJTkcsIENPTlRSQUNUT1JTIE5BV0lLIExBQiwgQ09OVFJBQ1RPUlMgUFJFTSBCSEFSVEkgUElQRSBNSUxMLCBDT05UUkFDVE9SUyBST0hJVCBNSVNIUkEgTUlMTCBTQUZBSSwgQ09OVFJBQ1RPUlMgU0hJVkFNIFRJV0FSSSBQSVBFIE1JTEwsIENPTlRSQUNUT1JTIFNPTlUgU0FMQVRJTkcsIENPTlRSQUNUT1JTIFZJS0FTSCBLVU1BUiBQSVBFIE1JTEwsIENSTSwgQ1JVU0hFUiwgRElTUEFUQ0gsIERJU1BBVENILElOV0FSRCwgSFIsIElOV0FSRCwgTEFCIEFORCBRVUFMSVRZIENPTlRST0wsIE1BUktFVElORywgUEMsIFBJUEUgTUlMTCBFTEVDVFJJQ0FMLCBQSVBFIE1JTEwgTUFJTlRFTkFOQ0UsIFBJUEUgTUlMTCBQUk9EVUNUSU9OLCBQUk9KRUNULCBQVVJDSEFTRSwgU0VDVVJJVFksIFNNUyBFTEVDVFJJQ0FMLCBTTVMgTUFJTlRFTkFOQ0UsIFNNUyBQUk9EVUNUSU9OLCBTVE9SRSwgU1RSSVAgTUlMTCBFTEVDVFJJQ0FMLCBTVFJJUCBNSUxMIE1BSU5URU5BTkNFLCBTVFJJUCBNSUxMIFBST0RVQ1RJT04sIFRSQU5TUE9SVCwgV0IsIFdPUktTSE9QIiwicGFnZV9hY2Nlc3MiOiIiLCJzeXN0ZW1fYWNjZXNzIjoiIiwiZW1wbG95ZWVfaWQiOiJTMDAwMDEiLCJlbWFpbF9pZCI6IiIsImRlcGFydG1lbnQiOiJBRE1JTiIsImlhdCI6MTc3MzEzOTg5MywiZXhwIjoxNzc1NzMxODkzfQ.eyVdUxF85RDxh16hT6TLy3qApCFzK80UH-7GrCG8J3I', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjgzNSIsInVzZXJuYW1lIjoiQUFLQVNIIEFHUkFXQUwiLCJ1c2VyX25hbWUiOiJBQUtBU0ggQUdSQVdBTCIsInJvbGUiOiJhZG1pbiIsInVzZXJfYWNjZXNzIjoiQURNSU4sQVVUT01BVElPTixDQ00sQ0NNIEVMRUNUUklDQUwsQ09OVFJBQ1RPUlMgQUpBWSBHSVJJIFBJUEUgUkVQQUlSSU5HLENPTlRSQUNUT1JTIEJJUkVORFJBIFNBTEFUSU5HLENPTlRSQUNUT1JTIENIQU5EVSBUSVdBUkkgUElQRSBNSUxMLENPTlRSQUNUT1JTIENIQU5EVSBUSVdBUkkgUkVDT0lMRVIsQ09OVFJBQ1RPUlMgR1VERFUgS1IgWUFEQVYgUElQRSBSRVBBSVJJTkcsQ09OVFJBQ1RPUlMgTVVNVEFaIFJFQ09JTEVSIEFORCBTQUxBVElORyxDT05UUkFDVE9SUyBOQVdJSyBMQUIsQ09OVFJBQ1RPUlMgUFJFTSBCSEFSVEkgUElQRSBNSUxMLENPTlRSQUNUT1JTIFJPSElUIE1JU0hSQSBNSUxMIFNBRkFJLENPTlRSQUNUT1JTIFNISVZBTSBUSVdBUkkgUElQRSBNSUxMLENPTlRSQUNUT1JTIFNPTlUgU0FMQVRJTkcsQ09OVFJBQ1RPUlMgVklLQVNIIEtVTUFSIFBJUEUgTUlMTCxDUk0sQ1JVU0hFUixESVNQQVRDSCxIUixJTldBUkQsTEFCIEFORCBRVUFMSVRZIENPTlRST0wsTUFSS0VUSU5HLFBDLFBJUEUgTUlMTCBFTEVDVFJJQ0FMLFBJUEUgTUlMTCBNQUlOVEVOQU5DRSxQSVBFIE1JTEwgUFJPRFVDVElPTixQUk9KRUNULFBVUkNIQVNFLFNFQ1VSSVRZLFNNUyBFTEVDVFJJQ0FMLFNNUyBNQUlOVEVOQU5DRSxTTVMgUFJPRFVDVElPTixTVE9SRSxTVFJJUCBNSUxMIEVMRUNUUklDQUwsU1RSSVAgTUlMTCBNQUlOVEVOQU5DRSxTVFJJUCBNSUxMIFBST0RVQ1RJT04sVFJBTlNQT1JULFdCLFdPUktTSE9QIiwicGFnZV9hY2Nlc3MiOiJEYXNoYm9hcmQsT3JkZXJzLEVucXVpcnksRW5xdWlyeSBMaXN0LFBlbmRpbmcgVmVoaWNsZXMsQ3VzdG9tZXJzLEZvbGxvdyBVcHMsSG90IENvaWwsUUMgTGFiLFNNUyBSZWdpc3RlcixSZWNvaWxlcixQaXBlIE1pbGwsTGFkZGVsLFR1bmRpcyxMZWFkcyxGb2xsb3cgVXAsQ2FsbCBUcmFja2VyIiwic3lzdGVtX2FjY2VzcyI6IkNIRUNLTElTVCxNQUlOVEVOQU5DRSxIT1VTRUtFRVBJTkcsTzJELEJBVENIQ09ERSxMRUFELVRPLU9SREVSLFNUT1JFIEFORCBQVVJDSEFTRSxTQUxFUyBNT0RVTEUsU1VCU0NSSVBUSU9OLEhSTVMsTE9HSVNUSUMsVklTSVRPUiBHQVRFIFBBU1MiLCJlbXBsb3llZV9pZCI6IlNSTVBMIiwiZW1haWxfaWQiOiJhZG1pbkBzYWdhcnRtdC5jb20iLCJkZXBhcnRtZW50IjoiQURNSU4iLCJpYXQiOjE3NzMxNDAxNTQsImV4cCI6MTc3NTczMjE1NH0.ijf66iYq_Uyuj_SRDZQ2HsogN8B75fTwaF05FcrD_BU']`


### 🔍 Sample Data (First 3 rows):
| id | created_at | user_name | password | email_id | number | department | given_by | role | status | user_access | leave_date | remark | leave_end_date | employee_id | last_punch_time | last_punch_device | page_access | system_access | subscription_access_system | user_access1 | store_access | emp_image | verify_access | verify_access_dept | store_role_access | designation | profile_img | document_img | division | session_token |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 775 | 2026-01-19 06:28:58.066706+00:00 | Siddharth Singh | 123 | ss3552630@gmail.com | 7067535650 | CONTRACTORS MUMTAZ RECOILER AND SALATING | None | user | active | CONTRACTORS MUMTAZ RECOILER AND SALATING | None | None | None | None | None | None | dashboard,all-task,/dashboard,/my-profile,/resume- | Checklist | {'pages': [], 'systems': []} | None | None | None | None | None | None | None | None | None | STRIP MILL | None |
| 805 | 2026-01-21 11:04:46.065727+00:00 | Rakesh Kumar Bisen | 1234 | rakesh@12gmail.com | 7067154770 | SMS MAINTENANCE | None | user | active | SMS MAINTENANCE | None | None | None | S09699 | None | None | dashboard,all-task,/dashboard,/my-profile,/resume- | CHECKLIST | {'pages': [], 'systems': []} |  | None | https://emp-profiles-dashboard.s3.amazonaws.com/em | None | None | None | None | None | None | SMS | None |
| 778 | 2026-01-19 07:35:53.174021+00:00 | Chandan Soni | 123 | ss3552630@gmail.com | 9303196837 | CONTRACTORS CHANDU TIWARI RECOILER | None | user | active | CONTRACTORS CHANDU TIWARI RECOILER | None | None | None | None | None | None | dashboard,all-task,/dashboard,/my-profile,/resume- | Checklist | {'pages': [], 'systems': []} | None | None | None | None | None | None | None | None | None | STRIP MILL | None |

---

## 📋 Table: `delegation`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **task_id** | `BIGINT` | False |
| **created_at** | `TIMESTAMP` | False |
| **department** | `TEXT` | True |
| **name** | `TEXT` | True |
| **task_description** | `TEXT` | True |
| **frequency** | `TEXT` | True |
| **remarks** | `TEXT` | True |
| **task_start_date** | `TIMESTAMP` | False |
| **given_by** | `TEXT` | True |
| **image** | `TEXT` | True |
| **enable_reminder** | `VARCHAR(3)` | True |
| **require_attachment** | `TEXT` | True |
| **status** | `TEXT` | True |
| **updated_at** | `TIMESTAMP` | True |
| **planned_date** | `TIMESTAMP` | True |
| **submission_date** | `TIMESTAMP` | True |
| **color_code_for** | `BIGINT` | True |
| **delay** | `INTERVAL` | True |
| **division** | `VARCHAR(255)` | True |




### 🏷️ Categorical / Allowed Values:
- **`frequency`** (1 values): `['one-time']`
- **`remarks`** (13 values): `['', 'botivate walo se hoha ham log nahi kar payege', 'done', 'Done', 'Done', 'follow up by ramesh bhaiya', 'not possible without bank api', 'ok', 'Work Completed', 'Work Completed', 'Work Done', 'work Done and training start', 'Working']`
- **`given_by`** (13 values): `['AAKASH AGRAWAL', 'AK GUPTA', 'AMIT TIWARI', 'ANUP KUMAR BOPCHE', 'DANVEER SINGH', 'DEEPAK BHALLA', 'RAJNISH BHARDWAJ', 'Rinku Gautam', 'RINKU SINGH', 'SANDEEP DUBEY', 'SHAILESH CHITRE', 'SHEELESH MARELE', 'Shree Ram Patle']`
- **`enable_reminder`** (1 values): `['yes']`
- **`require_attachment`** (2 values): `['no', 'yes']`
- **`status`** (3 values): `['done', 'Done', 'extend']`


### 🔍 Sample Data (First 3 rows):
| task_id | created_at | department | name | task_description | frequency | remarks | task_start_date | given_by | image | enable_reminder | require_attachment | status | updated_at | planned_date | submission_date | color_code_for | delay | division |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 19 | 2025-08-19 11:37:00 | ADMIN | Sandeep Kumar Dubey | ajit gupta gm sir meeting today 4.30 | one-time | None | 2025-08-19 16:02:00 | AAKASH AGRAWAL | None | yes | no | Done | None | 2025-08-19 16:02:00 | 2025-08-21 00:00:00 | 1 | 1 day, 7:58:00 | None |
| 20 | 2025-08-19 11:42:00 | ADMIN | Sandeep Kumar Dubey | akash bhaiya time 3.30 pm | one-time | None | 2025-08-22 15:25:00 | AAKASH AGRAWAL | None | yes | no | Done | None | 2025-08-22 15:25:00 | 2025-08-21 00:00:00 | 1 | -2 days, 8:35:00 | None |
| 21 | 2025-08-19 11:45:00 | ADMIN | Sandeep Kumar Dubey | ashish sir meeting 3.30 pm today | one-time | None | 2025-08-19 15:26:00 | AAKASH AGRAWAL | None | yes | no | Done | None | 2025-08-19 15:26:00 | 2025-08-21 00:00:00 | 1 | 1 day, 8:34:00 | None |

---

## 📋 Table: `checklist`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **task_id** | `BIGINT` | False |
| **department** | `TEXT` | True |
| **given_by** | `TEXT` | True |
| **name** | `TEXT` | True |
| **task_description** | `TEXT` | True |
| **enable_reminder** | `VARCHAR(3)` | True |
| **require_attachment** | `VARCHAR(3)` | True |
| **frequency** | `TEXT` | True |
| **remark** | `TEXT` | True |
| **status** | `TEXT` | True |
| **image** | `TEXT` | True |
| **admin_done** | `TEXT` | True |
| **delay** | `INTERVAL` | True |
| **planned_date** | `TEXT` | True |
| **created_at** | `TIMESTAMP` | True |
| **task_start_date** | `TIMESTAMP` | True |
| **submission_date** | `TIMESTAMP` | True |
| **user_status_checklist** | `TEXT` | True |
| **division** | `TEXT` | True |




### 🏷️ Categorical / Allowed Values:
- **`enable_reminder`** (2 values): `['yes', 'no']`
- **`require_attachment`** (2 values): `['yes', 'no']`
- **`frequency`** (11 values): `['daily', 'Daily', 'fortnightly', 'monthly', 'Monthly', 'one time', 'quarterly', 'weekly', 'Weekly', 'Y', 'yearly']`
- **`status`** (4 values): `['no', 'No', 'yes', 'Yes']`
- **`admin_done`** (3 values): `['confirmed', 'Confirmed', 'no']`
- **`user_status_checklist`** (4 values): `['no', 'No', 'yes', 'Yes']`
- **`division`** (5 values): `['COMMERCIAL', 'PIPE MILL', 'PROJECT', 'SMS', 'STRIP MILL']`


### 🔍 Sample Data (First 3 rows):
| task_id | department | given_by | name | task_description | enable_reminder | require_attachment | frequency | remark | status | image | admin_done | delay | planned_date | created_at | task_start_date | submission_date | user_status_checklist | division |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3522339 | PIPE MILL MAINTENANCE | ANUP KUMAR BOPCHE | Ravi Patle | "मशीन रिपेयरिंग-टूटे या घिसे पार्ट्स निकालकर कटिंग | yes | no | daily |  | yes | None | confirmed | 1 day, 4:06:06.354399 | 2026-01-22T09:00:00 | 2026-01-18 07:03:16.109592 | 2026-01-22 09:00:00 | 2026-01-23 13:06:06.354399 | Yes | PIPE MILL |
| 3517465 | PIPE MILL MAINTENANCE | ANUP KUMAR BOPCHE | Shrikant Yadav | "मशीन मॉनिटरिंग-मशीन रनिंग के दौरान वाइब्रेशन, नॉइ | yes | no | daily |  | no | None | confirmed | 15:00:00 | 2026-01-22T09:00:00 | 2026-01-18 06:24:53.327677 | 2026-01-22 09:00:00 | 2026-01-23 00:00:00 | No | PIPE MILL |
| 3517830 | PIPE MILL MAINTENANCE | ANUP KUMAR BOPCHE | Shrikant Yadav | "मशीन रिपेयरिंग-टूटे या घिसे पार्ट्स निकालकर कटिंग | yes | no | daily |  | no | None | confirmed | 15:00:00 | 2026-01-22T09:00:00 | 2026-01-18 06:25:22.331428 | 2026-01-22 09:00:00 | 2026-01-23 00:00:00 | No | PIPE MILL |

---

## 📋 Table: `working_day_calender`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **working_date** | `DATE` | True |
| **day** | `TEXT` | True |
| **week_num** | `INTEGER` | True |
| **month** | `INTEGER` | True |
| **id** | `INTEGER` | False |




### 🏷️ Categorical / Allowed Values:
- **`day`** (7 values): `['गुरु', 'बुध', 'मंगल', 'रवि', 'शनि', 'शुक्र', 'सोम']`


### 🔍 Sample Data (First 3 rows):
| working_date | day | week_num | month | id |
| --- | --- | --- | --- | --- |
| 2025-04-01 | मंगल | 14 | 4 | 1 |
| 2025-04-02 | बुध | 14 | 4 | 2 |
| 2025-04-03 | गुरु | 14 | 4 | 3 |

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
| **unique_code** | `VARCHAR(10)` | True |
| **created_at** | `TIMESTAMP` | True |
| **prefilled_link** | `TEXT` | True |
| **update_link** | `TEXT` | True |
| **melter_name** | `VARCHAR(255)` | True |




### 🏷️ Categorical / Allowed Values:
- **`sequence_number`** (2 values): `['A', 'B']`
- **`sms_head`** (2 values): `['Baldev Singh Saini', 'V M Gupta']`
- **`furnace_number`** (2 values): `['Furnace1', 'Furnace2']`
- **`remarks`** (5 values): `['dfsdfsdf', 'dsfsdf', 'sadas', 'sdfsd', 'sfdf']`
- **`picture`** (6 values): `['http://localhost:3004/uploads/sms-register-pictures/whatsappimage20260220at134242-1771930725985-563963371.jpeg', 'https://batchcode.sagartmt.com/uploads/sms-register-pictures/whatsappimage20260220at1342401-1772020692985-468844663.jpeg', 'https://batchcode.sagartmt.com//uploads/sms-register-pictures/whatsappimage20260220at1342421-1772005649761-668468138.jpeg', 'https://batchcode.sagartmt.com/uploads/sms-register-pictures/whatsappimage20260220at1342421-1772021616414-260607210.jpeg', 'https://batchcode.sagartmt.com//uploads/sms-register-pictures/whatsappimage20260220at134242-1771935754124-262202616.jpeg', 'https://batchcode.sagartmt.com/uploads/sms-register-pictures/whatsappimage20260220at134242-1772021660715-677698102.jpeg']`
- **`shift_incharge`** (2 values): `['Prakash Kumar', 'Pramod Thakur']`
- **`temperature`** (6 values): `['123', '234', '3423', '4234', '432', '4534']`
- **`unique_code`** (6 values): `['24B01', '24B02', '25B01', '25B02', '25B03', '25B04']`
- **`melter_name`** (6 values): `['asdas', 'dsfsf', 'sdf', 'sdfsd', 'werw', 'wqeqwe']`


### 🔍 Sample Data (First 3 rows):
| id | sample_timestamp | sequence_number | laddle_number | sms_head | furnace_number | remarks | picture | shift_incharge | temperature | unique_code | created_at | prefilled_link | update_link | melter_name |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2026-02-24 10:58:45.988000+00:00 | B | 3 | V M Gupta | Furnace2 | sfdf | http://localhost:3004/uploads/sms-register-picture | Pramod Thakur | 234 | 24B01 | None | None | None | sdfsd |
| 2 | 2026-02-24 12:22:34.129000+00:00 | A | 1 | V M Gupta | Furnace1 | dfsdfsdf | https://batchcode.sagartmt.com//uploads/sms-regist | Pramod Thakur | 4234 | 24B02 | None | None | None | asdas |
| 3 | 2026-02-25 07:47:29.765000+00:00 | A | 1 | V M Gupta | Furnace1 | sadas | https://batchcode.sagartmt.com//uploads/sms-regist | Pramod Thakur | 123 | 25B01 | None | None | None | wqeqwe |

---

## 📋 Table: `indent_approvals`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `INTEGER` | False |
| **indent_id** | `INTEGER` | True |
| **approver_id** | `VARCHAR(100)` | True |
| **approval_date** | `TIMESTAMP` | True |
| **remarks** | `TEXT` | True |
| **status** | `VARCHAR(20)` | True |




### 🏷️ Categorical / Allowed Values:
_No categorical columns detected_


### 🔍 Sample Data (First 3 rows):
_No data_

---

## 📋 Table: `ticket_book`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `INTEGER` | False |
| **status** | `VARCHAR(50)` | True |
| **type_of_bill** | `VARCHAR(50)` | True |
| **bill_number** | `VARCHAR(50)` | True |
| **travels_name** | `VARCHAR(100)` | True |
| **per_ticket_amount** | `NUMERIC` | True |
| **upload_bill_image** | `VARCHAR(255)` | True |
| **total_amount** | `NUMERIC` | True |
| **charges** | `NUMERIC` | True |
| **person_name** | `VARCHAR(255)` | True |
| **booked_name** | `VARCHAR(255)` | True |
| **created_at** | `TIMESTAMP` | True |
| **updated_at** | `TIMESTAMP` | True |
| **request_employee_code** | `VARCHAR(100)` | True |
| **booked_employee_code** | `VARCHAR(100)` | True |




### 🏷️ Categorical / Allowed Values:
_No categorical columns detected_


### 🔍 Sample Data (First 3 rows):
_No data_

---

## 📋 Table: `systems`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `INTEGER` | False |
| **systems** | `VARCHAR(255)` | False |
| **link** | `TEXT` | True |




### 🏷️ Categorical / Allowed Values:
- **`systems`** (8 values): `['CHECKLIST COMBINED', 'CLOSE GATE PASS', 'HRMS', 'LOGISTIC', 'SALES MODULE', 'STORE AND PURCHASE', 'SUBSCRIPTION', 'VISITOR GATE PASS']`
- **`link`** (8 values): `['https://checklist-frontend-aws.vercel.app/', 'https://doc-sub-frontend.vercel.app', 'https://gate-pass-srmpl.vercel.app/dashboard/delegation', 'https://gate-pass-srmpl.vercel.app/dashboard/quick-task', 'https://hrfms-frontend-aws.vercel.app/', 'https://new-store-repair-frontend.vercel.app/', 'https://o2d-lead-batchcode-frontend-aws.vercel.app/login', 'https://triofleet.trieon.in/']`


### 🔍 Sample Data (First 3 rows):
| id | systems | link |
| --- | --- | --- |
| 4 | SALES MODULE | https://o2d-lead-batchcode-frontend-aws.vercel.app |
| 15 | LOGISTIC | https://triofleet.trieon.in/ |
| 1 | CHECKLIST COMBINED | https://checklist-frontend-aws.vercel.app/ |

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
| **dip_reading** | `VARCHAR(100)` | True |




### 🏷️ Categorical / Allowed Values:
- **`slag_cleaning_top`** (2 values): `['Done', 'Not Done']`
- **`slag_cleaning_bottom`** (2 values): `['Done', 'Not Done']`
- **`nozzle_proper_lancing`** (2 values): `['Done', 'Not Done']`
- **`pursing_plug_cleaning`** (1 values): `['Not Done']`
- **`sly_gate_check`** (1 values): `['Not Done']`
- **`nozzle_check_cleaning`** (1 values): `['Not Done']`
- **`sly_gate_operate`** (1 values): `['Not Done']`
- **`nfc_proper_heat`** (1 values): `['Not Done']`
- **`nfc_filling_nozzle`** (1 values): `['Not Done']`
- **`timber_man_name`** (2 values): `['ffgdfgdf', 'gdfdhgfh']`
- **`laddle_man_name`** (2 values): `['dgdf', 'fghfgh']`
- **`laddle_foreman_name`** (2 values): `['dfgd', 'fghfgh']`
- **`supervisor_name`** (3 values): `['dfgdf', 'Raj Kumar', 'sdfs']`
- **`unique_code`** (3 values): `['C-4PF4', 'C-7N7L', 'C-C7FL']`
- **`dip_reading`** (2 values): `['fdfgdf', 'sdfsd']`


### 🔍 Sample Data (First 3 rows):
| id | sample_timestamp | sample_date | laddle_number | slag_cleaning_top | slag_cleaning_bottom | nozzle_proper_lancing | pursing_plug_cleaning | sly_gate_check | nozzle_check_cleaning | sly_gate_operate | nfc_proper_heat | nfc_filling_nozzle | plate_life | timber_man_name | laddle_man_name | laddle_foreman_name | supervisor_name | unique_code | created_at | dip_reading |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2026-02-24 10:52:53.955000+00:00 | 2026-03-03 | 1 | Done | Done | Done | Not Done | Not Done | Not Done | Not Done | Not Done | Not Done | 1 | gdfdhgfh | fghfgh | fghfgh | Raj Kumar | C-C7FL | 2026-02-24 10:52:54.559524+00:00 | sdfsd |
| 2 | 2026-02-24 11:01:09.150000+00:00 | 2026-02-24 | 2 | Not Done | Not Done | Not Done | Not Done | Not Done | Not Done | Not Done | Not Done | Not Done | 2 | gdfdhgfh | fghfgh | fghfgh | sdfs | C-4PF4 | 2026-02-24 11:01:09.600134+00:00 | sdfsd |
| 3 | 2026-02-25 09:25:49.688000+00:00 | 2026-02-25 | 1 | Not Done | Not Done | Not Done | Not Done | Not Done | Not Done | Not Done | Not Done | Not Done | 3 | ffgdfgdf | dgdf | dfgd | dfgdf | C-7N7L | 2026-02-25 09:25:49.724021+00:00 | fdfgdf |

---

## 📋 Table: `repair_followup`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `INTEGER` | False |
| **gate_pass_date** | `DATE` | True |
| **gate_pass_no** | `VARCHAR(50)` | True |
| **department** | `VARCHAR(50)` | True |
| **party_name** | `VARCHAR(150)` | True |
| **item_name** | `VARCHAR(200)` | True |
| **item_code** | `VARCHAR(100)` | True |
| **remarks** | `TEXT` | True |
| **uom** | `VARCHAR(20)` | True |
| **qty_issued** | `NUMERIC(12, 2)` | True |
| **lead_time** | `INTEGER` | True |
| **planned1** | `DATE` | True |
| **actual1** | `DATE` | True |
| **time_delay1** | `INTEGER` | True |
| **stage1_status** | `VARCHAR(50)` | True |
| **planned2** | `DATE` | True |
| **actual2** | `DATE` | True |
| **time_delay2** | `INTEGER` | True |
| **stage2_status** | `VARCHAR(50)` | True |
| **gate_pass_status** | `VARCHAR(50)` | True |
| **created_at** | `TIMESTAMP` | True |
| **updated_at** | `TIMESTAMP` | True |
| **extended_date** | `DATE` | True |




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
- **`sms_short_code`** (4 values): `['24B01', '24B02', '25B01', '25B02']`
- **`submission_type`** (3 values): `['Auto', 'Cold Billet', 'Hot Coil']`
- **`size`** (4 values): `['234', '342', '54435', '5454']`
- **`mill_incharge`** (2 values): `['Lal Babu', 'Ravi Singh']`
- **`quality_supervisor`** (3 values): `['Birendra Kumar Singh', 'Durgesh Sahu', 'Yashwant Sahu']`
- **`picture`** (3 values): `['http://localhost:3004/uploads/hot-coil-pictures/whatsappimage20260220at134242-1771930747722-74987028.jpeg', 'https://batchcode.sagartmt.com/uploads/hot-coil-pictures/whatsappimage20260220at134241-1772021551051-422698015.jpeg', 'https://batchcode.sagartmt.com//uploads/hot-coil-pictures/whatsappimage20260220at1342421-1772005732101-41476657.jpeg']`
- **`electrical_dc_operator`** (3 values): `['Anand', 'Hari Tiwari', 'Pankaj']`
- **`remarks`** (4 values): `['dfdfdd', 'dfgf', 'sdfsd', 'sdfsdf']`
- **`strand1_temperature`** (3 values): `['234', '3434', '54']`
- **`strand2_temperature`** (4 values): `['234', '3434', '423', '54']`
- **`shift_supervisor`** (3 values): `['54', 'admin', 'sdfsdf']`
- **`unique_code`** (4 values): `['24B01', '24B02', '25B01', '25B02']`


### 🔍 Sample Data (First 3 rows):
| id | sample_timestamp | sms_short_code | submission_type | size | mill_incharge | quality_supervisor | picture | electrical_dc_operator | remarks | strand1_temperature | strand2_temperature | shift_supervisor | unique_code | created_at | updated_at | update_link |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2026-02-24 10:59:07.724000 | 24B01 | Hot Coil | 342 | Lal Babu | Durgesh Sahu | http://localhost:3004/uploads/hot-coil-pictures/wh | Hari Tiwari | sdfsd | 234 | 423 | admin | 24B01 | 2026-02-24 10:59:07.950004 | 2026-02-24 10:59:07.950004 | None |
| 2 | 2026-02-24 12:24:53.216000 | 24B02 | Hot Coil | 5454 | Lal Babu | Yashwant Sahu | None | Hari Tiwari | dfdfdd | 3434 | 3434 | admin | 24B02 | 2026-02-24 12:24:53.252284 | 2026-02-24 12:24:53.252284 | None |
| 3 | 2026-02-25 07:48:52.103000 | 25B01 | Auto | 234 | Ravi Singh | Birendra Kumar Singh | https://batchcode.sagartmt.com//uploads/hot-coil-p | Anand | sdfsdf | 234 | 234 | sdfsdf | 25B01 | 2026-02-25 07:48:52.103781 | 2026-02-25 07:48:52.103781 | None |

---

## 📋 Table: `re_coile`
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
| **final_c** | `NUMERIC` | True |
| **final_mn** | `NUMERIC` | True |
| **final_s** | `NUMERIC` | True |
| **final_p** | `NUMERIC` | True |
| **tested_by** | `VARCHAR(60)` | True |
| **remarks** | `TEXT` | True |
| **report_picture** | `TEXT` | True |
| **unique_code** | `VARCHAR(30)` | True |
| **created_at** | `TIMESTAMP` | True |




### 🏷️ Categorical / Allowed Values:
- **`sms_batch_code`** (4 values): `['24B01', '24B02', '25B01', '25B03']`
- **`furnace_number`** (2 values): `['Furnace1', 'Furnace2']`
- **`sequence_code`** (2 values): `['A', 'B']`
- **`shift_type`** (1 values): `['Day']`
- **`tested_by`** (2 values): `['Komal Sahu', 'Sushil Bharti']`
- **`remarks`** (4 values): `['asdasddasfd', 'dfsdf', 'sdfs', 'sdfsdf']`
- **`report_picture`** (4 values): `['http://localhost:3004/uploads/qc-report-pictures/whatsappimage20260220at1342411-1771930814941-657202176.jpeg', 'https://batchcode.sagartmt.com//uploads/qc-report-pictures/whatsappimage20260220at134240-1772011037492-663408313.jpeg', 'https://batchcode.sagartmt.com//uploads/qc-report-pictures/whatsappimage20260220at134242-1771937143892-911394049.jpeg', 'https://batchcode.sagartmt.com/uploads/qc-report-pictures/whatsappimage20260220at134242-1772022642213-56845928.jpeg']`
- **`unique_code`** (4 values): `['QC-JEJN', 'QC-PTIB', 'QC-QZGE', 'QC-VVMF']`


### 🔍 Sample Data (First 3 rows):
| id | sample_timestamp | sms_batch_code | furnace_number | sequence_code | laddle_number | shift_type | final_c | final_mn | final_s | final_p | tested_by | remarks | report_picture | unique_code | created_at |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2026-02-24 11:00:14.946000+00:00 | 24B01 | Furnace2 | B | 3 | Day | 423 | 342 | None | 234 | Komal Sahu | sdfsdf | http://localhost:3004/uploads/qc-report-pictures/w | QC-JEJN | 2026-02-24 11:00:14.945816+00:00 |
| 2 | 2026-02-24 12:45:43.894000+00:00 | 24B02 | Furnace1 | A | 1 | Day | None | None | None | None | Sushil Bharti | asdasddasfd | https://batchcode.sagartmt.com//uploads/qc-report- | QC-PTIB | 2026-02-24 12:45:43.897185+00:00 |
| 3 | 2026-02-25 07:47:29.765000+00:00 | 25B01 | Furnace1 | A | 1 | Day | 324 | 234 | 324 | 234 | Sushil Bharti | dfsdf | https://batchcode.sagartmt.com//uploads/qc-report- | QC-VVMF | 2026-02-25 09:17:17.492441+00:00 |

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
- **`size`** (4 values): `['1 1/2" (25X50)', '2" (37X56)', '2" (68X25)', '3" (96X48)']`
- **`shift`** (1 values): `['Day']`
- **`unique_code`** (4 values): `['24B01B01', '24B02A01', '25B01A01', '25B02G01']`
- **`section`** (4 values): `['345', 'sdasd', 'sdfsd', 'sdfsdfs']`
- **`item_type`** (1 values): `['Square']`
- **`thickness`** (4 values): `['234', '34534', '423', 'sdfs']`
- **`picture`** (4 values): `['http://localhost:3004/uploads/pipe-mill-pictures/whatsappimage20260220at134241-1771930793410-837663929.jpeg', 'https://batchcode.sagartmt.com//uploads/pipe-mill-pictures/whatsappimage20260220at134241-1772011002435-199983118.jpeg', 'https://batchcode.sagartmt.com/uploads/pipe-mill-pictures/whatsappimage20260220at1342421-1772022422925-16782668.jpeg', 'https://batchcode.sagartmt.com//uploads/pipe-mill-pictures/whatsappimage20260220at134242-1771936674948-723020417.jpeg']`
- **`recoiler_short_code`** (4 values): `['24B01B', '24B02A', '25B01A', '25B02G']`
- **`mill_number`** (1 values): `['PIPE MILL 01']`
- **`quality_supervisor`** (2 values): `['Birendra Kumar Singh', 'Lekh Singh Patle']`
- **`mill_incharge`** (1 values): `['Ravi Singh']`
- **`forman_name`** (2 values): `['Hullash Paswan', 'Montu Aanand Ghosh']`
- **`fitter_name`** (2 values): `['Chandan Singh', 'Randhir Kumar']`
- **`remarks`** (3 values): `['adsasdsdasd', 'ffdgdf', 'sdfsd']`


### 🔍 Sample Data (First 3 rows):
| id | sample_timestamp | size | shift | pipe_mill | turbuse_name | turbine_is_ok | gas_flow_reading | blower_name | blower_is_ok | helper | unique_code | created_at | jobtime | production | time_start | time_end | section | item_type | thickness | picture | recoiler_short_code | mill_number | quality_supervisor | mill_incharge | forman_name | fitter_name | remarks |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2026-02-24 10:59:53.414000+00:00 | 3" (96X48) | Day | None | None | None | None | None | None | None | 24B01B01 | 2026-02-24 10:59:53.383811+00:00 | None | None | None | None | sdfsd | Square | sdfs | http://localhost:3004/uploads/pipe-mill-pictures/w | 24B01B | PIPE MILL 01 | Birendra Kumar Singh | Ravi Singh | Hullash Paswan | Randhir Kumar | sdfsd |
| 2 | 2026-02-24 12:37:54.951000+00:00 | 1 1/2" (25X50) | Day | None | None | None | None | None | None | None | 24B02A01 | 2026-02-24 12:37:54.953622+00:00 | None | None | None | None | sdasd | Square | 423 | https://batchcode.sagartmt.com//uploads/pipe-mill- | 24B02A | PIPE MILL 01 | Birendra Kumar Singh | Ravi Singh | Hullash Paswan | Randhir Kumar | adsasdsdasd |
| 3 | 2026-02-25 09:16:42.438000+00:00 | 2" (37X56) | Day | None | None | None | None | None | None | None | 25B01A01 | 2026-02-25 09:16:42.439234+00:00 | None | None | None | None | sdfsdfs | Square | 234 | https://batchcode.sagartmt.com//uploads/pipe-mill- | 25B01A | PIPE MILL 01 | Lekh Singh Patle | Ravi Singh | Montu Aanand Ghosh | Chandan Singh | None |

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
- **`status`** (2 values): `['active', 'Active']`


### 🔍 Sample Data (First 3 rows):
| client_id | client_name | city | contact_person | contact_details | sales_person_id | client_type | status | created_at | updated_at |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 8 | ABDULLAH TRADERS | NASHIK | AMIRULLAH CHAUDHARY | 9423478771 | 34 | CRR | active | 2026-01-30 07:50:35.922719 | 2026-01-30 07:50:35.922719 |
| 19 | ADVAIT STEEL MART | NULL | RAHUL JI | 9096722089 | 34 | NBD | active | 2026-01-30 07:50:35.922719 | 2026-01-30 07:50:35.922719 |
| 3 | AARADHYA STEEL | MAIHAR | GANESH JI | 8962109701 | 32 | CRR | active | 2026-01-30 07:50:35.922719 | 2026-01-30 07:50:35.922719 |

---

## 📋 Table: `make_quotation`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `BIGINT` | True |
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
| **grand_total** | `NUMERIC` | True |




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
- **`ship_to`** (2 values): `['NULL', 'safdsaf']`
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
| 2 | 2025-11-29 11:45:15.119642+00:00 | QN-004 | 2025-11-29 | Aakash | Chhattisgarh | Vipul |  | 9876501234 | 9811167788 | 27ABCDE1234F1Z5 | 27 | ABC Steels Pvt Ltd | Industrial Area, Raipur | NULL | Chhattisgarh | Manoj Singh | 9033442211 | 22AABCH1234Q1Z5 | 22 | MSME123456 | The above quoted prices are valid up to 5 days fro | 100% advance payment in the mode of NEFT, RTGS & D | Material is ready in our stock | Extra as per actual. | Transit insurance for all shipment is at Buyer's r | Extra as per actual. |  | 733605010000120 | Union Bank of India | MID CORP BR | UBIN0573361 | marketing@sagartmt.com | www.pankajgroup.in | ABCDE1234F | [{'gst': 18, 'qty': 1, 'code': 'ITM-1001', 'name': |  | 0.00 |
| 4 | 2025-11-29 11:47:07.550123+00:00 | QN-005 | 2025-11-29 | Aakash | Andhra Pradesh | Vipul |  | 9876501234 | 9811167788 | 27ABCDE1234F1Z5 | 27 | ABC Steels Pvt Ltd | Industrial Area, Raipur | NULL | Chhattisgarh | Manoj Singh | 9033442211 | 22AABCH1234Q1Z5 | 22 | MSME908776 | The above quoted prices are valid up to 5 days fro | 100% advance payment in the mode of NEFT, RTGS & D | Material is ready in our stock | Extra as per actual. | Transit insurance for all shipment is at Buyer's r | Extra as per actual. |  | 733605010000120 | Union Bank of India | MID CORP BR | UBIN0573361 | marketing@sagartmt.com | www.pankajgroup.in | ABCDE4455Z | [{'gst': 18, 'qty': 1, 'code': 'ITM-1001', 'name': |  | 0.00 |

---

## 📋 Table: `leave_request`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `INTEGER` | False |
| **employee_id** | `VARCHAR(100)` | True |
| **employee_name** | `VARCHAR(100)` | True |
| **designation** | `VARCHAR(100)` | True |
| **department** | `VARCHAR(100)` | True |
| **from_date** | `DATE` | True |
| **to_date** | `DATE` | True |
| **reason** | `TEXT` | True |
| **request_status** | `VARCHAR(50)` | True |
| **approved_by** | `VARCHAR(100)` | True |
| **hr_approval** | `VARCHAR(100)` | True |
| **approval_hr** | `VARCHAR(100)` | True |
| **approved_by_status** | `VARCHAR(50)` | True |
| **mobilenumber** | `VARCHAR(20)` | True |
| **urgent_mobilenumber** | `VARCHAR(20)` | True |
| **created_at** | `TIMESTAMP` | True |
| **updated_at** | `TIMESTAMP` | True |
| **commercial_head_status** | `VARCHAR(50)` | True |
| **approve_dates** | `DATE` | True |
| **user_id** | `INTEGER` | True |




### 🏷️ Categorical / Allowed Values:
- **`employee_id`** (13 values): `['100', 'S00016', 'S00039', 'S08076', 'S08362', 'S08434', 'S09103', 'S09298', 'S09470', 'S09531', 'S09578', 'S09630', 'S09755']`
- **`employee_name`** (13 values): `['Ajay Sahu', 'BIRBAL', 'Danveer Singh', 'Ganeshwar Chaturvedi', 'G Rammohan Rao', 'Hari Prasad', 'Kishan Kumar Rajak', 'K Ramesh Kumar', 'Manoj Nishad', 'Nilesh Rana', 'Shivraj Sharma', 'Shravan Nirmalkar', 'Vipin Pandey']`
- **`designation`** (7 values): `['', 'AGM PIPE MILL', 'EMPLOYEE RELATION MANAGER', 'OPERATION MANAGER', 'PC', 'PC HEAD', 'WEIGHBRIDGE OPERATOR']`
- **`department`** (6 values): `['HR', 'PC', 'PIPE MILL PRODUCTION', 'SMS ELECTRICAL', 'STRIP MILL ELECTRICAL', 'WB']`
- **`reason`** (16 values): `["Brother's marriage", 'Family problem going to Village', 'GOING TO HOMETOWN', 'Health problem', 'Holi Holiday', "my niece's wedding", 'Parsonal work', 'Personal reason', 'Personal Work', 'Personal Work', 'personnel work', 'PRASANOL WORK.', 'Prasonal', 'sister marriage', 'Tabiyat kharab hai', 'किराया रूम चेंज कर रहा हूँ 🙏🏻🙏🏻']`
- **`request_status`** (2 values): `['Approved', 'Pending']`
- **`approved_by`** (2 values): `['Amit Tiwari', 'K Ramesh Kumar']`
- **`hr_approval`** (1 values): `['Approved']`
- **`approval_hr`** (1 values): `['S09103']`
- **`approved_by_status`** (1 values): `['Approved']`
- **`mobilenumber`** (14 values): `['', '6263032883', '7089625040', '7348311805', '7999747599', '8602003474', '8602714849', '8878683267', '9329149372', '9329149381', '9644601458', '9770909934', '9770909942', '9770909946']`
- **`urgent_mobilenumber`** (10 values): `['', '6266919117', '6267030666', '7348311805', '7999747599', '9329149381', '9340638962', '9584910155', '9644601458', '9816399370']`
- **`commercial_head_status`** (1 values): `['Approved']`


### 🔍 Sample Data (First 3 rows):
| id | employee_id | employee_name | designation | department | from_date | to_date | reason | request_status | approved_by | hr_approval | approval_hr | approved_by_status | mobilenumber | urgent_mobilenumber | created_at | updated_at | commercial_head_status | approve_dates | user_id |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 100 | Danveer Singh |  | STRIP MILL ELECTRICAL | 2026-03-14 | 2026-03-28 | Family problem going to Village  | Pending | None | None | None | None | 7999747599 | 7999747599 | 2026-02-13 13:03:50.273317 | 2026-02-13 13:03:50.273317 | None | None | None |
| 8 | S08434 | Hari Prasad |  | STRIP MILL ELECTRICAL | 2026-02-25 | 2026-02-26 | Prasonal | Pending | None | None | None | None | 7348311805 | 7348311805 | 2026-02-24 07:47:36.738304 | 2026-02-24 07:47:36.738304 | None | None | 96 |
| 15 | S09578 | K Ramesh Kumar | PC HEAD | PC | 2026-02-27 | 2026-02-27 | Personal reason | Approved | None | Approved | S09103 | Approved | 9329149372 | 9584910155 | 2026-02-27 03:10:05.347280 | 2026-02-28 08:25:23.307816 | Approved | 2026-02-28 | 571 |

---

## 📋 Table: `visitors`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `INTEGER` | False |
| **visitor_name** | `VARCHAR(100)` | False |
| **mobile_number** | `VARCHAR(15)` | False |
| **visitor_photo** | `TEXT` | True |
| **visitor_address** | `TEXT` | True |
| **purpose_of_visit** | `TEXT` | True |
| **person_to_meet** | `VARCHAR(100)` | False |
| **date_of_visit** | `DATE` | False |
| **time_of_entry** | `TIME` | False |
| **visitor_out_time** | `TIME` | True |
| **approval_status** | `VARCHAR(20)` | True |
| **approved_by** | `VARCHAR(100)` | True |
| **approved_at** | `TIMESTAMP` | True |
| **status** | `VARCHAR(10)` | True |
| **gate_pass_closed** | `BOOLEAN` | True |
| **created_at** | `TIMESTAMP` | True |




### 🏷️ Categorical / Allowed Values:
- **`approval_status`** (1 values): `['approved']`
- **`status`** (2 values): `['IN', 'OUT']`
- **`gate_pass_closed`** (2 values): `['False', 'True']`


### 🔍 Sample Data (First 3 rows):
| id | visitor_name | mobile_number | visitor_photo | visitor_address | purpose_of_visit | person_to_meet | date_of_visit | time_of_entry | visitor_out_time | approval_status | approved_by | approved_at | status | gate_pass_closed | created_at |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 302 | Durgesh  | 9827492062 | None | Shiv om refrigeration  | Ac repairing  | Sandeep Kumar Dubey | 2026-01-28 | 12:23:00 | 13:05:14.791079 | approved | Sandeep Kumar Dubey | 2026-01-28 07:05:56.916325 | OUT | True | 2026-01-28 06:55:08.991007 |
| 296 | M Maity  | 7566098396 | https://srmpl-visitor-gatepass.s3.amazonaws.com/vi | Metaflux bhilai | Official  | Saroj Kumar Choudhary | 2026-01-26 | 12:17:00 | 13:38:53.156284 | approved | Saroj Kumar Choudhary | 2026-01-28 08:07:42.420309 | OUT | True | 2026-01-26 06:48:44.428295 |
| 371 | Vijay Kumar ji  | 9329013215 | https://srmpl-visitor-gatepass.s3.amazonaws.com/vi | Neeraj industries Bhilai  | None | Pawan Kumar Parganiha | 2026-02-12 | 13:30:00 | 15:50:08.132116 | approved | Pawan Kumar Parganiha | 2026-02-12 08:03:48.426482 | OUT | True | 2026-02-12 08:02:52.532539 |

---

## 📋 Table: `person_to_meet`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `INTEGER` | False |
| **person_to_meet** | `VARCHAR(100)` | False |
| **phone** | `VARCHAR(15)` | False |
| **created_at** | `TIMESTAMP` | True |




### 🏷️ Categorical / Allowed Values:
_No categorical columns detected_


### 🔍 Sample Data (First 3 rows):
| id | person_to_meet | phone | created_at |
| --- | --- | --- | --- |
| 2 | Sheelesh Marele | 8839494655 | 2026-01-13 06:43:37.496570 |
| 3 | Ajit Kumar Gupta | 9584556480 | 2026-01-13 06:43:37.496570 |
| 5 | Anil Kumar Mishra | 6266919126 | 2026-01-13 06:43:37.496570 |

---

## 📋 Table: `store_grn`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **planned_date** | `TIMESTAMP` | True |
| **grn_no** | `VARCHAR(50)` | True |
| **grn_date** | `DATE` | True |
| **party_name** | `VARCHAR(255)` | True |
| **party_bill_no** | `VARCHAR(100)` | True |
| **party_bill_amount** | `NUMERIC(14, 2)` | True |
| **sended_bill** | `BOOLEAN` | True |
| **approved_by_admin** | `BOOLEAN` | True |
| **approved_by_gm** | `BOOLEAN` | True |
| **close_bill** | `BOOLEAN` | True |




### 🏷️ Categorical / Allowed Values:
- **`sended_bill`** (1 values): `['True']`
- **`approved_by_admin`** (2 values): `['False', 'True']`
- **`approved_by_gm`** (1 values): `['False']`
- **`close_bill`** (1 values): `['False']`


### 🔍 Sample Data (First 3 rows):
| planned_date | grn_no | grn_date | party_name | party_bill_no | party_bill_amount | sended_bill | approved_by_admin | approved_by_gm | close_bill |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-01-13 05:16:31 | G325Y-04410 | 2026-01-10 | SHREE SAWARIYA SALES | SSS/25-26/1226 | 17606.00 | True | False | False | False |
| 2026-01-17 04:53:07 | G325Y-04501 | 2026-01-14 | SHREE SAWARIYA SALES | SSS/25-26/1245 | 41.00 | True | False | False | False |
| 2026-01-17 04:57:00 | G325Y-04502 | 2026-01-14 | SHREE SAWARIYA SALES | SSS/25-26/1244 | 5906.00 | True | False | False | False |

---

## 📋 Table: `plant_visitor`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `BIGINT` | False |
| **person_name** | `VARCHAR(150)` | True |
| **employee_code** | `VARCHAR(50)` | True |
| **reason_for_visit** | `TEXT` | True |
| **no_of_person** | `INTEGER` | True |
| **from_date** | `DATE` | True |
| **to_date** | `DATE` | True |
| **requester_name** | `VARCHAR(150)` | True |
| **request_for** | `VARCHAR(150)` | True |
| **remarks** | `TEXT` | True |
| **request_status** | `VARCHAR(50)` | True |
| **approv_employee_code** | `VARCHAR(50)` | True |
| **approve_by_name** | `VARCHAR(150)` | True |
| **created_at** | `TIMESTAMP` | True |
| **updated_at** | `TIMESTAMP` | True |




### 🏷️ Categorical / Allowed Values:
_No categorical columns detected_


### 🔍 Sample Data (First 3 rows):
_No data_

---

## 📋 Table: `indent`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `BIGINT` | False |
| **sample_timestamp** | `TIMESTAMP` | False |
| **form_type** | `VARCHAR(50)` | True |
| **request_number** | `VARCHAR(50)` | True |
| **indent_series** | `VARCHAR(50)` | True |
| **requester_name** | `VARCHAR(100)` | True |
| **department** | `VARCHAR(100)` | True |
| **division** | `VARCHAR(100)` | True |
| **item_code** | `VARCHAR(30)` | True |
| **product_name** | `VARCHAR(255)` | True |
| **request_qty** | `NUMERIC` | True |
| **uom** | `VARCHAR(20)` | True |
| **specification** | `TEXT` | True |
| **make** | `VARCHAR(100)` | True |
| **purpose** | `TEXT` | True |
| **cost_location** | `VARCHAR(255)` | True |
| **planned_1** | `TIMESTAMP` | True |
| **actual_1** | `TIMESTAMP` | True |
| **time_delay_1** | `VARCHAR(50)` | True |
| **request_status** | `VARCHAR(50)` | True |
| **approved_quantity** | `NUMERIC` | True |
| **created_at** | `TIMESTAMP` | True |
| **updated_at** | `TIMESTAMP` | True |
| **group_name** | `VARCHAR(100)` | True |
| **indent_number** | `VARCHAR(50)` | True |
| **gm_approval** | `VARCHAR(20)` | True |




### 🏷️ Categorical / Allowed Values:
- **`form_type`** (2 values): `['INDENT', 'REQUISITION']`
- **`request_number`** (9 values): `['IND09', 'IND10', 'IND11', 'IND12', 'IND14', 'IND15', 'IND16', 'IND17', 'REQ01']`
- **`indent_series`** (5 values): `['I1', 'I3', 'I4', 'I5', 'R4']`
- **`requester_name`** (4 values): `['Anup Kumar Bopche', 'BIRBAL', 'Hem Kumar Jagat', 'Shailesh Chitre']`
- **`department`** (4 values): `['AUTOMATION', 'PIPE MILL MAINTENANCE', 'PIPE MILL PRODUCTION', 'STRIP MILL PRODUCTION']`
- **`division`** (4 values): `['CO', 'PM', 'RP', 'SM']`
- **`item_code`** (11 values): `['C01010060', 'S01010003', 'S01010007', 'S01010009', 'S01030249', 'S01031407', 'S01150203', 'S01150347', 'S01180007', 'S01195981', 'S01330293']`
- **`product_name`** (11 values): `['AUTO LEVEL MAKE - SOKKIA MODEL  - B40A', 'BEARING 22252(URB)', 'BEARING 24052 (ARB)', 'COLD SAW CUTTER SHAFT (ALUMINIUM BODY)', 'ENGINE OIL 15W40', 'GLAND ROPE 12MM', 'GRINDING STONE 300X40 50.8 CGC60 (GREEN)', 'GUIDE STRIP 15X3MM', 'HOLDTITE', 'HT SPRING WASHER 14MM', 'VERNIER CALLIPER 12"']`
- **`uom`** (4 values): `['LTR', 'MT', 'NOS', 'PCS']`
- **`specification`** (7 values): `['', '1.1/2"x12"', '1/2"', 'As earlier purchase', 'dfghj', 'test', 'Type - SPL-HG/B S.NO. TH/03434']`
- **`make`** (8 values): `['', 'Bosch', 'Corborandaum', 'ertyu', 'Mitutoya', 'Shanthi gears(gmt)', 'test', 'URB']`
- **`purpose`** (10 values): `['', 'Coc lubrication', 'dfghj', 'For new pipe mill erection work', 'Gear box ,spair part', 'Grinding machine', 'Mill carden safe', 'Patra Patra mill fly weel', 'Siez cheking strips', 'test']`
- **`cost_location`** (8 values): `['', 'AUTOMOBILE & TRANSPORT', 'CRANE-1  (UNIT-1)', 'CRUSHER', 'MACHINE 2  (PIPE MILL)', 'PATRA MILL WORKSHOP', 'PIPE MILL', 'PIPE MILL (UNIT-2)']`
- **`time_delay_1`** (14 values): `['00:00:41.97', '00:01:05.183', '00:08:18.076', '00:22:31.637', '13 days 01:07:37.809', '13 days 01:07:53.399', '13 days 01:08:31.026', '13 days 01:08:55.434', '13 days 01:09:10.925', '13 days 01:09:19.251', '13 days 01:09:25.696', '13 days 01:09:36.465', '13 days 01:09:47.191', '5 days 22:51:43.416']`
- **`request_status`** (2 values): `['APPROVED', 'REJECTED']`
- **`group_name`** (6 values): `['ADHESIVE, TAPE & SEALANT', 'BEARING', 'CIVIL CONSTRUCTION', 'LUBRICANT & OIL', 'MECHANICAL', 'TOOLS']`
- **`indent_number`** (2 values): `['I325Y-00457', 'processed']`
- **`gm_approval`** (2 values): `['APPROVED', 'REJECTED']`


### 🔍 Sample Data (First 3 rows):
| id | sample_timestamp | form_type | request_number | indent_series | requester_name | department | division | item_code | product_name | request_qty | uom | specification | make | purpose | cost_location | planned_1 | actual_1 | time_delay_1 | request_status | approved_quantity | created_at | updated_at | group_name | indent_number | gm_approval |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 22 | 2026-02-12 09:30:38.379000+00:00 | INDENT | IND12 | I4 | Anup Kumar Bopche | PIPE MILL MAINTENANCE | PM | S01180007 | ENGINE OIL 15W40 | 210 | LTR |  |  | Coc lubrication  |  | 2026-02-12 09:30:38.379000+00:00 | 2026-02-25 10:39:33.813000+00:00 | 13 days 01:08:55.434 | REJECTED | 210 | 2026-02-12 09:30:36.900000+00:00 | 2026-02-25 10:39:33.810890+00:00 | LUBRICANT & OIL | None | None |
| 16 | 2026-02-12 09:30:38.164000+00:00 | INDENT | IND12 | I4 | Anup Kumar Bopche | PIPE MILL MAINTENANCE | PM | S01150203 | HT SPRING WASHER 14MM | 250 | PCS | 1/2" |  | Mill carden safe  | MACHINE 2  (PIPE MILL) | 2026-02-12 09:30:38.164000+00:00 | 2026-02-25 10:39:49.089000+00:00 | 13 days 01:09:10.925 | REJECTED | 250 | 2026-02-12 09:30:36.900000+00:00 | 2026-02-25 10:39:49.086592+00:00 | MECHANICAL | None | None |
| 25 | 2026-02-15 12:11:59.448000+00:00 | REQUISITION | REQ01 | R4 | Anup Kumar Bopche | PIPE MILL MAINTENANCE | PM | S01195981 | COLD SAW CUTTER SHAFT (ALUMINIUM BODY) | 1 | PCS | Type - SPL-HG/B S.NO. TH/03434 | Shanthi gears(gmt) | Gear box ,spair part | PIPE MILL | 2026-02-15 12:11:59.448000+00:00 | 2026-02-21 11:03:42.864000+00:00 | 5 days 22:51:43.416 | APPROVED | 1 | 2026-02-15 12:11:58.098000+00:00 | 2026-02-21 11:08:55.205374+00:00 | MECHANICAL | None | APPROVED |

---

## 📋 Table: `departments`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `INTEGER` | False |
| **department** | `VARCHAR(100)` | False |
| **hod** | `TEXT` | True |
| **mobile_number** | `VARCHAR(15)` | True |




### 🏷️ Categorical / Allowed Values:
- **`hod`** (4 values): `['Birbal', 'Mukesh Jain', 'Shailesh Chitre', 'Vibhuti Mohan Gupta']`
- **`mobile_number`** (4 values): `['7470898501', '9300099119', '9770909924', '9816399370']`


### 🔍 Sample Data (First 3 rows):
| id | department | hod | mobile_number |
| --- | --- | --- | --- |
| 1 | ACCOUNTS | None | None |
| 2 | ADMIN | None | None |
| 4 | CCM | None | None |

---

## 📋 Table: `indent_requests`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `INTEGER` | False |
| **indent_no** | `VARCHAR(50)` | False |
| **request_date** | `TIMESTAMP` | True |
| **department** | `VARCHAR(100)` | True |
| **requested_by** | `VARCHAR(100)` | True |
| **status** | `VARCHAR(20)` | True |
| **priority** | `VARCHAR(20)` | True |
| **purpose** | `TEXT` | True |
| **created_at** | `TIMESTAMP` | True |




### 🏷️ Categorical / Allowed Values:
_No categorical columns detected_


### 🔍 Sample Data (First 3 rows):
_No data_

---

## 📋 Table: `indent_items`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `INTEGER` | False |
| **indent_id** | `INTEGER` | True |
| **item_name** | `VARCHAR(255)` | False |
| **quantity** | `INTEGER` | False |
| **available_stock** | `INTEGER` | True |




### 🏷️ Categorical / Allowed Values:
_No categorical columns detected_


### 🔍 Sample Data (First 3 rows):
_No data_

---

## 📋 Table: `enquiry_tracker`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `BIGINT` | True |
| **timestamp** | `TIMESTAMP` | True |
| **enquiry_no** | `TEXT` | True |
| **enquiry_status** | `TEXT` | True |
| **what_did_customer_say** | `TEXT` | True |
| **current_stage** | `TEXT` | True |
| **followup_status** | `TEXT` | True |
| **next_call_date** | `TEXT` | True |
| **next_call_time** | `TEXT` | True |
| **is_order_received_status** | `TEXT` | True |
| **acceptance_via** | `TEXT` | True |
| **payment_mode** | `TEXT` | True |
| **payment_terms_in_days** | `INTEGER` | True |
| **transport_mode** | `TEXT` | True |
| **remark** | `TEXT` | True |
| **if_no_relevant_reason_status** | `TEXT` | True |
| **if_no_relevant_reason_remark** | `TEXT` | True |
| **customer_order_hold_reason_category** | `TEXT` | True |
| **holding_date** | `TEXT` | True |
| **hold_remark** | `TEXT` | True |
| **sales_cordinator** | `TEXT` | True |
| **calling_days** | `INTEGER` | True |
| **order_no** | `TEXT` | True |
| **party_name** | `TEXT` | True |
| **sales_person_name** | `TEXT` | True |




### 🏷️ Categorical / Allowed Values:
- **`enquiry_no`** (4 values): `['ARUN YADAV', 'EN-01', 'LD-003', 'LD-004']`
- **`enquiry_status`** (3 values): `['hot', 'open', 'warm']`
- **`what_did_customer_say`** (4 values): `['Customer said quotation under review', 'Reviewing Quote', 'sadfdsaf', 'sdfds']`
- **`current_stage`** (2 values): `['order-expected', 'order-status']`
- **`followup_status`** (1 values): `['Reviewing Quote']`
- **`next_call_date`** (2 values): `['2025-11-26', '2025-11-29']`
- **`next_call_time`** (4 values): `['11:01:00', '13:07:00', '13:12:00', '17:24:00']`
- **`is_order_received_status`** (3 values): `['hold', 'no', 'yes']`
- **`acceptance_via`** (2 values): `['email', 'whatsapp']`
- **`payment_mode`** (2 values): `['neft', 'rtgs']`
- **`transport_mode`** (2 values): `['by road', 'road transport']`
- **`remark`** (8 values): `['afdasfas', 'asdfas', 'asdfasfsa', 'asdfasfsadf', 'asfasfas', 'cdsFSA', 'demoo', 'sadfasfda']`
- **`if_no_relevant_reason_status`** (1 values): `['project on hold']`
- **`if_no_relevant_reason_remark`** (1 values): `['asdfsadf']`
- **`customer_order_hold_reason_category`** (1 values): `['customer documentation pending']`
- **`holding_date`** (1 values): `['2025-11-29']`
- **`hold_remark`** (1 values): `['wafasd']`
- **`order_no`** (7 values): `['DO-01', 'DO-02', 'DO-03', 'DO-04', 'DO-05', 'DO-06', 'DO-07']`


### 🔍 Sample Data (First 3 rows):
| id | timestamp | enquiry_no | enquiry_status | what_did_customer_say | current_stage | followup_status | next_call_date | next_call_time | is_order_received_status | acceptance_via | payment_mode | payment_terms_in_days | transport_mode | remark | if_no_relevant_reason_status | if_no_relevant_reason_remark | customer_order_hold_reason_category | holding_date | hold_remark | sales_cordinator | calling_days | order_no | party_name | sales_person_name |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2025-11-26 11:54:48.644062+00:00 | LD-003 | hot | Reviewing Quote | order-expected | Reviewing Quote | 2025-11-26 | 17:24:00 | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None | None |
| 2 | 2025-11-26 11:58:04.590322+00:00 | LD-003 | hot | Reviewing Quote | order-status | None | None | None | yes | email | rtgs | 1 | by road | asdfas | None | None | None | None | None | None | None | DO-01 | None | None |
| 4 | 2025-11-28 06:25:11.773008+00:00 | LD-003 | warm | Reviewing Quote | order-status | None | None | None | no | None | None | None | None | None | project on hold | asdfsadf | None | None | None | None | None | None | None | None |

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

## 📋 Table: `fms_leads`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `TEXT` | True |
| **created_at** | `TEXT` | True |
| **updated_at** | `TEXT` | True |
| **lead_no** | `TEXT` | True |
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
| **planned** | `TEXT` | True |
| **actual** | `TEXT` | True |
| **delay** | `TEXT` | True |
| **status** | `TEXT` | True |
| **customer_feedback** | `TEXT` | True |
| **enquiry_received_status** | `TEXT` | True |
| **enquiry_received_date** | `TEXT` | True |
| **enquiry_approach** | `TEXT` | True |
| **project_approx_value** | `TEXT` | True |
| **item_qty** | `TEXT` | True |
| **total_qty** | `TEXT` | True |
| **next_action** | `TEXT` | True |
| **next_call_date** | `TEXT` | True |
| **next_call_time** | `TEXT` | True |
| **planned1** | `TEXT` | True |
| **actual1** | `TEXT` | True |
| **delay1** | `TEXT` | True |
| **enquiry_status** | `TEXT` | True |
| **customer_say** | `TEXT` | True |
| **current_stage** | `TEXT` | True |
| **followup_status** | `TEXT` | True |
| **followup_next_call_date** | `TEXT` | True |
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
| **hold_date** | `TEXT` | True |
| **hold_remark** | `TEXT` | True |
| **sc_name** | `TEXT` | True |
| **planned_days** | `TEXT` | True |
| **leadscallingdays** | `TEXT` | True |
| **enquirycallingdays** | `TEXT` | True |
| **orderno** | `TEXT` | True |




### 🏷️ Categorical / Allowed Values:
- **`id`** (2 values): `['3', '4']`
- **`created_at`** (2 values): `['2025-11-25 10:08:09.30877+00', '2025-11-25 10:45:44.990059+00']`
- **`updated_at`** (2 values): `['2025-11-25 11:17:37.644367+00', '2025-11-28 06:43:38.412729+00']`
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
- **`planned`** (1 values): `['2025-11-26']`
- **`actual`** (1 values): `['2025-11-25']`
- **`status`** (1 values): `['Hot']`
- **`enquiry_received_status`** (1 values): `['yes']`
- **`enquiry_received_date`** (2 values): `['2025-11-24', '2025-11-27']`
- **`enquiry_approach`** (2 values): `['INWARD', 'Phone Call']`
- **`project_approx_value`** (2 values): `['21121.00', '231232.00']`
- **`item_qty`** (2 values): `['[{"name":"HR STRIP","quantity":"1212"}]', '[{"name":"HR STRIP","quantity":"12121"},{"name":"Fe500D TMT Bar","quantity":"121212"}]']`
- **`total_qty`** (2 values): `['1212', '133333']`
- **`next_action`** (1 values): `['awfasdfas']`
- **`next_call_date`** (2 values): `['2025-11-24', '2025-12-02']`
- **`next_call_time`** (2 values): `['16:33', '16:34']`
- **`planned1`** (2 values): `['2025-11-26', '2025-11-29']`
- **`actual1`** (2 values): `['2025-11-28', '2025-11-29']`
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
- **`planned_days`** (1 values): `['1']`
- **`orderno`** (1 values): `['DO-05']`


### 🔍 Sample Data (First 3 rows):
| id | created_at | updated_at | lead_no | lead_receiver_name | lead_source | company_name | phone_number | salesperson_name | location | email_address | state | address | nob | additional_notes | planned | actual | delay | status | customer_feedback | enquiry_received_status | enquiry_received_date | enquiry_approach | project_approx_value | item_qty | total_qty | next_action | next_call_date | next_call_time | planned1 | actual1 | delay1 | enquiry_status | customer_say | current_stage | followup_status | followup_next_call_date | followup_next_call_time | is_order_received | acceptance_via | payment_mode | payment_terms_days | transport_mode | remark | not_received_reason_status | not_received_reason_remark | customer_order_hold_category | hold_date | hold_remark | sc_name | planned_days | leadscallingdays | enquirycallingdays | orderno |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | 2025-11-25 10:08:09.30877+00 | 2025-11-25 11:17:37.644367+00 | LD-003 | TRIPATI RANA | WHATSAPP | Sourabh Rolling MIlls | 9827164305 | sadfsadf | asfasfasf | asdfsd@email.com | Arunachal Pradesh | asdfasfsa | safasd | fasfasfd | 2025-11-26 | 2025-11-25 | None | Hot | None | yes | 2025-11-24 | INWARD | 231232.00 | [{"name":"HR STRIP","quantity":"1212"}] | 1212 | awfasdfas | 2025-12-02 | 16:34 | 2025-11-26 | 2025-11-28 | None | hot | Reviewing Quote | order-status | None | None | None | yes | email | rtgs | 7 | by road | sadfasfda | project on hold | asdfsadf | None | None | None | ARUN YADAV | 1 | None | None | None |
| 4 | 2025-11-25 10:45:44.990059+00 | 2025-11-28 06:43:38.412729+00 | LD-004 | Aakash Agrawal | Indiamart | RBP Energy | 9022331100 | Rakesh Verma | Bilaspur, CG | rbp@gmail.com | Chhattisgarh | asfdas | Manufacturing | asdfdasf | 2025-11-26 | None | None | Hot | None | yes | 2025-11-27 | Phone Call | 21121.00 | [{"name":"HR STRIP","quantity":"12121"},{"name":"F | 133333 | awfasdfas | 2025-11-24 | 16:33 | 2025-11-29 | 2025-11-29 | None | open | Customer said quotation under review | order-status | None | None | None | yes | email | neft | 30 | road transport | asfasfas | None | None | None | None | None | Amit Pandey | 1 | None | None | DO-05 |

---

## 📋 Table: `leads_tracker`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `TEXT` | True |
| **created_at** | `TEXT` | True |
| **updated_at** | `TEXT` | True |
| **lead_no** | `TEXT` | True |
| **lead_source** | `TEXT` | True |
| **company_name** | `TEXT` | True |
| **phone_number** | `TEXT` | True |
| **sales_person_name** | `TEXT` | True |
| **location** | `TEXT` | True |
| **email_address** | `TEXT` | True |
| **status** | `TEXT` | True |
| **current_stage** | `TEXT` | True |
| **followup_status** | `TEXT` | True |
| **next_call_date** | `TEXT` | True |
| **remark** | `TEXT` | True |
| **calling_days** | `TEXT` | True |




### 🏷️ Categorical / Allowed Values:
- **`id`** (9 values): `['1', '2', '3', '4', '5', '6', '7', '8', '9']`
- **`created_at`** (9 values): `['2025-11-25 10:57:54.431151+00', '2025-11-25 10:58:25.812082+00', '2025-11-25 11:01:15.234733+00', '2025-11-25 11:03:36.617871+00', '2025-11-25 11:04:59.934056+00', '2025-11-25 11:06:41.442301+00', '2025-11-25 11:07:44.223505+00', '2025-11-25 11:17:37.61827+00', '2025-11-28 06:43:38.379908+00']`
- **`updated_at`** (2 values): `['LD-003', 'LD-004']`
- **`lead_no`** (2 values): `['Customer said quotation under review', 'Reviewing Quote']`
- **`lead_source`** (1 values): `['Hot']`
- **`company_name`** (2 values): `['expected', 'yes']`
- **`phone_number`** (4 values): `['2025-11-24', '2025-11-25', '2025-11-26', '2025-11-27']`
- **`sales_person_name`** (2 values): `['INWARD', 'Phone Call']`
- **`location`** (7 values): `['[]', '[{"name": "HR STRIP", "quantity": "1212"}]', '[{"name": "HR STRIP", "quantity": "1212121"}]', '[{"name": "HR STRIP", "quantity": "12121"}, {"name": "Fe500D TMT Bar", "quantity": "121212"}]', '[{"name": "MS BILLET", "quantity": "1212"}]', '[{"name": "MS BILLET", "quantity": "12121"}]', '[{"name": "MS PIPE1", "quantity": "212"}]']`
- **`email_address`** (6 values): `['0', '1212', '12121', '1212121', '133333', '212']`
- **`status`** (1 values): `['awfasdfas']`
- **`current_stage`** (2 values): `['2025-11-24', '2025-12-02']`
- **`followup_status`** (2 values): `['16:33', '16:34']`


### 🔍 Sample Data (First 3 rows):
| id | created_at | updated_at | lead_no | lead_source | company_name | phone_number | sales_person_name | location | email_address | status | current_stage | followup_status | next_call_date | remark | calling_days |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2025-11-25 10:57:54.431151+00 | LD-003 | Reviewing Quote | Hot | yes | 2025-11-26 | INWARD | [{"name": "MS BILLET", "quantity": "1212"}] | 1212 | None | None | None | None | None | None |
| 2 | 2025-11-25 10:58:25.812082+00 | LD-003 | Reviewing Quote | Hot | yes | 2025-11-25 | INWARD | [{"name": "MS PIPE1", "quantity": "212"}] | 212 | None | None | None | None | None | None |
| 3 | 2025-11-25 11:01:15.234733+00 | LD-003 | Reviewing Quote | Hot | yes | 2025-11-24 | INWARD | [{"name": "HR STRIP", "quantity": "1212121"}] | 1212121 | None | None | None | None | None | None |

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
| **rate** | `NUMERIC` | True |
| **description** | `TEXT` | True |
| **prepared_by** | `TEXT` | True |
| **followup_status** | `TEXT` | True |
| **reference_phone_no_2** | `TEXT` | True |
| **what_did_customer_say** | `TEXT` | True |




### 🏷️ Categorical / Allowed Values:
- **`lead_receiver_name`** (6 values): `['Amit Pandey', 'Anil Kumar Mishra', 'NULL', 'Rahul Sharma', 'Sheetal Patel', 'Tripati Rana']`
- **`lead_source`** (6 values): `['Direct Visit', 'Email', 'Indiamart', 'Referral', 'Telephonic', 'Whatsapp']`
- **`state`** (2 values): `['Chhattisgarh', 'NULL']`
- **`quotation_shared_by`** (2 values): `['NULL', 'Rahul Sharma']`
- **`enquiry_status`** (4 values): `['Followup', 'Hot', 'Open', 'Quotation Sent']`
- **`acceptance_via`** (2 values): `['Email', 'NULL']`
- **`payment_mode`** (4 values): `['Cash', 'NEFT', 'RTGS', 'UPI']`
- **`not_received_reason_status`** (5 values): `['Budget Constraints', 'Customer Busy', 'High Price', 'Low Budget', 'Need more time']`
- **`hold_reason_category`** (4 values): `['Budget Issue', 'Customer Documentation Pending', 'Not Interested', 'Project on hold']`
- **`consignee_company_name`** (2 values): `['Hamar Energy Pvt Ltd', 'NULL']`
- **`consignee_client_name`** (2 values): `['NULL', 'Prakash Sharma']`
- **`consignee_client_contact_no`** (2 values): `['9876543210', 'NULL']`
- **`consignee_billing_address`** (2 values): `['NULL', 'Raipur, Chhattisgarh - 492001']`
- **`consignee_state`** (2 values): `['Chhattisgarh', 'NULL']`
- **`consignee_gstin_uin`** (2 values): `['22AABCH1234Q1Z5', 'NULL']`
- **`consignee_state_code`** (2 values): `['22', 'NULL']`
- **`sp_name`** (6 values): `['Aakash', 'Harish', 'Rohit', 'S K Nayak', 'Tarun', 'Vipul']`
- **`reference_contact_no1`** (6 values): `['7723020095', '9000011111', '9876501234', '9898989898', '9993322110', '9999933333']`
- **`sp_state`** (6 values): `['Andhra Pradesh', 'Chhattisgarh', 'demo', 'Madhya Pradesh', 'Maharashtra', 'Odisha']`
- **`sp_state_code`** (5 values): `['21', '22', '23', '27', '36']`
- **`sp_pan`** (5 values): `['ABCDE1234F', 'ABCDE4455Z', 'FGHJK1234X', 'JKLPM9987D', 'MIJLP8877A']`
- **`consignor_bank_details`** (6 values): `['Account No.: 123456789012, HDFC Bank, Raipur', 'Account No.: 733605010000120 Bank Name: Union Bank of India Bank Address: MID CORP BR IFSC CODE: UBIN0573361 Email: marketing@sagartmt.com Website: www.pankajgroup.in', 'Axis Bank, Rourkela', 'Bank of Baroda, Indore', 'ICICI Bank, Nagpur Branch, A/C: 121212121212', 'Union Bank, MID CORP BR, A/C: 733605010000120']`
- **`consignor_state_code`** (5 values): `['21', '22', '23', '27', '36']`
- **`consignor_gstin`** (6 values): `['21ABCDE1111F1Z3', '22AABCH1234Q1Z5', '22AABCT1234E1Z2', '23AACCR1111R1Z2', '27ABCDE1234F1Z5', '36AAICS2367M1Z3']`
- **`consignor_msme_no`** (5 values): `['MSME123456', 'MSME1299', 'MSME55678', 'MSME908776', 'MSME9988']`
- **`lead_assign_to`** (2 values): `['Aakash Agrawal', 'NULL']`
- **`requirement_product_category`** (4 values): `['Angles', 'MS BILLET', 'Rod', 'TMT Bars']`
- **`sales_coordinator_name`** (6 values): `['Arun Yadav', 'Dayanand Kaiwartya', 'Jay Nirmal', 'Mohit Sinha', 'NULL', 'Shubham Pandey']`
- **`nob`** (5 values): `['Construction', 'Fabrication', 'Industrial', 'Manufacturing', 'Rolling']`
- **`enquiry_approach`** (3 values): `['Email', 'Phone', 'Phone Call']`
- **`requirement_product_category_codes`** (5 values): `['ANG-009', 'BLT-002', 'RBT-007', 'TMT-001', 'TMT-016']`
- **`live_company_name`** (6 values): `['Hamar Energy Pvt Ltd', 'MetalWorks India', 'Navkar Metals', 'RBP Energy', 'SRM Mining Pvt Ltd', 'Sunrise Casting']`
- **`live_person_name`** (6 values): `['Devendra Rao', 'Kaushal', 'Niraj', 'Prakash Sharma', 'Rakesh Verma', 'Santosh']`
- **`live_mobile`** (6 values): `['8888888888', '9022331100', '9090909090', '9123456780', '9876543210', '9988776655']`
- **`live_email_address`** (5 values): `['metalworks@gmail.com', 'navkar@gmail.com', 'rbp@gmail.com', 'srm@gmail.com', 'sunrise@gmail.com']`
- **`live_address`** (6 values): `['Bilaspur, CG', 'Indore, MP', 'Nagpur MIDC', 'Raipur, Chhattisgarh - 492001', 'Rourkela', 'Visakhapatnam, AP']`
- **`live_sc_name`** (6 values): `['Arun Yadav', 'Dayanand Kaiwartya', 'Jay Nirmal', 'Mohit Sinha', 'NULL', 'Shubham Pandey']`
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
- **`enquiry_receiver_name`** (6 values): `['Amit Pandey', 'Anil Kumar Mishra', 'NULL', 'Rahul Sharma', 'Sheetal Patel', 'Tripati Rana']`
- **`enquiry_assign_to`** (6 values): `['Abhishek', 'Akhil', 'Anshul', 'Rahul Sharma', 'Sagar TMT Sales Team', 'Vikas']`
- **`item_list`** (5 values): `['8mm Rod Qty 150', 'Angle 65x65 Qty 50', 'Fe500D TMT BAR - 12mm - Qty 500KG', 'Fe550D TMT - Qty 300KG', 'MS BILLET - 100mm']`
- **`description`** (5 values): `['High quality TMT bars suitable for construction', 'Premium grade TMT for high load', 'Standard billet for rolling mills', 'Standard rod for fabrication', 'Standard steel angle']`
- **`prepared_by`** (2 values): `['Aakash', 'NULL']`
- **`followup_status`** (3 values): `['Followup', 'Pending', 'Reviewing']`
- **`reference_phone_no_2`** (6 values): `['8888811111', '9000022222', '9811167788', '9898989898', '9900990099', '9998877665']`
- **`what_did_customer_say`** (5 values): `['Customer said quotation under review', 'Req: Send revised value', 'Reviewing Quote', 'Wants to negotiate', 'Will revert soon']`


### 🔍 Sample Data (First 3 rows):
| id | created_at | lead_receiver_name | lead_source | state | quotation_shared_by | enquiry_status | acceptance_via | payment_mode | not_received_reason_status | hold_reason_category | consignee_company_name | consignee_client_name | consignee_client_contact_no | consignee_billing_address | consignee_state | consignee_gstin_uin | consignee_state_code | sp_name | reference_contact_no1 | sp_state | sp_state_code | sp_pan | consignor_bank_details | consignor_state_code | consignor_gstin | consignor_msme_no | lead_assign_to | requirement_product_category | sales_coordinator_name | nob | enquiry_approach | requirement_product_category_codes | live_company_name | live_person_name | live_mobile | live_email_address | live_address | live_sc_name | live_source | direct_company_name | direct_client_name | direct_client_contact_no | direct_state | direct_billing_address | item_code | item_category | item_name | payment_terms_days | transport_mode | freight_type | payment_terms | enquiry_receiver_name | enquiry_assign_to | item_list | rate | description | prepared_by | followup_status | reference_phone_no_2 | what_did_customer_say |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | 2025-11-29 10:19:59.898706+00:00 | Rahul Sharma | Email | NULL | NULL | Hot | NULL | RTGS | Budget Constraints | Project on hold | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Harish | 7723020095 | Andhra Pradesh | 36 | ABCDE4455Z | Union Bank, MID CORP BR, A/C: 733605010000120 | 36 | 36AAICS2367M1Z3 | MSME908776 | NULL | MS BILLET | Dayanand Kaiwartya | Rolling | Email | BLT-002 | SRM Mining Pvt Ltd | Devendra Rao | 9988776655 | srm@gmail.com | Visakhapatnam, AP | Dayanand Kaiwartya | Whatsapp | 3M Projects Pvt Ltd | Rajesh Verma | 9823111000 | Andhra Pradesh | IDA Plot 4/A, Visakhapatnam | BLT-002 | MS Billet | MS Billet 100mm | 1 | BY ROAD | FOR | 100% ADVANCE | Anil Kumar Mishra | Akhil | MS BILLET - 100mm | 42000.00 | Standard billet for rolling mills | NULL | Reviewing | 9900990099 | Reviewing Quote |
| 4 | 2025-11-29 10:19:59.898706+00:00 | Tripati Rana | Referral | NULL | NULL | Followup | NULL | UPI | Customer Busy | Customer Documentation Pending | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Vipul | 9876501234 | Maharashtra | 27 | FGHJK1234X | ICICI Bank, Nagpur Branch, A/C: 121212121212 | 27 | 27ABCDE1234F1Z5 | MSME1299 | NULL | TMT Bars | Jay Nirmal | Industrial | Email | TMT-016 | Navkar Metals | Santosh | 8888888888 | navkar@gmail.com | Nagpur MIDC | Jay Nirmal | Exhibition | PQR Engineering Ltd | Ajay Gupta | 9001122334 | Maharashtra | MIDC Industrial Area, Nagpur | TMT-016 | TMT Bars | Fe550 TMT Bar | 15 | Transport | Paid | Advance | Rahul Sharma | Vikas | Fe550D TMT - Qty 300KG | 62000.00 | Premium grade TMT for high load | NULL | Pending | 9811167788 | Req: Send revised value |
| 5 | 2025-11-29 10:19:59.898706+00:00 | Amit Pandey | Direct Visit | NULL | NULL | Open | NULL | Cash | Low Budget | Not Interested | NULL | NULL | NULL | NULL | NULL | NULL | NULL | Rohit | 9000011111 | Madhya Pradesh | 23 | JKLPM9987D | Bank of Baroda, Indore | 23 | 23AACCR1111R1Z2 | MSME55678 | NULL | Angles | Mohit Sinha | Construction | Phone | ANG-009 | Sunrise Casting | Kaushal | 9123456780 | sunrise@gmail.com | Indore, MP | Mohit Sinha | Email | Royal Steel Traders | Irfan Khan | 9988771122 | Madhya Pradesh | Indore Industrial Belt | ANG-009 | Angles | Angle 65x65 | 0 | Self Pickup | NA | Immediate | Tripati Rana | Anshul | Angle 65x65 Qty 50 | 52000.00 | Standard steel angle | NULL | Pending | 9000022222 | Wants to negotiate |

---

## 📋 Table: `enq_erp`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `BIGINT` | False |
| **item_type** | `VARCHAR(100)` | True |
| **size** | `VARCHAR(100)` | True |
| **thickness** | `NUMERIC` | True |
| **enquiry_date** | `DATE` | True |
| **customer** | `VARCHAR(200)` | True |
| **quantity** | `INTEGER` | True |
| **created_at** | `TIMESTAMP` | True |
| **sales_executive** | `VARCHAR(300)` | True |




### 🏷️ Categorical / Allowed Values:
- **`item_type`** (3 values): `['rectangular', 'round', 'square']`
- **`size`** (20 values): `['19X19', '20X40', '25 OD', '25X25', '25X50', '25X68', '31X31', '32 OD', '37X56', '38X38', '42 OD', '47X47', '48 OD', '60 OD', '62X62', '72X72', '76 OD', '80X40', '88 OD', '96X48']`
- **`sales_executive`** (3 values): `['Dayanand Kaiwartya', 'Jai Nirmal', 'Mohit Sinha']`


### 🔍 Sample Data (First 3 rows):
| id | item_type | size | thickness | enquiry_date | customer | quantity | created_at | sales_executive |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 131 | round | 48 OD | 3.20 | 2026-02-05 | Mega iran  | 27 | 2026-02-05 10:43:48.745835 | Dayanand Kaiwartya |
| 112 | square | 19X19 | 1.50 | 2026-02-05 | Mega iron  | 10 | 2026-02-05 10:26:58.778717 | Dayanand Kaiwartya |
| 113 | square | 47X47 | 1.50 | 2026-02-05 | Mega iron  | 5 | 2026-02-05 10:26:58.783082 | Dayanand Kaiwartya |

---

## 📋 Table: `client_followups`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **followup_id** | `INTEGER` | False |
| **client_name** | `VARCHAR(150)` | False |
| **sales_person** | `VARCHAR(150)` | False |
| **actual_order** | `NUMERIC` | True |
| **actual_order_date** | `DATE` | True |
| **date_of_calling** | `DATE` | False |
| **next_calling_date** | `DATE` | True |
| **created_at** | `TIMESTAMP` | True |
| **updated_at** | `TIMESTAMP` | True |




### 🏷️ Categorical / Allowed Values:
- **`sales_person`** (5 values): `['Amit Pandey', 'Anil Kumar Mishra', 'Rahul Sharma', 'Sheetal Patel', 'Tripati Rana']`


### 🔍 Sample Data (First 3 rows):
| followup_id | client_name | sales_person | actual_order | actual_order_date | date_of_calling | next_calling_date | created_at | updated_at |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | AA GOLEWALE | Anil Kumar Mishra | None | None | 2026-02-02 | None | 2026-02-27 11:20:02.598063 | 2026-02-27 11:20:02.598063 |
| 2 | AA GOLEWALE | Anil Kumar Mishra | None | None | 2026-02-12 | None | 2026-02-27 11:20:02.598063 | 2026-02-27 11:20:02.598063 |
| 3 | AA GOLEWALE | Anil Kumar Mishra | None | None | 2026-02-20 | None | 2026-02-27 11:20:02.598063 | 2026-02-27 11:20:02.598063 |

---

## 📋 Table: `request`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `INTEGER` | False |
| **person_name** | `VARCHAR(100)` | False |
| **no_of_person** | `INTEGER` | True |
| **from_date** | `DATE` | True |
| **to_date** | `DATE` | True |
| **type_of_travel** | `VARCHAR(50)` | True |
| **departure_date** | `DATE` | True |
| **reason_for_travel** | `VARCHAR(255)` | True |
| **request_no** | `VARCHAR(50)` | True |
| **requester_name** | `VARCHAR(255)` | True |
| **requester_designation** | `VARCHAR(255)` | True |
| **requester_department** | `VARCHAR(255)` | True |
| **request_for** | `VARCHAR(255)` | True |
| **request_quantity** | `INTEGER` | True |
| **experience** | `VARCHAR(100)` | True |
| **education** | `VARCHAR(255)` | True |
| **remarks** | `TEXT` | True |
| **request_status** | `VARCHAR(50)` | True |
| **created_at** | `TIMESTAMP` | True |
| **updated_at** | `TIMESTAMP` | True |
| **employee_code** | `VARCHAR(100)` | True |
| **from_city** | `VARCHAR(100)` | True |
| **to_city** | `VARCHAR(100)` | True |




### 🏷️ Categorical / Allowed Values:
- **`person_name`** (1 values): `['Girdhari Lal']`
- **`request_no`** (2 values): `['T-0001', 'T-0002']`
- **`requester_name`** (1 values): `['Girdhari Lal']`
- **`requester_department`** (1 values): `['SMS ELECTRICAL']`
- **`request_status`** (1 values): `['Open']`
- **`employee_code`** (1 values): `['S09061']`


### 🔍 Sample Data (First 3 rows):
| id | person_name | no_of_person | from_date | to_date | type_of_travel | departure_date | reason_for_travel | request_no | requester_name | requester_designation | requester_department | request_for | request_quantity | experience | education | remarks | request_status | created_at | updated_at | employee_code | from_city | to_city |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Girdhari Lal | 1 | None | None | None | None | None | T-0001 | Girdhari Lal | None | SMS ELECTRICAL | None | None | None | None | None | Open | 2026-02-24 01:54:01.593021 | 2026-02-24 01:54:01.593021 | S09061 | None | None |
| 2 | Girdhari Lal | 1 | None | None | None | None | None | T-0002 | Girdhari Lal | None | SMS ELECTRICAL | None | None | None | None | None | Open | 2026-02-24 01:54:07.262325 | 2026-02-24 01:54:07.262325 | S09061 | None | None |

---

## 📋 Table: `re_coiler`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `INTEGER` | False |
| **sample_timestamp** | `TIMESTAMP` | True |
| **hot_coiler_short_code** | `VARCHAR(50)` | False |
| **size** | `VARCHAR(50)` | True |
| **supervisor** | `VARCHAR(100)` | True |
| **incharge** | `VARCHAR(100)` | True |
| **contractor** | `VARCHAR(100)` | True |
| **machine_number** | `VARCHAR(50)` | True |
| **welder_name** | `VARCHAR(100)` | True |
| **unique_code** | `VARCHAR(50)` | False |
| **created_at** | `TIMESTAMP` | True |
| **shift** | `VARCHAR(20)` | True |




### 🏷️ Categorical / Allowed Values:
- **`hot_coiler_short_code`** (4 values): `['24B01', '24B02', '25B01', '25B02']`
- **`size`** (4 values): `['234', '342', '54435', '5454']`
- **`supervisor`** (3 values): `['Karmalal Nishad', 'Ramdhan Verma', 'Vijay Raut']`
- **`incharge`** (2 values): `['Ramdhan Verma', 'Toman Lal Sahu']`
- **`contractor`** (1 values): `['Dhananjay (CT)']`
- **`machine_number`** (3 values): `['SRMPL01', 'SRMPL02', 'SRMPL07']`
- **`welder_name`** (3 values): `['Badshah Khan', 'Jitendra', 'Nirmal']`
- **`unique_code`** (4 values): `['24B01B', '24B02A', '25B01A', '25B02G']`
- **`shift`** (1 values): `['Day']`


### 🔍 Sample Data (First 3 rows):
| id | sample_timestamp | hot_coiler_short_code | size | supervisor | incharge | contractor | machine_number | welder_name | unique_code | created_at | shift |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2026-02-24 10:59:21.906000+00:00 | 24B01 | 342 | Vijay Raut | Toman Lal Sahu | Dhananjay (CT) | SRMPL02 | Nirmal | 24B01B | 2026-02-24 10:59:21.888377+00:00 | Day |
| 2 | 2026-02-24 12:25:26.305000+00:00 | 24B02 | 5454 | Ramdhan Verma | Toman Lal Sahu | Dhananjay (CT) | SRMPL01 | Jitendra | 24B02A | 2026-02-24 12:25:26.308789+00:00 | Day |
| 3 | 2026-02-25 08:32:00.189000+00:00 | 25B01 | 234 | Vijay Raut | Ramdhan Verma | Dhananjay (CT) | SRMPL01 | Badshah Khan | 25B01A | 2026-02-25 08:32:00.191350+00:00 | Day |

---

## 📋 Table: `login`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `BIGINT` | False |
| **create_at** | `TIMESTAMP` | True |
| **user_name** | `VARCHAR(150)` | False |
| **password** | `TEXT` | False |
| **role** | `VARCHAR(50)` | True |
| **user_id** | `VARCHAR(50)` | True |
| **email** | `VARCHAR(200)` | True |
| **number** | `VARCHAR(20)` | True |
| **department** | `VARCHAR(100)` | True |
| **give_by** | `VARCHAR(150)` | True |
| **status** | `VARCHAR(20)` | True |
| **user_acess** | `VARCHAR(200)` | True |
| **employee_id** | `VARCHAR(50)` | True |
| **createdate** | `TIMESTAMP` | True |
| **updatedate** | `TIMESTAMP` | True |




### 🏷️ Categorical / Allowed Values:
_No categorical columns detected_


### 🔍 Sample Data (First 3 rows):
_No data_

---

## 📋 Table: `maintenance_task_assign`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `BIGINT` | False |
| **created_at** | `TIMESTAMP` | True |
| **time_stamp** | `TIMESTAMP` | True |
| **task_no** | `VARCHAR(50)` | True |
| **serial_no** | `VARCHAR(100)` | True |
| **machine_name** | `VARCHAR(255)` | True |
| **given_by** | `VARCHAR(255)` | True |
| **doer_name** | `VARCHAR(255)` | True |
| **task_type** | `VARCHAR(100)` | True |
| **machine_area** | `VARCHAR(255)` | True |
| **part_name** | `VARCHAR(255)` | True |
| **need_sound_test** | `BOOLEAN` | True |
| **temperature** | `VARCHAR(50)` | True |
| **enable_reminders** | `BOOLEAN` | True |
| **require_attachment** | `BOOLEAN` | True |
| **task_start_date** | `DATE` | True |
| **frequency** | `VARCHAR(50)` | True |
| **description** | `TEXT` | True |
| **priority** | `VARCHAR(50)` | True |
| **machine_department** | `VARCHAR(100)` | True |
| **actual_date** | `DATE` | True |
| **delay** | `VARCHAR(50)` | True |
| **task_status** | `VARCHAR(50)` | True |
| **remarks** | `TEXT` | True |
| **sound_status** | `VARCHAR(50)` | True |
| **temperature_status** | `VARCHAR(50)` | True |
| **image_link** | `TEXT` | True |
| **file_name** | `VARCHAR(255)` | True |
| **file_type** | `VARCHAR(100)` | True |
| **maintenance_cost** | `NUMERIC` | True |
| **doer_department** | `VARCHAR(255)` | True |
| **division** | `VARCHAR(200)` | True |




### 🏷️ Categorical / Allowed Values:
- **`given_by`** (19 values): `['ANIL KUMAR MISHRA', 'ANUP KUMAR BOPCHE', 'BALDEV SINGH SAINI', 'DANVEER SINGH', 'DEEPAK BHALLA', 'DHANJI', 'G RAM MOHAN RAO', 'GUNJAN TIWARI', 'HULLAS PASWAN', 'MRIGENDRA NARAYAN BEPARI', 'RAJNISH BHARDWAJ', 'RINKU GAUTAM', 'ROSHAN RAJAK', 'SACHIN SAXENA', 'SANDEEP DUBEY', 'SHAILESH CHITRE', 'SHREE RAM PATLE', 'SUMAN JHA', 'TEJ BAHADUR YADAV']`
- **`task_type`** (1 values): `['Maintenance']`
- **`machine_area`** (25 values): `['', 'Continues mill', 'Finish mill', 'I', 'Mill', 'Patra mill workshop', 'PIPE MILL', 's', 'S', 'Sms crene', 'Strip mill', 'Strip Mill', 'U', 'uint-1', 'unit-1', 'Unit 1', 'Unit-1', 'UNIT-1', 'UNIT- 1', 'unit-2', 'UNIT-2', 'UNIT- 2', 'Workshop', 'यूनिट 1', 'यूनिट 2']`
- **`part_name`** (24 values): `['', '`', 'Carbon brush', 'Carbon brush and clean', 'Carbon brush and clean motor', 'Check all motor and check carbon brush.', 'Check and clean', 'Check carbon', 'Check connection clean motor', 'Check feeder and contractor kit', 'Check kit and clean panel', 'Check kit and loose connection clean panel', 'Clean and change carbon brush', 'Contractor kit', 'Lt motor', 'Lub oil and coolant water', 'Lub oil cleaning', 'Motor', 'Motor and blower', 'n', 'No', 'PIPE MILL', 'UNIT-1', 'UNIT- 1']`
- **`need_sound_test`** (2 values): `['False', 'True']`
- **`temperature`** (3 values): `['', 'No', 'Yes']`
- **`enable_reminders`** (2 values): `['False', 'True']`
- **`require_attachment`** (2 values): `['False', 'True']`
- **`frequency`** (4 values): `['daily', 'monthly', 'one-time', 'weekly']`
- **`priority`** (11 values): `['', '15 DAY', '15 DAYS', '1 MONTH', 'DAILY', 'High', 'Low', 'Medium', 'MONTHLY', 'Urgent', 'WEEKLY']`
- **`machine_department`** (9 values): `['CCM', 'PIPE MILL ELECTRICAL', 'PIPE MILL MAINTENANCE', 'SMS ELECTRICAL', 'SMS MAINTENANCE', 'STRIP MILL ELECTRICAL', 'STRIP MILL PRODUCTION', 'TRANSPORT', 'WORKSHOP']`
- **`task_status`** (4 values): `['no', 'No', 'yes', 'Yes']`
- **`remarks`** (1 values): `['']`
- **`sound_status`** (5 values): `['', 'Bad', 'Good', 'Need Repair', 'OK']`
- **`temperature_status`** (16 values): `['', '31', '32', '40', '48', 'Holiday', 'Leave', 'Liive', 'Live', 'Live', 'No', 'ok', 'T', 'temp', 'Yes', 'लिव']`
- **`doer_department`** (10 values): `['CCM', 'PIPE MILL ELECTRICAL', 'PIPE MILL MAINTENANCE', 'PIPE MILL PRODUCTION', 'SMS ELECTRICAL', 'SMS MAINTENANCE', 'STRIP MILL ELECTRICAL', 'STRIP MILL MAINTENANCE', 'STRIP MILL PRODUCTION', 'WORKSHOP']`
- **`division`** (3 values): `['PIPE MILL', 'SMS', 'STRIP MILL']`


### 🔍 Sample Data (First 3 rows):
| id | created_at | time_stamp | task_no | serial_no | machine_name | given_by | doer_name | task_type | machine_area | part_name | need_sound_test | temperature | enable_reminders | require_attachment | task_start_date | frequency | description | priority | machine_department | actual_date | delay | task_status | remarks | sound_status | temperature_status | image_link | file_name | file_type | maintenance_cost | doer_department | division |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2680 | 2025-12-22 09:50:28.971971+00:00 | 2025-12-03 15:29:00 | TM-2672 | SM/WS/LTSF-12 | SHAPER MACHINE 2 | DHANJI | Rakesh Kumar | Maintenance | Workshop | None | False | No | True | False | 2026-01-10 | daily | गेयर चेक, बेल्ट चेक, ऑयलिंग और ग्रीसिंग | Medium | WORKSHOP | 2026-01-20 | None | Yes | None | Good | None | None | None | None | None | WORKSHOP | STRIP MILL |
| 75 | 2025-12-22 09:50:28.971971+00:00 | 2025-11-28 15:35:00 | TM-075 | SM/MILL/DG-003 | COMPRESSOR1 | None | Shiv Kumar Yadav | Maintenance | Strip mill | Motor  | False | No | False | False | 2026-01-14 | weekly | Check and clean  | WEEKLY | STRIP MILL ELECTRICAL | None | None | No | None | None | None | None | None | None | None | STRIP MILL PRODUCTION | STRIP MILL |
| 76 | 2025-12-22 09:50:28.971971+00:00 | 2025-11-28 15:35:00 | TM-076 | SM/MILL/DG-003 | COMPRESSOR1 | None | Shiv Kumar Yadav | Maintenance | Strip mill | Motor  | False | No | False | False | 2026-01-21 | weekly | Check and clean  | WEEKLY | STRIP MILL ELECTRICAL | None | None | No | None | None | None | None | None | None | None | STRIP MILL PRODUCTION | STRIP MILL |

---

## 📋 Table: `assign_task`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `INTEGER` | False |
| **task_id** | `VARCHAR(50)` | False |
| **department** | `VARCHAR(100)` | True |
| **given_by** | `VARCHAR(100)` | True |
| **name** | `VARCHAR(100)` | True |
| **task_description** | `TEXT` | True |
| **remark** | `TEXT` | True |
| **status** | `VARCHAR(50)` | True |
| **image** | `TEXT` | True |
| **attachment** | `TEXT` | True |
| **frequency** | `VARCHAR(50)` | True |
| **task_start_date** | `TIMESTAMP` | True |
| **submission_date** | `TIMESTAMP` | True |
| **delay** | `INTEGER` | True |
| **remainder** | `VARCHAR(100)` | True |
| **created_at** | `TIMESTAMP` | True |
| **hod** | `VARCHAR(255)` | True |
| **doer_name2** | `VARCHAR(255)` | True |
| **division** | `VARCHAR(300)` | True |
| **doer_department** | `TEXT` | True |




### 🏷️ Categorical / Allowed Values:
- **`department`** (25 values): `['Admin Office - First Floor', 'Admin Office - Ground Floor', 'Back Office', 'Canteen Area 1 & 2', 'Car Parking Area', 'CCM PLC Panel Room', 'CCM SBO Panel Room', 'Container Office', 'Labour Colony', 'Main Gate', 'Mandir', 'New Lab', 'Patra Mill AC Panel Room', 'Patra Mill DC Panel Room', 'Patra Mill Foreman Office', 'Patra Mill SBO Panel', 'Pipe Mill', 'Plant Area', 'SMS Electrical Store Room', 'SMS Office', 'SMS Panel Room', 'Store Office', 'TMT Foreman Office', 'Weight Office & Kata In/Out', 'Workshop']`
- **`given_by`** (3 values): `['AAKASH AGRAWAL', 'AJIT KUMAR GUPTA', 'SHEELESH MARELE']`
- **`name`** (2 values): `['Company Reja', 'Housekeeping Staff']`
- **`status`** (2 values): `['no', 'Yes']`
- **`attachment`** (1 values): `['confirmed']`
- **`frequency`** (3 values): `['daily', 'monthly', 'weekly']`
- **`doer_name2`** (4 values): `['Makhan Lal', 'Sarad Behera', 'Tikeshwar Chakradhari(Hk)', 'Tikeshware Chakradhari(KH)']`
- **`division`** (4 values): `['COMMERCIAL', 'PIPE MILL', 'SMS', 'STRIP MILL']`
- **`doer_department`** (11 values): `['ADMIN', 'CCM', 'HR', 'LAB AND QUALITY CONTROL', 'PIPE MILL PRODUCTION', 'SECURITY', 'SMS ELECTRICAL', 'STORE', 'STRIP MILL ELECTRICAL', 'WB', 'WORKSHOP']`


### 🔍 Sample Data (First 3 rows):
| id | task_id | department | given_by | name | task_description | remark | status | image | attachment | frequency | task_start_date | submission_date | delay | remainder | created_at | hod | doer_name2 | division | doer_department |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 271691 | 271691 | TMT Foreman Office | SHEELESH MARELE | Housekeeping Staff | झाड़ू से सफाई किया गया | ok | Yes | None | confirmed | daily | 2026-01-19 00:00:00+00:00 | 2026-01-19 08:13:30.727000+00:00 | None | None | 2026-02-18 11:07:00 | Sparsh Jha | None | COMMERCIAL | ADMIN |
| 271702 | 271702 | TMT Foreman Office | SHEELESH MARELE | Housekeeping Staff | झाड़ू से सफाई किया गया | ok | Yes | None | confirmed | daily | 2026-01-30 00:00:00+00:00 | 2026-01-30 07:24:21.428000+00:00 | None | None | 2026-02-18 11:07:00 | Sparsh Jha | None | COMMERCIAL | ADMIN |
| 271732 | 271732 | TMT Foreman Office | SHEELESH MARELE | Housekeeping Staff | झाड़ू से सफाई किया गया | ok | Yes | None | confirmed | daily | 2026-03-01 00:00:00+00:00 | 2026-03-01 08:54:16.739000+00:00 | 57 | None | 2026-02-18 11:07:00 | makhan | Makhan Lal | COMMERCIAL | ADMIN |

---

## 📋 Table: `locations`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **location_id** | `INTEGER` | False |
| **location** | `TEXT` | False |




### 🏷️ Categorical / Allowed Values:
_No categorical columns detected_


### 🔍 Sample Data (First 3 rows):
| location_id | location |
| --- | --- |
| 2 | Admin Office - First Floor |
| 3 | Admin Office - Ground Floor |
| 4 | Back Office |

---

## 📋 Table: `form_responses`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `INTEGER` | False |
| **serial_no** | `VARCHAR(100)` | True |
| **machine_name** | `VARCHAR(255)` | True |
| **purchase_date** | `DATE` | True |
| **purchase_price** | `NUMERIC` | True |
| **vendor** | `VARCHAR(255)` | True |
| **model_no** | `VARCHAR(100)` | True |
| **warranty_expiration** | `DATE` | True |
| **manufacturer** | `VARCHAR(255)` | True |
| **maintenance_schedule** | `VARCHAR(255)` | True |
| **department** | `VARCHAR(255)` | True |
| **location** | `VARCHAR(255)` | True |
| **initial_maintenance_date** | `DATE` | True |
| **user_manual** | `TEXT` | True |
| **purchase_bill** | `TEXT` | True |
| **notes** | `TEXT` | True |
| **tag_no** | `VARCHAR(100)` | True |
| **user_allot** | `VARCHAR(255)` | True |




### 🏷️ Categorical / Allowed Values:
- **`maintenance_schedule`** (14 values): `['15 DAY', '15 DAYS', '1 MONTH', '30 DAYS', '7 DAY', '7DAYS', '7 DAYS', '8 MONTH', 'Daily', 'DAILY', 'Daily, Weekly', 'Half-Yearly', 'MONTHLY', 'Weekly']`
- **`department`** (14 values): `['ALL ELECTRICAL', 'CCM', 'CCM MAINTENANCE', 'IT', 'LAB AND QUALITY CONTROL', 'PIPE MILL ELECTRICAL', 'PIPE MILL MAINTENANCE', 'SMS ELECTRICAL', 'SMS MAINTENANCE', 'STORE', 'STRIP MILL ELECTRICAL', 'STRIP MILL PRODUCTION', 'TRANSPORT', 'WORKSHOP']`
- **`user_allot`** (5 values): `['30:01:00', '40:01:00', '80:01:00', 'SPECTRO', 'user']`


### 🔍 Sample Data (First 3 rows):
| id | serial_no | machine_name | purchase_date | purchase_price | vendor | model_no | warranty_expiration | manufacturer | maintenance_schedule | department | location | initial_maintenance_date | user_manual | purchase_bill | notes | tag_no | user_allot |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | SRMPL\ALL IN ONE\01 | ALL IN ONE PC | None | None | None | None | None | None | None | IT | None | None | None | None | None | SRMPL\ALL IN ONE\01 | None |
| 2 | SRMPL\KEYBOARD\01 | KEYBOARD | None | None | None | None | None | None | None | IT | None | None | None | None | None | SRMPL\KEYBOARD\01 | None |
| 3 | SRMPL\MOUSE\01 | MOUSE | None | None | None | None | None | None | None | IT | None | None | None | None | None | SRMPL\MOUSE\01 | None |

---

## 📋 Table: `master`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `BIGINT` | False |
| **doer_name** | `TEXT` | True |
| **department1** | `TEXT` | True |
| **given_by** | `TEXT` | True |
| **task_status** | `TEXT` | True |
| **task_type** | `TEXT` | True |
| **priority** | `TEXT` | True |
| **created_at** | `TIMESTAMP` | True |
| **department** | `TEXT` | True |




### 🏷️ Categorical / Allowed Values:
- **`given_by`** (24 values): `['AAKASH AGRAWAL', 'AK GUPTA', 'ANIL KUMAR MISHRA', 'ANUP KUMAR BOPCHE', 'BALDEV SINGH SAINI', 'DANVEER SINGH', 'DEEPAK BHALLA', 'DHANJI', 'G RAM MOHAN RAO', 'GUNJAN TIWARI', 'HULLAS PASWAN', 'MANTU ANAND GHOSE', 'MRIGENDRA NARAYAN BEPARI', 'RAJNISH BHARDWAJ', 'RAVI KUMAR SINGH', 'RINKU GAUTAM', 'RINKU SINGH', 'ROSHAN RAJAK', 'SACHIN SAXENA', 'SANDEEP DUBEY', 'SHAILESH CHITRE', 'SHREE RAM PATLE', 'SUMAN JHA', 'TEJ BAHADUR YADAV']`
- **`task_status`** (1 values): `['In House']`
- **`task_type`** (1 values): `['Maintence']`
- **`priority`** (3 values): `['High', 'Low', 'Urgent']`
- **`department`** (14 values): `['ALL ELECTRICAL', 'CCM', 'CCM MAINTENANCE', 'LAB AND QUALITY CONTROL', 'PIPE MILL ELECTRICAL', 'PIPE MILL MAINTENANCE', 'PIPE MILL PRODUCTION', 'SMS ELECTRICAL', 'SMS MAINTENANCE', 'STORE', 'STRIP MILL ELECTRICAL', 'STRIP MILL MAINTENANCE', 'STRIP MILL PRODUCTION', 'TRANSPORT']`


### 🔍 Sample Data (First 3 rows):
| id | doer_name | department1 | given_by | task_status | task_type | priority | created_at | department |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | SKNayak | ACCOUNTS | AAKASH AGRAWAL | In House | Maintence | Low | 2025-11-25 05:24:01.832024+00:00 | PIPE MILL ELECTRICAL |
| 3 | Pintu Pandit | ADMIN | RINKU SINGH | None | None | High | 2025-11-25 05:24:01.832024+00:00 | LAB AND QUALITY CONTROL |
| 4 | Rupesh Kumar Rawat | ADMIN | DANVEER SINGH | None | None | Urgent | 2025-11-25 05:24:01.832024+00:00 | SMS ELECTRICAL |

---

## 📋 Table: `all_loans`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `BIGINT` | False |
| **loan_name** | `VARCHAR(255)` | False |
| **bank_name** | `VARCHAR(255)` | False |
| **amount** | `NUMERIC(15, 2)` | False |
| **emi** | `NUMERIC(12, 2)` | False |
| **loan_start_date** | `DATE` | False |
| **loan_end_date** | `DATE` | False |
| **provided_document_name** | `VARCHAR(255)` | True |
| **upload_document** | `TEXT` | True |
| **remarks** | `TEXT` | True |
| **created_at** | `TIMESTAMP` | True |




### 🏷️ Categorical / Allowed Values:
_No categorical columns detected_


### 🔍 Sample Data (First 3 rows):
_No data_

---

## 📋 Table: `approval_history`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `INTEGER` | False |
| **approval_no** | `VARCHAR(50)` | True |
| **subscription_no** | `VARCHAR(50)` | True |
| **approval_status** | `VARCHAR(50)` | True |
| **note** | `TEXT` | True |
| **approved_by** | `VARCHAR(255)` | True |
| **requested_on** | `TIMESTAMP` | True |
| **timestamp** | `TIMESTAMP` | True |




### 🏷️ Categorical / Allowed Values:
- **`approval_status`** (2 values): `['Approved', 'Rejected']`
- **`note`** (7 values): `['', 'done', 'done hemant joshi mobile no phone pay', 'done lata di mobile no phone pay done', 'done pawan mobile no phone pay', 'ok', 'room rent done mobile no']`
- **`approved_by`** (1 values): `['Admin']`


### 🔍 Sample Data (First 3 rows):
| id | approval_no | subscription_no | approval_status | note | approved_by | requested_on | timestamp |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | APG-0001 | SUB-0013 | Approved | None | Admin | 2025-11-04 16:06:30+00:00 | 2025-11-04 18:02:30+00:00 |
| 2 | APG-0002 | SUB-0014 | Approved | None | Admin | 2025-11-04 16:09:00+00:00 | 2025-11-04 18:03:13+00:00 |
| 3 | APG-0003 | SUB-0014 | Approved | None | Admin | 2025-11-04 16:09:00+00:00 | 2025-11-04 18:05:09+00:00 |

---

## 📋 Table: `resume_request`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `BIGINT` | False |
| **candidate_name** | `VARCHAR(255)` | False |
| **candidate_email** | `VARCHAR(255)` | True |
| **candidate_mobile** | `VARCHAR(20)` | True |
| **applied_for_designation** | `VARCHAR(255)` | True |
| **req_id** | `VARCHAR(100)` | True |
| **experience** | `NUMERIC(4, 1)` | True |
| **previous_company** | `VARCHAR(255)` | True |
| **previous_salary** | `NUMERIC(12, 2)` | True |
| **reason_for_changing** | `TEXT` | True |
| **marital_status** | `VARCHAR(50)` | True |
| **reference** | `VARCHAR(255)` | True |
| **address_present** | `TEXT` | True |
| **resume** | `TEXT` | True |
| **interviewer_planned** | `TIMESTAMP` | True |
| **interviewer_actual** | `TIMESTAMP` | True |
| **interviewer_status** | `VARCHAR(100)` | True |
| **candidate_status** | `VARCHAR(50)` | True |
| **joined_status** | `VARCHAR(10)` | True |
| **created_at** | `TIMESTAMP` | True |
| **updated_at** | `TIMESTAMP` | True |




### 🏷️ Categorical / Allowed Values:
_No categorical columns detected_


### 🔍 Sample Data (First 3 rows):
_No data_

---

## 📋 Table: `collect_noc`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `BIGINT` | False |
| **serial_no** | `VARCHAR(50)` | False |
| **loan_name** | `VARCHAR(255)` | False |
| **bank_name** | `VARCHAR(255)` | False |
| **loan_start_date** | `DATE` | False |
| **loan_end_date** | `DATE` | False |
| **closure_request_date** | `DATE` | False |
| **collect_noc** | `BOOLEAN` | False |
| **created_at** | `TIMESTAMP` | True |




### 🏷️ Categorical / Allowed Values:
_No categorical columns detected_


### 🔍 Sample Data (First 3 rows):
_No data_

---

## 📋 Table: `subscription`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `INTEGER` | False |
| **timestamp** | `TIMESTAMP` | True |
| **subscription_no** | `VARCHAR(50)` | True |
| **company_name** | `VARCHAR(255)` | True |
| **subscriber_name** | `VARCHAR(255)` | True |
| **subscription_name** | `VARCHAR(255)` | True |
| **price** | `NUMERIC(12, 2)` | True |
| **frequency** | `VARCHAR(50)` | True |
| **purpose** | `TEXT` | True |
| **planned_1** | `DATE` | True |
| **actual_1** | `DATE` | True |
| **time_delay_1** | `INTERVAL` | True |
| **renewal_status** | `VARCHAR(50)` | True |
| **renewal_count** | `INTEGER` | True |
| **planned_2** | `DATE` | True |
| **actual_2** | `DATE` | True |
| **time_delay_2** | `INTERVAL` | True |
| **approval_status** | `VARCHAR(50)` | True |
| **planned_3** | `DATE` | True |
| **actual_3** | `DATE` | True |
| **time_delay_3** | `INTERVAL` | True |
| **start_date** | `DATE` | True |
| **end_date** | `DATE` | True |
| **document_copy** | `TEXT` | True |
| **updated_price** | `NUMERIC(12, 2)` | True |
| **created_at** | `TIMESTAMP` | True |
| **updated_at** | `TIMESTAMP` | True |
| **planned2_days** | `INTEGER` | True |
| **planned3_days** | `INTEGER` | True |
| **planned1_days** | `INTEGER` | True |
| **reason_for_renewal** | `VARCHAR` | True |




### 🏷️ Categorical / Allowed Values:
- **`company_name`** (6 values): `['Acme Corp', 'Alankar Alloys', 'Pankaj Ispat', 'Sourabh Rolling mill', 'Sourabh Rolling Mills', 'Sourabh Rolling MIlls']`
- **`subscriber_name`** (7 values): `['Amit Tiwari', 'audit', 'jyoti mishra room rent', 'lata chauhan', 'Priyanshu', 'Prrrriyanshu', 'sandeep']`
- **`frequency`** (4 values): `['Annually', 'Monthly', 'Quarterly', 'Yearly']`
- **`renewal_status`** (1 values): `['Approved']`
- **`approval_status`** (2 values): `['Approved', 'Rejected']`
- **`reason_for_renewal`** (1 values): `['Renewal purpose']`


### 🔍 Sample Data (First 3 rows):
| id | timestamp | subscription_no | company_name | subscriber_name | subscription_name | price | frequency | purpose | planned_1 | actual_1 | time_delay_1 | renewal_status | renewal_count | planned_2 | actual_2 | time_delay_2 | approval_status | planned_3 | actual_3 | time_delay_3 | start_date | end_date | document_copy | updated_price | created_at | updated_at | planned2_days | planned3_days | planned1_days | reason_for_renewal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 33 | 2025-12-08 09:16:11.165000+00:00 | SUB-0031 | Sourabh Rolling Mills | audit | Alpna Creation | 1420.00 | Annually | doman renewal :- sagartmt.com | 2026-12-06 | None | None | None | 0 | 2025-12-17 | 2025-12-08 | -1 day, 23:59:51 | Approved | 2025-12-17 | 2025-12-08 | -1 day, 23:59:51 | 2025-12-06 | 2026-12-06 | None | None | 2025-12-08 09:16:11.241576+00:00 | 2025-12-08 09:20:39.066444+00:00 | 7 | 7 | 7 | None |
| 3 | 2025-11-03 18:22:48+00:00 | SUB-0003 | Sourabh Rolling MIlls | audit | LIGHTHOUSE INFO SYSTEMS PVT. LTD | 363428.00 | Annually | Software Maintenance Charges @19% of Rs.16.21 Lacs | 2026-06-01 | None | None | None | None | 2025-11-12 | 2025-11-06 | -1 day, 23:59:54 | Approved | 2025-11-17 | 2025-11-07 | -1 day, 23:59:50 | 2025-06-01 | 2026-06-01 | None | None | 2025-12-05 07:32:11.514434+00:00 | 2025-12-05 07:32:11.514434+00:00 | 7 | 7 | 7 | None |
| 38 | 2026-02-03 05:17:58.427000+00:00 | SUB-0032 | Sourabh Rolling Mills | audit | Biomax HR Software Subscription | 2000.00 | Yearly | Database service for hr software valid till 20/03/ | None | None | None | None | 0 | 2026-02-12 | None | None | None | None | None | None | None | None | None | None | 2026-02-03 05:17:58.402530+00:00 | 2026-02-03 05:17:58.402530+00:00 | 7 | 7 | 7 | None |

---

## 📋 Table: `payment_history`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `INTEGER` | False |
| **subscription_no** | `VARCHAR(50)` | True |
| **payment_mode** | `VARCHAR(50)` | True |
| **transaction_id** | `VARCHAR(255)` | True |
| **start_date** | `DATE` | True |
| **insurance_document** | `TEXT` | True |
| **timestamp** | `TIMESTAMP` | True |




### 🏷️ Categorical / Allowed Values:
- **`payment_mode`** (3 values): `['Bank Transfer', 'Credit Card', 'UPI']`


### 🔍 Sample Data (First 3 rows):
| id | subscription_no | payment_mode | transaction_id | start_date | insurance_document | timestamp |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | SUB-0013 | UPI | 530702054215 | 2025-11-03 | https://drive.google.com/file/d/1zhpIOPEQPAEjhXbRh | 2025-11-05 16:35:23+00:00 |
| 2 | SUB-0014 | UPI | 739704644198 | 2025-11-03 | https://drive.google.com/file/d/1LkKbwTvvL-m9PEAa8 | 2025-11-05 16:41:19+00:00 |
| 3 | SUB-0015 | UPI | 99953361035 | 2025-11-03 | https://drive.google.com/file/d/1u68MN7Z16Xk7A7RES | 2025-11-05 17:40:58+00:00 |

---

## 📋 Table: `request_forclosure`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `BIGINT` | False |
| **serial_no** | `VARCHAR(50)` | False |
| **loan_name** | `VARCHAR(255)` | False |
| **bank_name** | `VARCHAR(255)` | False |
| **amount** | `NUMERIC(15, 2)` | False |
| **emi** | `NUMERIC(12, 2)` | False |
| **loan_start_date** | `DATE` | False |
| **loan_end_date** | `DATE` | False |
| **request_date** | `DATE` | False |
| **requester_name** | `VARCHAR(255)` | False |
| **created_at** | `TIMESTAMP` | True |




### 🏷️ Categorical / Allowed Values:
_No categorical columns detected_


### 🔍 Sample Data (First 3 rows):
_No data_

---

## 📋 Table: `sharedocuments`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `BIGINT` | False |
| **timestamp** | `TIMESTAMP` | False |
| **email** | `VARCHAR(255)` | False |
| **name** | `VARCHAR(255)` | True |
| **document_name** | `VARCHAR(255)` | True |
| **document_type** | `VARCHAR(100)` | True |
| **category** | `VARCHAR(100)` | True |
| **serial_no** | `VARCHAR(100)` | True |
| **image** | `TEXT` | True |
| **source_sheet** | `VARCHAR(255)` | True |
| **share_method** | `VARCHAR(100)` | True |
| **number** | `BIGINT` | True |




### 🏷️ Categorical / Allowed Values:
_No categorical columns detected_


### 🔍 Sample Data (First 3 rows):
_No data_

---

## 📋 Table: `subscription_renewals`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `INTEGER` | False |
| **renewal_no** | `VARCHAR(50)` | True |
| **subscription_no** | `VARCHAR(50)` | True |
| **renewal_status** | `VARCHAR(50)` | True |
| **approved_by** | `VARCHAR(255)` | True |
| **price** | `NUMERIC(12, 2)` | True |
| **timestamp** | `TIMESTAMP` | True |




### 🏷️ Categorical / Allowed Values:
- **`renewal_status`** (2 values): `['Approved', 'Renewed']`
- **`approved_by`** (3 values): `['Admin', 'Pintu Pandit', 'Shravan Nirmalkar']`


### 🔍 Sample Data (First 3 rows):
| id | renewal_no | subscription_no | renewal_status | approved_by | price | timestamp |
| --- | --- | --- | --- | --- | --- | --- |
| 6 | REN-0001 | SUB-0030 | Renewed | Admin | 123412.00 | 2025-11-21 17:40:46+00:00 |
| 7 | REN-0002 | SUB-0024 | Renewed | Shravan Nirmalkar | 1178.82 | 2025-11-25 09:36:24+00:00 |
| 8 | REN-0003 | SUB-0025 | Renewed | Admin | 1999.00 | 2025-12-03 17:46:29+00:00 |

---

## 📋 Table: `documents`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **document_id** | `BIGINT` | False |
| **created_at** | `TIMESTAMP` | True |
| **serial_no** | `BIGINT` | False |
| **document_name** | `TEXT` | False |
| **document_type** | `TEXT` | True |
| **category** | `TEXT` | True |
| **company_department** | `TEXT` | True |
| **tags** | `ARRAY` | True |
| **person_name** | `TEXT` | True |
| **need_renewal** | `VARCHAR(3)` | True |
| **renewal_date** | `DATE` | True |
| **image** | `TEXT` | True |
| **email** | `TEXT` | True |
| **mobile** | `VARCHAR(15)` | True |
| **is_deleted** | `BOOLEAN` | True |




### 🏷️ Categorical / Allowed Values:
- **`document_type`** (3 values): `['Certificate', 'Other', 'Report']`
- **`category`** (2 values): `['Company', 'Personal']`
- **`company_department`** (1 values): `['SOURABH ROLLING MILLS.PVT.LTD']`
- **`person_name`** (8 values): `['Alankar Alloys Private Limited', 'GAURI GANESH ISPAT PRIVATE LIMITED', 'PANKAJ AGRAWAL', 'PANKAJ ISPAT PRIVATE LTD.', 'Pintu Pandit', 'sourabh rolling mills', 'SOURABH ROLLING MILLS PVT LTD', 'SOURABH ROLLING MILLS.PVT.LTD']`
- **`need_renewal`** (2 values): `['yes', 'no']`
- **`is_deleted`** (1 values): `['False']`


### 🔍 Sample Data (First 3 rows):
| document_id | created_at | serial_no | document_name | document_type | category | company_department | tags | person_name | need_renewal | renewal_date | image | email | mobile | is_deleted |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2025-08-20 12:16:00 | 1 | Company Logo | Other | Company | None | None | SOURABH ROLLING MILLS PVT LTD | no | None | https://drive.google.com/uc?export=view&id=115cCoW | None | None | False |
| 2 | 2025-08-29 17:28:00 | 2 | PANCARD SOURABH | Other | Company | None | None | sourabh rolling mills | no | None | https://drive.google.com/uc?export=view&id=1qJUGR0 | None | None | False |
| 3 | 2025-08-29 17:28:00 | 3 | Gst certificate | Certificate | Company | None | None | sourabh rolling mills | no | None | https://drive.google.com/uc?export=view&id=1uClHt1 | None | None | False |

---

## 📋 Table: `payment_fms`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `UUID` | False |
| **unique_no** | `TEXT` | False |
| **fms_name** | `TEXT` | False |
| **pay_to** | `TEXT` | False |
| **amount** | `NUMERIC(12, 2)` | False |
| **remarks** | `TEXT` | True |
| **attachment** | `TEXT` | True |
| **created_at** | `TIMESTAMP` | True |
| **planned1** | `DATE` | True |
| **actual1** | `DATE` | True |
| **status** | `TEXT` | True |
| **stage_remarks** | `TEXT` | True |
| **planned2** | `DATE` | True |
| **actual2** | `DATE` | True |
| **payment_type** | `TEXT` | True |
| **planned3** | `DATE` | True |
| **actual3** | `DATE` | True |
| **delay1** | `INTERVAL` | True |
| **delay2** | `INTERVAL` | True |
| **delay3** | `INTERVAL` | True |




### 🏷️ Categorical / Allowed Values:
_No categorical columns detected_


### 🔍 Sample Data (First 3 rows):
_No data_

---

## 📋 Table: `subscription_master`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **company_name** | `TEXT` | False |
| **document_type** | `VARCHAR(255)` | True |
| **category** | `VARCHAR(255)` | True |
| **renewal_filter** | `BOOLEAN` | True |
| **id** | `BIGINT` | False |




### 🏷️ Categorical / Allowed Values:
- **`company_name`** (5 values): `['', 'Acme Corp', 'Alankar Alloys', 'Pankaj Ispat', 'Sourabh Rolling Mills']`
- **`document_type`** (9 values): `['Certificate', 'Contract', 'Invoice', 'Other', 'Praposal', 'Report', 'Resume', 'Service', 'Tax Document']`
- **`category`** (4 values): `['', 'Company', 'Director', 'Personal']`
- **`renewal_filter`** (1 values): `['False']`


### 🔍 Sample Data (First 3 rows):
| company_name | document_type | category | renewal_filter | id |
| --- | --- | --- | --- | --- |
| Sourabh Rolling Mills | None | None | None | 1 |
| Pankaj Ispat | None | None | None | 2 |
| Alankar Alloys | None | None | None | 3 |

---

## 📋 Table: `patching_checklist`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `INTEGER` | False |
| **check_date** | `DATE` | True |
| **furnace_number** | `VARCHAR(50)` | True |
| **crucible_number** | `VARCHAR(50)` | True |
| **rm_party_name** | `VARCHAR(150)` | True |
| **material_type** | `VARCHAR(100)` | True |
| **rm_bag_pic** | `TEXT` | True |
| **patching_start_time** | `TIMESTAMP` | True |
| **patching_end_time** | `TIMESTAMP` | True |
| **fc_breaking_check** | `BOOLEAN` | True |
| **lining_check** | `BOOLEAN` | True |
| **gld_check** | `BOOLEAN` | True |
| **premix_check** | `BOOLEAN` | True |
| **bottom_check** | `BOOLEAN` | True |
| **full_check** | `BOOLEAN` | True |
| **nali_top_dry_check** | `BOOLEAN` | True |
| **weight_check** | `BOOLEAN` | True |
| **proper_weight_per_check** | `BOOLEAN` | True |
| **mix_check** | `BOOLEAN` | True |
| **checked_by** | `VARCHAR(100)` | True |
| **pprm_party** | `VARCHAR(150)` | True |
| **p_patching_life** | `INTEGER` | True |
| **created_at** | `TIMESTAMP` | True |
| **unique_code** | `TEXT` | True |




### 🏷️ Categorical / Allowed Values:
- **`furnace_number`** (3 values): `['F1', 'F2', 'Furnace 3']`
- **`crucible_number`** (2 values): `['1', 'A']`
- **`rm_party_name`** (3 values): `['RK Minerals', 'RKPL', 'S&B']`
- **`material_type`** (2 values): `['Non Premix', 'Premix']`
- **`rm_bag_pic`** (3 values): `['http://localhost:3004/uploads/patching-checklist-pictures/whatsappimage20260220at1342411-1771930850859-345581788.jpeg', 'https://batchcode.sagartmt.com//uploads/patching-checklist-pictures/whatsappimage20260220at134241-1772011527282-664857408.jpeg', 'https://batchcode.sagartmt.com/uploads/patching-checklist-pictures/whatsappimage20260220at134242-1772022688651-191398859.jpeg']`
- **`fc_breaking_check`** (2 values): `['False', 'True']`
- **`lining_check`** (2 values): `['False', 'True']`
- **`gld_check`** (2 values): `['False', 'True']`
- **`premix_check`** (2 values): `['False', 'True']`
- **`bottom_check`** (1 values): `['False']`
- **`full_check`** (2 values): `['False', 'True']`
- **`nali_top_dry_check`** (2 values): `['False', 'True']`
- **`weight_check`** (2 values): `['False', 'True']`
- **`proper_weight_per_check`** (2 values): `['False', 'True']`
- **`mix_check`** (2 values): `['False', 'True']`
- **`checked_by`** (2 values): `['sdfs', 'sdfsdf']`
- **`pprm_party`** (1 values): `['sdfsd']`
- **`unique_code`** (3 values): `['PC-6FSD', 'PC-VUPE', 'PC-WA4P']`


### 🔍 Sample Data (First 3 rows):
| id | check_date | furnace_number | crucible_number | rm_party_name | material_type | rm_bag_pic | patching_start_time | patching_end_time | fc_breaking_check | lining_check | gld_check | premix_check | bottom_check | full_check | nali_top_dry_check | weight_check | proper_weight_per_check | mix_check | checked_by | pprm_party | p_patching_life | created_at | unique_code |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | 2026-02-24 | Furnace 3 | A | RK Minerals | Non Premix | http://localhost:3004/uploads/patching-checklist-p | 2026-02-24 16:30:00 | 2026-02-24 19:30:00 | False | False | False | False | False | False | False | False | False | False | sdfsdf | sdfsd | 423 | 2026-02-24 11:00:50.786994 | PC-WA4P |
| 4 | 2026-02-25 | F1 | 1 | RKPL | Premix | https://batchcode.sagartmt.com//uploads/patching-c | 2026-02-25 14:54:00 | 2026-02-25 15:54:00 | True | True | False | True | False | False | True | True | True | True | sdfs | sdfsd | 3 | 2026-02-25 09:25:27.352269 | PC-6FSD |
| 5 | 2026-02-25 | F2 | 1 | S&B | Premix | https://batchcode.sagartmt.com/uploads/patching-ch | 2026-02-25 18:00:00 | 2026-02-25 18:01:00 | True | True | True | False | False | True | False | False | False | True | sdfsdf | sdfsd | 3 | 2026-02-25 12:31:28.712272 | PC-VUPE |

---

## 📋 Table: `tundish_checklist`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `BIGINT` | False |
| **sample_timestamp** | `TIMESTAMP` | True |
| **tundish_number** | `VARCHAR(20)` | False |
| **nozzle_plate_check** | `TEXT` | True |
| **well_block_check** | `TEXT` | True |
| **board_proper_set** | `TEXT` | True |
| **board_sand_filling** | `TEXT` | True |
| **refractory_slag_cleaning** | `TEXT` | True |
| **tundish_mession_name** | `VARCHAR(100)` | True |
| **handover_proper_check** | `TEXT` | True |
| **handover_nozzle_installed** | `TEXT` | True |
| **handover_masala_inserted** | `TEXT` | True |
| **stand1_mould_operator** | `VARCHAR(100)` | True |
| **stand2_mould_operator** | `VARCHAR(100)` | True |
| **timber_man_name** | `VARCHAR(100)` | True |
| **laddle_operator_name** | `VARCHAR(100)` | True |
| **shift_incharge_name** | `VARCHAR(100)` | True |
| **forman_name** | `VARCHAR(100)` | True |
| **remarks** | `TEXT` | True |
| **unique_code** | `VARCHAR(50)` | False |
| **created_at** | `TIMESTAMP` | True |




### 🏷️ Categorical / Allowed Values:
- **`tundish_number`** (1 values): `['1']`
- **`nozzle_plate_check`** (2 values): `['Done', 'Not Done']`
- **`well_block_check`** (2 values): `['Done', 'Not Done']`
- **`board_proper_set`** (2 values): `['Done', 'Not Done']`
- **`board_sand_filling`** (2 values): `['Done', 'Not Done']`
- **`refractory_slag_cleaning`** (1 values): `['Done']`
- **`tundish_mession_name`** (3 values): `['dfg', 'sdf', 'sdfsd']`
- **`handover_proper_check`** (1 values): `['Yes']`
- **`handover_nozzle_installed`** (1 values): `['Yes']`
- **`handover_masala_inserted`** (1 values): `['Yes']`
- **`stand1_mould_operator`** (2 values): `['dfg', 'sdfsd']`
- **`stand2_mould_operator`** (3 values): `['dfg', 'sdf', 'sdfs']`
- **`timber_man_name`** (2 values): `['dfg', 'sdf']`
- **`laddle_operator_name`** (3 values): `['dfg', 'sdf', 'sdfs']`
- **`shift_incharge_name`** (3 values): `['dfg', 'sdf', 'sdfsdf']`
- **`forman_name`** (3 values): `['dfg', 'sdf', 'sdfsdf']`
- **`unique_code`** (3 values): `['T-BPN6', 'T-NWAW', 'T-ZGFK']`


### 🔍 Sample Data (First 3 rows):
| id | sample_timestamp | tundish_number | nozzle_plate_check | well_block_check | board_proper_set | board_sand_filling | refractory_slag_cleaning | tundish_mession_name | handover_proper_check | handover_nozzle_installed | handover_masala_inserted | stand1_mould_operator | stand2_mould_operator | timber_man_name | laddle_operator_name | shift_incharge_name | forman_name | remarks | unique_code | created_at |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2026-02-24 10:58:24.906000 | 1 | Done | Done | Done | Done | Done | sdf | Yes | Yes | Yes | sdfsd | sdf | sdf | sdfs | sdfsdf | sdfsdf | None | T-NWAW | 2026-02-24 10:58:25.284288 |
| 2 | 2026-02-25 11:12:00 | 1 | Done | Done | Done | Done | Done | dfg | Yes | Yes | Yes | dfg | dfg | dfg | dfg | dfg | dfg | None | T-ZGFK | 2026-02-25 11:12:55.567902 |
| 3 | 2026-02-25 18:01:00 | 1 | Not Done | Not Done | Not Done | Not Done | Done | sdfsd | Yes | Yes | Yes | sdfsd | sdfs | sdf | sdf | sdf | sdf | None | T-BPN6 | 2026-02-25 12:32:02.456586 |

---
