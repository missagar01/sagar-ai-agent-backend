# 🗄️ Schema Report: Checklist & Delegation System
**Generated:** 2026-02-04 12:39

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




### 🏷️ Categorical / Allowed Values:
- **`frequency`** (1 values): `['one-time']`
- **`remarks`** (12 values): `['', 'done', 'Done', 'Done', 'follow up by ramesh bhaiya', 'not possible without bank api', 'ok', 'Work Completed', 'Work Completed', 'Work Done', 'work Done and training start', 'Working']`
- **`given_by`** (12 values): `['AAKASH AGRAWAL', 'AK GUPTA', 'ANUP KUMAR BOPCHE', 'DANVEER SINGH', 'DEEPAK BHALLA', 'RAJNISH BHARDWAJ', 'Rinku Gautam', 'RINKU SINGH', 'SANDEEP DUBEY', 'SHAILESH CHITRE', 'SHEELESH MARELE', 'Shree Ram Patle']`
- **`enable_reminder`** (1 values): `['yes']`
- **`require_attachment`** (2 values): `['no', 'yes']`
- **`status`** (3 values): `['done', 'Done', 'extend']`


### 🔍 Sample Data (First 3 rows):
| task_id | created_at | department | name | task_description | frequency | remarks | task_start_date | given_by | image | enable_reminder | require_attachment | status | updated_at | planned_date | submission_date | color_code_for | delay |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 19 | 2025-08-19 11:37:00 | ADMIN | Sandeep Kumar Dubey | ajit gupta gm sir meeting today 4.30 | one-time | None | 2025-08-19 16:02:00 | AAKASH AGRAWAL | None | yes | no | Done | None | 2025-08-19 16:02:00 | 2025-08-21 00:00:00 | 1 | 1 day, 7:58:00 |
| 20 | 2025-08-19 11:42:00 | ADMIN | Sandeep Kumar Dubey | akash bhaiya time 3.30 pm | one-time | None | 2025-08-22 15:25:00 | AAKASH AGRAWAL | None | yes | no | Done | None | 2025-08-22 15:25:00 | 2025-08-21 00:00:00 | 1 | -2 days, 8:35:00 |
| 21 | 2025-08-19 11:45:00 | ADMIN | Sandeep Kumar Dubey | ashish sir meeting 3.30 pm today | one-time | None | 2025-08-19 15:26:00 | AAKASH AGRAWAL | None | yes | no | Done | None | 2025-08-19 15:26:00 | 2025-08-21 00:00:00 | 1 | 1 day, 8:34:00 |

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
- **`reason`** (19 values): `['', 'asdf', 'asdfgh', 'asdfsadf', 'done', 'Done', 'Done', 'fghjkl', 'follow up by ramesh bhaiya', 'have another work', 'mnvhj', 'not possible without bank api', 'ok', 'task_complete', 'Work Completed', 'Work Completed', 'Work Done', 'work Done and training start', 'Working']`
- **`given_by`** (16 values): `['AAKASH AGRAWAL', 'AK GUPTA', 'ANUP KUMAR BOPCHE', 'ccvgdff', 'DANVEER SINGH', 'DEEPAK BHALLA', 'DM', 'MD Sir', 'nchf', 'RAJNISH BHARDWAJ', 'Rinku Gautam', 'RINKU SINGH', 'SANDEEP DUBEY', 'SHAILESH CHITRE', 'SHEELESH MARELE', 'Shree Ram Patle']`


### 🔍 Sample Data (First 3 rows):
| task_id | created_at | status | next_extend_date | reason | image_url | name | task_description | given_by | id |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 51 | 2025-09-22 12:18:27.685699+00:00 | done | None | None | None | Dinesh Kumar Bandhe | Maintenance module तैयार हो चुका है, कृपया यूज़र्स | AAKASH AGRAWAL | 04daf1ef-6000-4c51-868b-7d8ab75a3c90 |
| 64 | 2025-09-19 04:21:00.965202+00:00 | done | None | None | None | admin | Boundry rounding  | Rinku Gautam | 07db9bf4-dfd8-49fc-986c-1d56e5bf62d1 |
| 44 | 2025-09-19 04:01:56.317176+00:00 | extend | 2025-09-27 00:00:00 | None | None | admin | Maintenance module तैयार हो चुका है, कृपया यूज़र्स | AAKASH AGRAWAL | 082eb679-6071-40b3-96d8-9eaa75f97351 |

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




