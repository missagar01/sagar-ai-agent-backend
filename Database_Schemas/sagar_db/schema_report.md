# 🗄️ Schema Report: Sagar001122 System
**Generated:** 2026-02-03 13:10

---

## 📋 Table: `persons`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `INTEGER` | False |
| **name** | `TEXT` | False |
| **address** | `TEXT` | True |




### 🏷️ Categorical / Allowed Values:
- **`name`** (3 values): `['Anjali Singh', 'Rohit Sharma', 'Vikas Choudhary']`
- **`address`** (3 values): `['Delhi, India', 'Mumbai, Maharashtra', 'Raipur, Chhattisgarh']`


### 🔍 Sample Data (First 3 rows):
| id | name | address |
| --- | --- | --- |
| 1 | Vikas Choudhary | Raipur, Chhattisgarh |
| 2 | Rohit Sharma | Mumbai, Maharashtra |
| 3 | Anjali Singh | Delhi, India |

---

## 📋 Table: `login`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `BIGINT` | False |
| **username** | `TEXT` | False |
| **password** | `TEXT` | False |
| **role** | `TEXT` | False |
| **page_access** | `ARRAY` | True |
| **created_at** | `TIMESTAMP` | True |




### 🏷️ Categorical / Allowed Values:
- **`role`** (2 values): `['admin', 'user']`


