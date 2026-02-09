# Test Cases – SkillShikshya Website Automation

## 1. Course Search

### 1.1 Search QA Course Test
**Test Case ID:** TC_CS_001  
**Description:** Verify that searching for a course returns relevant results.  
**Steps:**  
1. Navigate to https://skillshikshya.com/  
2. Enter "QA" in the search box  
3. Submit the search  
4. Observe the results page  
**Expected Result:** Page shows results containing "QA" or "Quality".  

### 1.2 Search Non-existing Course Test
**Test Case ID:** TC_CS_002  
**Description:** Verify that searching for a non-existing course returns a "No results" message.  
**Steps:**  
1. Navigate to https://skillshikshya.com/  
2. Enter "XYZCourse" in the search box  
3. Submit the search  
4. Observe the results page  
**Expected Result:** Page shows "No results found" or similar message.  

### 1.3 Empty Search Test
**Test Case ID:** TC_CS_003  
**Description:** Verify that submitting the search with empty input returns all courses or a proper message.  
**Steps:**  
1. Navigate to https://skillshikshya.com/  
2. Leave search box empty  
3. Submit the search  
4. Observe the results page  
**Expected Result:** Either all courses are displayed or a "Please enter search term" message appears.  

---

## 2. Enrollment Form

### 2.1 Valid Enrollment Test
**Test Case ID:** TC_EF_001  
**Description:** Verify that filling and submitting the enrollment form with valid data is successful.  
**Steps:**  
1. Navigate to https://skillshikshya.com/enroll-form  
2. Fill all fields with valid data  
3. Click Submit  
**Expected Result:** Page shows success message like "Thank you" or "Success".  

### 2.2 Empty Email Test
**Test Case ID:** TC_EF_002  
**Description:** Verify that form validation works when the email field is empty.  
**Steps:**  
1. Leave email field empty  
2. Fill all other fields  
3. Click Submit  
**Expected Result:** Form shows an error like "Email is required".  

### 2.3 Invalid Email Test
**Test Case ID:** TC_EF_003  
**Description:** Verify that entering an invalid email triggers a validation error.  
**Steps:**  
1. Enter "invalidEmail" in email field  
2. Fill all other fields  
3. Click Submit  
**Expected Result:** Form shows error "Enter valid email".  

### 2.4 Missing Required Field Test
**Test Case ID:** TC_EF_004  
**Description:** Verify that the form cannot be submitted if a required field is empty.  
**Steps:**  
1. Leave "Name" field empty  
2. Fill other fields  
3. Click Submit  
**Expected Result:** Error message appears indicating the missing field.  

### 2.5 Invalid Phone Number Test
**Test Case ID:** TC_EF_005  
**Description:** Verify that the form validates phone number format.  
**Steps:**  
1. Enter letters or less than 8 digits in phone field  
2. Click Submit  
**Expected Result:** Error message appears indicating invalid phone number.  

### 2.6 Select Mode of Training Test
**Test Case ID:** TC_EF_006  
**Description:** Verify that the mode of training can be selected correctly.  
**Steps:**  
1. Choose "Online" or "Offline"  
2. Click Submit  
**Expected Result:** Selected mode is saved successfully.  

### 2.7 Grade Selection Test
**Test Case ID:** TC_EF_007  
**Description:** Verify that the grade dropdown works correctly.  
**Steps:**  
1. Select any grade  
2. Click Submit  
**Expected Result:** Selected grade is saved successfully.  

---

## 3. User Login

### 3.1 Valid Login Test
**Test Case ID:** TC_UL_001  
**Description:** Verify that a registered user can log in successfully.  
**Steps:**  
1. Navigate to https://skillshikshya.com/login  
2. Enter valid email and password  
3. Click Submit  
**Expected Result:** Dashboard or logout option is visible.  

### 3.2 Invalid Password Test
**Test Case ID:** TC_UL_002  
**Description:** Verify that login fails with an invalid password.  
**Steps:**  
1. Enter valid email  
2. Enter invalid password  
3. Click Submit  
**Expected Result:** Error message appears like "Invalid credentials".  

### 3.3 Empty Fields Login Test
**Test Case ID:** TC_UL_003  
**Description:** Verify that login validation works for empty fields.  
**Steps:**  
1. Leave email or password empty  
2. Click Submit  
**Expected Result:** Error message appears like "Email and password are required".  

### 3.4 Remember Me Checkbox Test
**Test Case ID:** TC_UL_004  
**Description:** Verify that "Remember Me" option works correctly.  
**Steps:**  
1. Check "Remember Me"  
2. Login and logout  
3. Revisit login page  
**Expected Result:** Email remains pre-filled in login form.  

---

## 4. User Registration

### 4.1 Valid Registration Test
**Test Case ID:** TC_UR_001  
**Description:** Verify that a new user can register with valid details.  
**Steps:**  
1. Navigate to https://skillshikshya.com/register  
2. Fill name, email, password, confirm password  
3. Click Submit  
**Expected Result:** User sees "Registered successfully" or "Verify your email".  

### 4.2 Password Mismatch Test
**Test Case ID:** TC_UR_002  
**Description:** Verify registration fails if password and confirm password do not match.  
**Steps:**  
1. Enter different passwords  
2. Click Submit  
**Expected Result:** Error message appears like "Passwords do not match".  

### 4.3 Invalid Email Test
**Test Case ID:** TC_UR_003  
**Description:** Verify registration fails with invalid email format.  
**Steps:**  
1. Enter invalid email like "useremail"  
2. Click Submit  
**Expected Result:** Error message appears like "Enter a valid email".  

### 4.4 Empty Field Registration Test
**Test Case ID:** TC_UR_004  
**Description:** Verify that registration validation works when fields are empty.  
**Steps:**  
1. Leave required fields empty  
2. Click Submit  
**Expected Result:** Error message appears for missing fields.  

### 4.5 Duplicate Email Registration Test
**Test Case ID:** TC_UR_005  
**Description:** Verify that registration fails if email is already registered.  
**Steps:**  
1. Enter an email that is already registered  
2. Click Submit  
**Expected Result:** Error message appears like "Email already exists".  