### 🏷️ Categorical / Allowed Values:
- **`enable_reminder`** (2 values): `['yes', 'no']`
- **`require_attachment`** (2 values): `['yes', 'no']`
- **`frequency`** (14 values): `['daily', 'Daily', 'F', 'fortnightly', 'monthly', 'Monthly', 'one time', 'one-time', 'quarterly', 'W', 'weekly', 'Weekly', 'Y', 'yearly']`
- **`status`** (4 values): `['no', 'No', 'yes', 'Yes']`
- **`admin_done`** (4 values): `['confirmed', 'Confirmed', 'Done', 'No']`
- **`user_status_checklist`** (5 values): `['no', 'No', 'Pending', 'yes', 'Yes']`


### 🔍 Sample Data (First 3 rows):
| task_id | department | given_by | name | task_description | enable_reminder | require_attachment | frequency | remark | status | image | admin_done | delay | planned_date | created_at | task_start_date | submission_date | user_status_checklist |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3009301 | PC | AK GUPTA | Vishal Pandey | Ramesh work fallow up  | yes | no | daily | None | None | None | None | None | 2026-05-29T09:00:00 | 2025-12-19 14:33:27.527684 | 2026-05-29 09:00:00 | None | None |
| 3009302 | PC | AK GUPTA | Vishal Pandey | Ramesh work fallow up  | yes | no | daily | None | None | None | None | None | 2026-05-30T09:00:00 | 2025-12-19 14:33:27.527684 | 2026-05-30 09:00:00 | None | None |
| 3009303 | PC | AK GUPTA | Vishal Pandey | Ramesh work fallow up  | yes | no | daily | None | None | None | None | None | 2026-05-31T09:00:00 | 2025-12-19 14:33:27.527684 | 2026-05-31 09:00:00 | None | None |

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
| **subscription_access_system** | `TEXT` | True |
| **user_access1** | `TEXT` | True |
| **store_access** | `TEXT` | True |
| **emp_image** | `TEXT` | True |
| **verify_access** | `VARCHAR(20)` | True |
| **verify_access_dept** | `TEXT` | True |