### 🔍 Sample Data (First 3 rows):
| id | username | password | role | page_access | created_at |
| --- | --- | --- | --- | --- | --- |
| 8 | Sandeep Kumar Dubey | user18 | user | ['Dashboard', 'Machines', 'Assign Task', 'Tasks',  | 2025-11-13 12:18:13.868279+00:00 |
| 10 | Janak Kumar | user56 | admin | ['Dashboard', 'Machines', 'Assign Task', 'Tasks',  | 2025-11-13 12:18:13.868279+00:00 |
| 11 | Shravan Nirmalkar | user2 | admin | ['Dashboard', 'Machines', 'Assign Task', 'Tasks',  | 2025-11-13 12:18:13.868279+00:00 |

---

## 📋 Table: `form_responses`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `TEXT` | False |
| **serial_no** | `VARCHAR(100)` | True |
| **machine_name** | `VARCHAR(255)` | True |
| **purchase_date** | `DATE` | True |
| **purchase_price** | `NUMERIC(12, 2)` | True |
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
- **`maintenance_schedule`** (16 values): `['15 DAY', '15 DAYS', '1 MONTH', '30 DAYS', '7 DAY', '7DAYS', '7 DAYS', '8 MONTH', 'Daily', 'DAILY', '["Daily","Weekly"]', 'Daily, Weekly', 'Half-Yearly', 'MONTHLY', 'Weekly', '["Weekly"]']`
- **`department`** (14 values): `['ALL ELECTRICAL', 'CCM', 'CCM MAINTENANCE', 'IT', 'LAB AND QUALITY CONTROL', 'PIPE MILL ELECTRICAL', 'PIPE MILL MAINTENANCE', 'SMS ELECTRICAL', 'SMS MAINTENANCE', 'STORE', 'STRIP MILL ELECTRICAL', 'STRIP MILL PRODUCTION', 'TRANSPORT', 'WORKSHOP']`
- **`user_allot`** (7 values): `['30:1', '40:1', '80:1', 'asdsad', 'SPECTRO', 'user', 'vikas']`


### 🔍 Sample Data (First 3 rows):
| id | serial_no | machine_name | purchase_date | purchase_price | vendor | model_no | warranty_expiration | manufacturer | maintenance_schedule | department | location | initial_maintenance_date | user_manual | purchase_bill | notes | tag_no | user_allot |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | SRMPL\ALL IN ONE\01 | ALL IN ONE PC | None | None | None | None | None | None | None | IT | None | None | None | None | None | SRMPL\ALL IN ONE\01 | None |
| 2 | SRMPL\KEYBOARD\01 | KEYBOARD | None | None | None | None | None | None | None | IT | None | None | None | None | None | SRMPL\KEYBOARD\01 | None |
| 3 | SRMPL\MOUSE\01 | MOUSE | None | None | None | None | None | None | None | IT | None | None | None | None | None | SRMPL\MOUSE\01 | None |

---

## 📋 Table: `working_day_calendar`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `BIGINT` | False |
| **working_date** | `DATE` | False |
| **day_name** | `TEXT` | True |
| **week_num** | `INTEGER` | True |
| **month_num** | `INTEGER` | True |




### 🏷️ Categorical / Allowed Values:
- **`day_name`** (7 values): `['Fri', 'Mon', 'Sat', 'Sun', 'Thu', 'Tue', 'Wed']`


### 🔍 Sample Data (First 3 rows):
| id | working_date | day_name | week_num | month_num |
| --- | --- | --- | --- | --- |
| 1 | 2025-07-27 | Sun | 30 | 7 |
| 2 | 2025-07-28 | Mon | 31 | 7 |
| 3 | 2025-07-29 | Tue | 31 | 7 |

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
| 14 | Lakhan Dutta | DISPATCH | ROSHAN RAJAK | None | None | None | 2025-11-25 05:24:01.832024+00:00 | None |
| 15 | Nand Kishor Bisen | DISPATCH | SUMAN JHA | None | None | None | 2025-11-25 05:24:01.832024+00:00 | None |
| 16 | Sandeep Kumar Dubey | AUTOMATION | MRIGENDRA NARAYAN BEPARI | None | None | None | 2025-11-25 05:24:01.832024+00:00 | None |

---

## 📋 Table: `maintenance_task_assign_staging`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **time_stamp** | `TEXT` | True |
| **task_no** | `TEXT` | True |
| **serial_no** | `TEXT` | True |
| **machine_name** | `TEXT` | True |
| **given_by** | `TEXT` | True |
| **doer_name** | `TEXT` | True |
| **task_type** | `TEXT` | True |
| **machine_area** | `TEXT` | True |
| **part_name** | `TEXT` | True |
| **need_sound_test** | `TEXT` | True |
| **temperature** | `TEXT` | True |
| **enable_reminders** | `TEXT` | True |
| **require_attachment** | `TEXT` | True |
| **task_start_date** | `TEXT` | True |
| **frequency** | `TEXT` | True |
| **description** | `TEXT` | True |
| **priority** | `TEXT` | True |
| **department** | `TEXT` | True |
| **location** | `TEXT` | True |
| **purchase_price** | `TEXT` | True |
| **actual_date** | `TEXT` | True |
| **delay** | `TEXT` | True |
| **task_status** | `TEXT` | True |
| **remarks** | `TEXT` | True |
| **sound_status** | `TEXT` | True |
| **temperature_status** | `TEXT` | True |
| **image_link** | `TEXT` | True |
| **file_name** | `TEXT` | True |
| **file_type** | `TEXT` | True |
| **maintenance_cost** | `TEXT` | True |




### 🏷️ Categorical / Allowed Values:
- **`given_by`** (8 values): `['BALDEV SINGH SAINI', 'DANVEER SINGH', 'DEEPAK BHALLA', 'DHANJI', 'RAJNISH BHARDWAJ', 'ROSHAN RAJAK', 'SHAILESH CHITRE', 'TEJ BAHADUR YADAV']`
- **`task_type`** (1 values): `['Maintenance']`
- **`machine_area`** (15 values): `['Continues mill', 'Finish mill', 'Mill', 'Patra Mill', 'Patra mill workshop', 'Sms crene', 'Strip mill', 'unit-1', 'Unit 1', 'Unit-1', 'UNIT- 1', 'UNIT- 2', 'Workshop', 'यूनिट 1', 'यूनिट 2']`
- **`part_name`** (21 values): `['Carbon brush', 'Carbon brush and clean', 'Carbon brush and clean motor', 'Check all motor and check carbon brush.', 'Check and clean', 'Check carbon', 'Check connection clean motor', 'Check feeder and contractor kit', 'Check kit and clean panel', 'Check kit and loose connection clean panel', 'Check kit and silip ring motor and cly', 'Clean and change carbon brush', 'Contractor kit', 'Lt motor', 'Lub oil and coolant water', 'Lub oil cleaning', 'Motor', 'Motor and blower', 'n', 'No', 'UNIT- 1']`
- **`need_sound_test`** (2 values): `['No', 'Yes']`
- **`temperature`** (2 values): `['No', 'Yes']`
- **`enable_reminders`** (2 values): `['No', 'Yes']`
- **`require_attachment`** (2 values): `['No', 'Yes']`
- **`frequency`** (4 values): `['daily', 'monthly', 'one-time', 'weekly']`
- **`priority`** (8 values): `['15 DAY', '15 DAYS', '1 MONTH', 'DAILY', 'High', 'Medium', 'MONTHLY', 'WEEKLY']`
- **`actual_date`** (1 values): `['05/12/2025']`
- **`task_status`** (1 values): `['Yes']`
- **`remarks`** (1 values): `['ok']`
- **`sound_status`** (1 values): `['Ok']`
- **`temperature_status`** (1 values): `['0']`


### 🔍 Sample Data (First 3 rows):
| time_stamp | task_no | serial_no | machine_name | given_by | doer_name | task_type | machine_area | part_name | need_sound_test | temperature | enable_reminders | require_attachment | task_start_date | frequency | description | priority | department | location | purchase_price | actual_date | delay | task_status | remarks | sound_status | temperature_status | image_link | file_name | file_type | maintenance_cost |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 19/11/2025, 11:35:22 | TM-001 | SRMPL-c5dcmotor/001 | C5 DC MOTOR | DANVEER SINGH | Dhirendra Tripathi | Maintenance | Continues mill | Motor and blower | No | No | Yes | Yes | 07/12/2025 10:32:00 | weekly | Check carbon brush and clean motor  . | High | None | None | None | None | None | None | None | None | None | None | None | None | None |
| 19/11/2025, 11:35:22 | TM-002 | SRMPL-c5dcmotor/001 | C5 DC MOTOR | DANVEER SINGH | Dhirendra Tripathi | Maintenance | Continues mill | Motor and blower | No | No | Yes | Yes | 14/12/2025 10:32:00 | weekly | Check carbon brush and clean motor  . | High | None | None | None | None | None | None | None | None | None | None | None | None | None |
| 19/11/2025, 11:35:22 | TM-003 | SRMPL-c5dcmotor/001 | C5 DC MOTOR | DANVEER SINGH | Dhirendra Tripathi | Maintenance | Continues mill | Motor and blower | No | No | Yes | Yes | 21/12/2025 10:32:00 | weekly | Check carbon brush and clean motor  . | High | None | None | None | None | None | None | None | None | None | None | None | None | None |

---

## 📋 Table: `maintenance_task_assign`
### Columns:
| Name | Type | Nullable |
| :--- | :--- | :--- |
| **id** | `BIGINT` | False |
| **created_at** | `TIMESTAMP` | True |
| **Time_Stamp** | `TIMESTAMP` | True |
| **Task_No** | `VARCHAR(50)` | True |
| **Serial_No** | `VARCHAR(100)` | True |
| **Machine_Name** | `VARCHAR(255)` | True |
| **Given_By** | `VARCHAR(255)` | True |
| **Doer_Name** | `VARCHAR(255)` | True |
| **Task_Type** | `VARCHAR(100)` | True |
| **Machine_Area** | `VARCHAR(255)` | True |
| **Part_Name** | `VARCHAR(255)` | True |
| **Need_Sound_Test** | `BOOLEAN` | True |
| **Temperature** | `VARCHAR(50)` | True |
| **Enable_Reminders** | `BOOLEAN` | True |
| **Require_Attachment** | `BOOLEAN` | True |
| **Task_Start_Date** | `DATE` | True |
| **Frequency** | `VARCHAR(50)` | True |
| **Description** | `TEXT` | True |
| **Priority** | `VARCHAR(50)` | True |
| **machine_department** | `VARCHAR(100)` | True |
| **Actual_Date** | `DATE` | True |
| **Delay** | `VARCHAR(50)` | True |
| **Task_Status** | `VARCHAR(50)` | True |
| **Remarks** | `TEXT` | True |
| **Sound_Status** | `VARCHAR(50)` | True |
| **Temperature_Status** | `VARCHAR(50)` | True |
| **Image_Link** | `TEXT` | True |
| **File_Name** | `VARCHAR(255)` | True |
| **File_Type** | `VARCHAR(100)` | True |
| **Maintenance_Cost** | `NUMERIC(12, 2)` | True |
| **doer_department** | `VARCHAR(255)` | True |




### 🏷️ Categorical / Allowed Values:
- **`Given_By`** (18 values): `['', 'ANIL KUMAR MISHRA', 'ANUP KUMAR BOPCHE', 'BALDEV SINGH SAINI', 'DANVEER SINGH', 'DEEPAK BHALLA', 'DHANJI', 'G RAM MOHAN RAO', 'HULLAS PASWAN', 'RAJNISH BHARDWAJ', 'RINKU GAUTAM', 'ROSHAN RAJAK', 'SACHIN SAXENA', 'SANDEEP DUBEY', 'SHAILESH CHITRE', 'SHREE RAM PATLE', 'SUMAN JHA', 'TEJ BAHADUR YADAV']`
- **`Task_Type`** (1 values): `['Maintenance']`
- **`Machine_Area`** (25 values): `['', 'Continues mill', 'Finish mill', 'I', 'Mill', 'Patra mill workshop', 'PIPE MILL', 's', 'S', 'Sms crene', 'Strip mill', 'Strip Mill', 'U', 'uint-1', 'unit-1', 'Unit 1', 'Unit-1', 'UNIT-1', 'UNIT- 1', 'unit-2', 'UNIT-2', 'UNIT- 2', 'Workshop', 'यूनिट 1', 'यूनिट 2']`
- **`Part_Name`** (24 values): `['', '`', 'Carbon brush', 'Carbon brush and clean', 'Carbon brush and clean motor', 'Check all motor and check carbon brush.', 'Check and clean', 'Check carbon', 'Check connection clean motor', 'Check feeder and contractor kit', 'Check kit and clean panel', 'Check kit and loose connection clean panel', 'Clean and change carbon brush', 'Contractor kit', 'Lt motor', 'Lub oil and coolant water', 'Lub oil cleaning', 'Motor', 'Motor and blower', 'n', 'No', 'PIPE MILL', 'UNIT-1', 'UNIT- 1']`
- **`Need_Sound_Test`** (2 values): `['False', 'True']`
- **`Temperature`** (3 values): `['', 'No', 'Yes']`
- **`Enable_Reminders`** (2 values): `['False', 'True']`
- **`Require_Attachment`** (2 values): `['False', 'True']`
- **`Frequency`** (3 values): `['daily', 'monthly', 'weekly']`
- **`Priority`** (10 values): `['', '15 DAY', '15 DAYS', '1 MONTH', 'DAILY', 'High', 'Low', 'Medium', 'MONTHLY', 'WEEKLY']`
- **`machine_department`** (7 values): `['PIPE MILL ELECTRICAL', 'PIPE MILL MAINTENANCE', 'SMS ELECTRICAL', 'SMS MAINTENANCE', 'STRIP MILL ELECTRICAL', 'STRIP MILL PRODUCTION', 'WORKSHOP']`
- **`Task_Status`** (4 values): `['no', 'No', 'yes', 'Yes']`
- **`Remarks`** (1 values): `['']`
- **`Sound_Status`** (5 values): `['', 'Bad', 'Good', 'Need Repair', 'OK']`
- **`Temperature_Status`** (3 values): `['', '31', '32']`
- **`doer_department`** (9 values): `['PIPE MILL ELECTRICAL', 'PIPE MILL MAINTENANCE', 'PIPE MILL PRODUCTION', 'SMS ELECTRICAL', 'SMS MAINTENANCE', 'STRIP MILL ELECTRICAL', 'STRIP MILL MAINTENANCE', 'STRIP MILL PRODUCTION', 'WORKSHOP']`


### 🔍 Sample Data (First 3 rows):
| id | created_at | Time_Stamp | Task_No | Serial_No | Machine_Name | Given_By | Doer_Name | Task_Type | Machine_Area | Part_Name | Need_Sound_Test | Temperature | Enable_Reminders | Require_Attachment | Task_Start_Date | Frequency | Description | Priority | machine_department | Actual_Date | Delay | Task_Status | Remarks | Sound_Status | Temperature_Status | Image_Link | File_Name | File_Type | Maintenance_Cost | doer_department |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 82 | 2025-12-22 09:50:28.971971+00:00 | 2025-11-28 15:35:29 | TM-082 | SM/MILL/DG-003 | COMPRESSOR1 | None | Shiv Kumar Yadav | Maintenance | Strip mill | Motor  | False | No | False | False | 2026-03-04 | weekly | Check and clean  | WEEKLY | STRIP MILL ELECTRICAL | None | None | None | None | None | None | None | None | None | None | STRIP MILL PRODUCTION |
| 83 | 2025-12-22 09:50:28.971971+00:00 | 2025-11-28 15:35:29 | TM-083 | SM/MILL/DG-003 | COMPRESSOR1 | None | Shiv Kumar Yadav | Maintenance | Strip mill | Motor  | False | No | False | False | 2026-03-11 | weekly | Check and clean  | WEEKLY | STRIP MILL ELECTRICAL | None | None | None | None | None | None | None | None | None | None | STRIP MILL PRODUCTION |
| 84 | 2025-12-22 09:50:28.971971+00:00 | 2025-11-28 15:35:29 | TM-084 | SM/MILL/DG-003 | COMPRESSOR1 | None | Shiv Kumar Yadav | Maintenance | Strip mill | Motor  | False | No | False | False | 2026-03-18 | weekly | Check and clean  | WEEKLY | STRIP MILL ELECTRICAL | None | None | None | None | None | None | None | None | None | None | STRIP MILL PRODUCTION |

---