### 🏷️ Categorical / Allowed Values:
- **`given_by`** (21 values): `['', 'AAKASH AGRAWAL', 'AK GUPTA', 'ANIL KUMAR MISHRA', 'ANUP KUMAR BOPCHE', 'DEEPAK BHALLA', 'G RAM MOHAN RAO', 'GUNJAN TIWARI', 'HULLAS PASWAN', 'MANTU ANAND GHOSE', 'MRIGENDRA NARAYAN BEPARI', 'MUKESH PATLE', 'RAJNISH BHARDWAJ', 'RAVI KUMAR SINGH', 'RINKU GAUTAM', 'RINKU SINGH', 'ROSHAN RAJAK', 'SANDEEP DUBEY', 'SHAILESH CHITRE', 'SHEELESH MARELE', 'SUMAN JHA']`
- **`role`** (2 values): `['admin', 'user']`
- **`status`** (1 values): `['active']`
- **`remark`** (1 values): `['']`
- **`last_punch_device`** (2 values): `['E03C1CB34D83AA02', 'E03C1CB36042AA02']`
- **`page_access`** (23 values): `['', 'all-task', 'all-task,assign-task', 'all-task,dashboard', 'assign-task,all-task,dashboard', 'dashboard,all-task', 'dashboard,all-task,assign-task', 'dashboard,all-task,delegation', 'dashboard,all-task,machines', 'dashboard,assign-task,all-task', 'dashboard,assign-task,delegation,all-task', 'dashboard,assign-task,delegation,all-task', 'dashboard,assign-task,delegation,all-task,hrmanager', 'dashboard,assign-task,delegation,all-task,hrmanager', 'dashboard,assign-task,delegation,all-task,hrmanager,machines', 'dashboard,assign-task,delegation,all-task,setting', 'dashboard,assign-task,delegation,all-task,task-verification', 'dashboard,delegation,all-task', 'dashboard,delegation,all-task,assign-task,hrmanager', 'dashboard,delegation,all-task,hrmanager', 'dashboard,machines,assign-task,delegation,all-task,hrmanager', 'dashboard,quick-task,machines,assign-task,delegation,all-task,mis-report,setting,hrmanager', 'delegation,all-task,dashboard,hrmanager']`
- **`system_access`** (23 values): `['Checklist', 'CHECKLIST', 'CHECKLIST COMBINED,STORE AND PURCHASE,SALES MODULE,ALL PAYMENT SYSTEM,HRMS,VISITOR GATE PASS', 'CHECKLIST,HOUSEKEEPING,MAINTENANCE,STORE AND PURCHASE,HRMS', 'CHECKLIST,HOUSEKEEPING,STORE AND PURCHASE,HRMS', 'Checklist,Maintenance', 'CHECKLIST,MAINTENANCE', 'CHECKLIST,MAINTENANCE,HOUSEKEEPING,CHECKLIST,HOUSEKEEPING,STORE AND PURCHASE,HRMS', 'CHECKLIST,MAINTENANCE,HOUSEKEEPING,HOUSEKEEPING,MAINTENANCE,CHECKLIST,STORE AND PURCHASE,HRMS', 'CHECKLIST,MAINTENANCE,HOUSEKEEPING,STORE AND PURCHASE,HRMS', 'CHECKLIST,MAINTENANCE,HOUSEKEEPING,STORE AND PURCHASE,SALES MODULE,ALL PAYMENT SYSTEM,HRMS,LOGISTIC', 'CHECKLIST,MAINTENANCE,STORE AND PURCHASE,HRMS', 'CHECKLIST,MAINTENANCE,STORE AND PURCHASE,HRMS,ALL PAYMENT SYSTEM', 'CHECKLIST,MAINTENANCE,STORE AND PURCHASE,HRMS,HOUSEKEEPING', 'CHECKLIST,MAINTENANCE,STORE AND PURCHASE,HRMS,HOUSEKEEPING,Housekeeping,Maintenance,Checklist', 'CHECKLIST,MAINTENANCE,STORE AND PURCHASE,HRMS,Housekeeping,Maintenance,Checklist', 'CHECKLIST,MAINTENANCE,STORE AND PURCHASE,HRMS,SALES MODULE', 'CHECKLIST,SALES MODULE,STORE AND PURCHASE,HRMS', 'CHECKLIST,STORE AND PURCHASE,HRMS', 'CHECKLIST,STORE AND PURCHASE,HRMS,VISITOR GATE PASS', 'HOUSEKEEPING,MAINTENANCE,CHECKLIST', 'MAINTENANCE,CHECKLIST', 'MAINTENANCE,HOUSEKEEPING,CHECKLIST,STORE AND PURCHASE,SALES MODULE,HRMS']`
- **`subscription_access_system`** (4 values): `['{"systems":["subscription","document"],"pages":["Dashboard","Subscription"]}', '{"systems":["subscription","document"],"pages":["Dashboard","Subscription/Approval","Subscription/Renewal","Subscription/All","Subscription/Payment","Document/All","Document/Renewal","Document/Shared","Resource Manager"]}', '{"systems":["subscription","document","payment"],"pages":["Dashboard","Subscription/Renewal","Subscription/All","Subscription/Payment","Document/All","Document/Renewal","Document/Shared","Resource Manager","Payment/Request Form","Payment/Make Payment","Payment/Tally Entry"]}', '{"systems":["subscription","payment"],"pages":["Subscription/Approval"]}']`
- **`user_access1`** (17 values): `['', 'Admin Office - First Floor, Admin Office - Ground Floor, Back Office, Cabins ग्राउंड फ्लोर: and first floor, Canteen Area 1 & 2, Car Parking Area, CCM, CCM Office, CCM Panel Room, CCM PLC Panel Room, CCM SBO Panel Room, Container Office, Labour Colony & Bathroom, Main Gate, Main Gate Front Area, Mandir, New Lab, Patra Mill AC Panel Room, Patra Mill DC Panel Room, Patra Mill Foreman Office, Patra Mill Pump Room, Patra Mill SBO Panel, Pipe Mill, Plant Area, SMS Electrical Room, SMS Maintenance Off', 'Admin Office - First Floor, Admin Office - Ground Floor, Back Office, Cabins ग्राउंड फ्लोर: and first floor, Canteen Area 1 & 2, Car Parking Area, CCM, CCM Office, CCM Panel Room, CCM PLC Panel Room, CCM SBO Panel Room, Container Office, Labour Colony & Bathroom, Main Gate, Main Gate Front Area, Mandir, New Lab, Patra Mill AC Panel Room, Patra Mill DC Panel Room, Patra Mill Foreman Office, Patra Mill Pump Room, Patra Mill SBO Panel, Pipe Mill, Plant Area, SMS Electrical Room, SMS Maintenance Office, SMS Office, SMS Panel Room, Store Office, Weight Office & Kata In/Out, Workshop', 'Admin Office - First Floor, Admin Office - Ground Floor, Car Parking Area', 'Back Office, Container Office', 'Canteen Area 1 & 2, Labour Colony & Bathroom, Main Gate, Main Gate Front Area, Mandir, Plant Area', 'Canteen Area 1 & 2, Labour Colony, Main Gate, Main Gate Front Area, Mandir, Plant Area', 'CCM PLC Panel Room, CCM SBO Panel Room', 'New Lab', 'Patra Mill AC Panel Room, Patra Mill DC Panel Room', 'Patra Mill SBO Panel', 'Pipe Mill', 'SMS Electrical Store Room, SMS Office', 'SMS Panel Room, SMS Electrical Store Room', 'Store Office', 'Weight Office & Kata In/Out', 'Workshop']`
- **`store_access`** (6 values): `['APPROVE INDENT DATA', 'INDENT,PURCHASE ORDER,INVENTORY,REPAIR GATE PASS,REPAIR FOLLOW UP', 'PURCHASE ORDER', 'STORE GRN', 'STORE GRN ADMIN APPROVAL', 'STORE GRN CLOSE']`
- **`verify_access`** (2 values): `['hod', 'manager']`
- **`verify_access_dept`** (24 values): `['ADMIN,ACCOUNTS,AUTOMATION,CCM,CCM ELECTRICAL,CONTRACTORS AJAY GIRI PIPE REPAIRING,CONTRACTORS BIRENDRA SALATING,CONTRACTORS CHANDU TIWARI PIPE MILL,CONTRACTORS CHANDU TIWARI RECOILER,CONTRACTORS GUDDU KR YADAV PIPE REPAIRING,CONTRACTORS MUMTAZ RECOILER & SALATING,CONTRACTORS MUMTAZ RECOILER AND SALATING,CONTRACTORS NAWIK LAB,CONTRACTORS PREM BHARTI PIPE MILL,CONTRACTORS ROHIT MISHRA MILL SAFAI,CONTRACTORS SHIVAM TIWARI PIPE MILL,CONTRACTORS SONU SALATING,CONTRACTORS VIKASH KUMAR PIPE MILL,CRM,CRUSHER,DISPATCH,HR,INWARD,MARKETING,LAB AND QUALITY CONTROL,PC,PIPE MILL ELECTRICAL,PIPE MILL MAINTENANCE,PIPE MILL PRODUCTION,PROJECT,PURCHASE,SECURITY,SMS ELECTRICAL,SMS MAINTENANCE,SMS PRODUCTION,STORE,STRIP MILL ELECTRICAL,STRIP MILL MAINTENANCE,STRIP MILL PRODUCTION,TRANSPORT,WB,WORKSHOP', 'ADMIN,AUTOMATION,ACCOUNTS,DISPATCH,HR,INWARD,PURCHASE,SECURITY,STORE,WB,PC', 'CCM', 'CCM ELECTRICAL,STRIP MILL ELECTRICAL', 'CCM,PROJECT,CCM ELECTRICAL,SMS ELECTRICAL,SMS MAINTENANCE,SMS PRODUCTION', 'CONTRACTORS BIRENDRA SALATING,CONTRACTORS CHANDU TIWARI RECOILER,CONTRACTORS ROHIT MISHRA MILL SAFAI', 'CONTRACTORS MUMTAZ RECOILER AND SALATING,CONTRACTORS SONU SALATING', 'CRM,MARKETING', 'CRM,MARKETING,LAB AND QUALITY CONTROL,PIPE MILL ELECTRICAL,PIPE MILL MAINTENANCE,PIPE MILL PRODUCTION,PC,TRANSPORT,SECURITY,DISPATCH,INWARD', 'DISPATCH,INWARD', 'LAB AND QUALITY CONTROL', 'PC', 'PIPE MILL ELECTRICAL', 'PIPE MILL MAINTENANCE', 'PIPE MILL PRODUCTION', 'PROJECT', 'SECURITY', 'SMS ELECTRICAL', 'SMS MAINTENANCE', 'SMS PRODUCTION', 'STRIP MILL ELECTRICAL,STRIP MILL MAINTENANCE,STRIP MILL PRODUCTION,WORKSHOP', 'STRIP MILL MAINTENANCE', 'TRANSPORT', 'WORKSHOP']`


### 🔍 Sample Data (First 3 rows):
| id | created_at | user_name | password | email_id | number | department | given_by | role | status | user_access | leave_date | remark | leave_end_date | employee_id | last_punch_time | last_punch_device | page_access | system_access | subscription_access_system | user_access1 | store_access | emp_image | verify_access | verify_access_dept |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 767 | 2026-01-18 05:39:28.544410+00:00 | Shrikant Yadav | 9669 | shrikantyadav@gmail.com | 9875136297 | PIPE MILL MAINTENANCE | None | user | active | PIPE MILL MAINTENANCE | None | None | None | S09669 | None | None | dashboard,all-task | Checklist | None | None | None | None | None | None |
| 814 | 2026-01-25 05:03:57.943824+00:00 | Anand Kumar Kushwaha | 1234 | anandkumar123@gmail.com | 9109314548 | PIPE MILL ELECTRICAL | None | user | active | PIPE MILL ELECTRICAL | None | None | None | S9248 | None | None | dashboard,all-task | CHECKLIST | None | None | None | None | None | None |
| 768 | 2026-01-18 06:51:58.841718+00:00 | Ravi Patle | 123 | ss3552630@gmail.com | None | PIPE MILL MAINTENANCE | None | user | active | PIPE MILL MAINTENANCE | None | None | None | None | None | None | all-task,assign-task | Checklist | None | None | None | https://emp-profiles-dashboard.s3.amazonaws.com/em | None | None |

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

## 📋 Table: `users_staging`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `BIGINT` | True |
| **created_at** | `TIMESTAMP` | True |
| **user_name** | `TEXT` | True |
| **password** | `TEXT` | True |
| **email_id** | `TEXT` | True |
| **number** | `BIGINT` | True |
| **department** | `TEXT` | True |
| **given_by** | `TEXT` | True |
| **role** | `TEXT` | True |
| **status** | `TEXT` | True |
| **user_access** | `TEXT` | True |
| **leave_date** | `TIMESTAMP` | True |
| **remark** | `TEXT` | True |
| **leave_end_date** | `TIMESTAMP` | True |
| **employee_id** | `TEXT` | True |




### 🏷️ Categorical / Allowed Values:
- **`given_by`** (22 values): `['AAKASH AGRAWAL', 'AK GUPTA', 'ANIL KUMAR MISHRA', 'ANUP KUMAR BOPCHE', 'DANVEER SINGH', 'DEEPAK BHALLA', 'Dhanji', 'G RAM MOHAN RAO', 'GUNJAN TIWARI', 'HULLAS PASWAN', 'MANTU ANAND GHOSE', 'MRIGENDRA NARAYAN BEPARI', 'RAJNISH BHARDWAJ', 'RINKU GAUTAM', 'RINKU SINGH', 'ROSHAN RAJAK', 'SACHIN SAXENA', 'SANDEEP DUBEY', 'SHAILESH CHITRE', 'SHEELESH MARELE', 'Shree Ram Patle', 'SUMAN JHA']`
- **`role`** (2 values): `['admin', 'user']`
- **`status`** (2 values): `['active', 'inactive']`


### 🔍 Sample Data (First 3 rows):
| id | created_at | user_name | password | email_id | number | department | given_by | role | status | user_access | leave_date | remark | leave_end_date | employee_id |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | 2025-08-28 06:00:35.902673+00:00 | admin | admin1234 | abc@gmail.com | 123 | None | AAKASH AGRAWAL | admin | active | ACCOUNTS,ADMIN,CCM,CCM ELECTRICAL,CRM,CRUSHER,DISP | None | None | None | None |
| 4 | 2025-08-28 06:00:35.902673+00:00 | SKNayak | user1 | None | 6266919120 | ACCOUNTS | SHEELESH MARELE | user | active | ACCOUNTS | None | None | None | S02990 |
| 5 | 2025-08-28 06:00:35.902673+00:00 | Shravan Nirmalkar | user2 | pc@sagartmt.com | 9329149381 | PC | RINKU SINGH | user | active | PC | None | None | None | S08362 |

---

## 📋 Table: `systems`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `INTEGER` | False |
| **systems** | `VARCHAR(255)` | False |
| **link** | `TEXT` | True |




### 🏷️ Categorical / Allowed Values:
- **`systems`** (7 values): `['CHECKLIST COMBINED', 'HRMS', 'LOGISTIC', 'SALES MODULE', 'STORE AND PURCHASE', 'SUBSCRIPTION', 'VISITOR GATE PASS']`
- **`link`** (7 values): `['https://checklist-frontend-aws.vercel.app/', 'https://doc-sub-frontend.vercel.app', 'https://gate-pass-srmpl.vercel.app/dashboard/quick-task', 'https://hr.sagargroup.co/', 'https://new-store-repair-frontend.vercel.app/', 'https://o2d-lead-batchcode-frontend-aws.vercel.app/login', 'https://triofleet.trieon.in/']`


### 🔍 Sample Data (First 3 rows):
| id | systems | link |
| --- | --- | --- |
| 4 | SALES MODULE | https://o2d-lead-batchcode-frontend-aws.vercel.app |
| 15 | LOGISTIC | https://triofleet.trieon.in/ |
| 1 | CHECKLIST COMBINED | https://checklist-frontend-aws.vercel.app/ |

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

## 📋 Table: `departments`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `INTEGER` | False |
| **department** | `VARCHAR(100)` | False |




### 🏷️ Categorical / Allowed Values:
_No categorical columns detected_


### 🔍 Sample Data (First 3 rows):
| id | department |
| --- | --- |
| 1 | ACCOUNTS |
| 2 | ADMIN |
| 3 | AUTOMATION |

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
- **`approval_status`** (2 values): `['approved', 'pending']`
- **`approved_by`** (13 values): `['Deepak Bhalla', 'Hem Kumar Jagat', 'K Ramesh Kumar', 'Mukesh Patle', 'Pawan Kumar Parganiha', 'Rahul Sharma', 'Rinku Singh', 'Sandeep Kumar Dubey', 'Saroj Kumar Choudhary', 'Shailesh Chitre', 'Sheelesh Marele', 'Sheetal Patel', 'Shivraj Sharma']`
- **`status`** (2 values): `['IN', 'OUT']`
- **`gate_pass_closed`** (2 values): `['False', 'True']`


### 🔍 Sample Data (First 3 rows):
| id | visitor_name | mobile_number | visitor_photo | visitor_address | purpose_of_visit | person_to_meet | date_of_visit | time_of_entry | visitor_out_time | approval_status | approved_by | approved_at | status | gate_pass_closed | created_at |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 302 | Durgesh  | 9827492062 | None | Shiv om refrigeration  | Ac repairing  | Sandeep Kumar Dubey | 2026-01-28 | 12:23:00 | 13:05:14.791079 | approved | Sandeep Kumar Dubey | 2026-01-28 07:05:56.916325 | OUT | True | 2026-01-28 06:55:08.991007 |
| 296 | M Maity  | 7566098396 | https://srmpl-visitor-gatepass.s3.amazonaws.com/vi | Metaflux bhilai | Official  | Saroj Kumar Choudhary | 2026-01-26 | 12:17:00 | 13:38:53.156284 | approved | Saroj Kumar Choudhary | 2026-01-28 08:07:42.420309 | OUT | True | 2026-01-26 06:48:44.428295 |
| 308 | Hem Kumar | 7723020093 | None | Flat 302, Shanti Apartments, MG Road, Pune | testing by developer | Amit Tiwari | 2026-01-28 | 10:30:00 | None | pending | None | None | IN | False | 2026-01-28 10:07:56.692281 |

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
| 1 | Aakash Agrawal | 9329149382 | 2026-01-13 06:43:37.496570 |
| 2 | Sheelesh Marele | 8839494655 | 2026-01-13 06:43:37.496570 |
| 3 | Ajit Kumar Gupta | 9584556480 | 2026-01-13 06:43:37.496570 |

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




### 🏷️ Categorical / Allowed Values:
- **`form_type`** (2 values): `['INDENT', 'REQUISITION']`
- **`request_number`** (6 values): `['IND01', 'IND02', 'IND03', 'IND04', 'IND05', 'REQ01']`
- **`indent_series`** (4 values): `['I1', 'I5', 'R1', 'R4']`
- **`requester_name`** (2 values): `['Hem Kumar Jagat', 'Shravan Nirmalkar']`
- **`department`** (2 values): `['AUTOMATION', 'PC']`
- **`division`** (3 values): `['CO', 'PM', 'SM']`
- **`item_code`** (6 values): `['F05010018', 'S01020002', 'S01060008', 'S01070009', 'S01070014', 'S01160007']`
- **`product_name`** (6 values): `['ABSORPTION VESSEL FOR C&C APPARATUS', 'BEARING V22.40.006.0', 'CYL DIA 50 M/C TS02/03-TS', 'KEYBOARD', 'MOUSE PAD', 'SILICOMANGANESE']`
- **`uom`** (5 values): `['LTR', 'MT', 'MTR', 'NOS', 'SET']`
- **`specification`** (6 values): `['', 'asdfsdfsd', 'CDP model with digital board', 'qawsedf', 'sdsfsdf', 'WIRE LESS USB 3.0']`
- **`make`** (7 values): `['121', '20', 'Dell', 'dgfdg', 'HP', 'logitech', 'LOGITECH']`
- **`purpose`** (6 values): `['', 'edrftgyhuji', 'FOR DEVELOPER', 'sdfsdfsdf', 'sdfsdfsdfsdfsdfsd', 'USE FOR OFFICE']`
- **`cost_location`** (4 values): `['ADMINISTRATION OFFICE', 'CENTRAL WORKSHOP', 'CIVIL WORK', 'GENERAL/COMMON']`
- **`time_delay_1`** (5 values): `['00:00:26.511', '00:00:26.512', '00:00:44.197', '00:01:52.098', '00:04:21.3']`
- **`request_status`** (2 values): `['APPROVED', 'PENDING']`
- **`group_name`** (4 values): `['AUTOMOBILE', 'BY PRODUCTS', 'COMPRESSOR SPARES', 'COMPUTER']`
- **`indent_number`** (3 values): `['srm0002', 'srm001', 'srm004']`


### 🔍 Sample Data (First 3 rows):
| id | sample_timestamp | form_type | request_number | indent_series | requester_name | department | division | item_code | product_name | request_qty | uom | specification | make | purpose | cost_location | planned_1 | actual_1 | time_delay_1 | request_status | approved_quantity | created_at | updated_at | group_name | indent_number |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3 | 2026-01-16 10:07:38.085000+00:00 | INDENT | IND03 | I1 | Hem Kumar Jagat | AUTOMATION | SM | F05010018 | SILICOMANGANESE | 12 | MT | sdsfsdf | 121 | sdfsdfsdf | CENTRAL WORKSHOP | 2026-01-16 10:07:38.085000+00:00 | 2026-01-16 10:08:04.596000+00:00 | 00:00:26.511 | APPROVED | 123 | 2026-01-16 10:07:38.935000+00:00 | 2026-01-16 10:08:04.595533+00:00 | BY PRODUCTS | None |
| 4 | 2026-01-16 10:07:38.087000+00:00 | INDENT | IND03 | I1 | Hem Kumar Jagat | AUTOMATION | SM | S01020002 | BEARING V22.40.006.0 | 3 | MTR | asdfsdfsd | dgfdg | sdfsdfsdfsdfsdfsd | CENTRAL WORKSHOP | 2026-01-16 10:07:38.087000+00:00 | 2026-01-16 10:08:04.599000+00:00 | 00:00:26.512 | APPROVED | 33 | 2026-01-16 10:07:38.935000+00:00 | 2026-01-16 10:08:04.595533+00:00 | AUTOMOBILE | None |
| 1 | 2026-01-14 12:17:31.811000+00:00 | INDENT | IND01 | R1 | Shravan Nirmalkar | PC | SM | S01160007 | ABSORPTION VESSEL FOR C&C APPARATUS | 2 | LTR | CDP model with digital board | HP | USE FOR OFFICE  | ADMINISTRATION OFFICE | 2026-01-14 12:17:31.811000+00:00 | None | None | PENDING | None | 2026-01-14 12:17:32.516000+00:00 | 2026-01-19 07:25:13.661123+00:00 | None | srm001 |

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
