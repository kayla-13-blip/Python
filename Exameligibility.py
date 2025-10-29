import datetime
MIN_AGE = 18
REGISTRATION_CUTOFF = datetime.date(2025, 10, 20)
print("Exam Eligibility Checker")
birth_year= int(input("Enter your year of birth : "))
reg_year= int(input("Enter your registration year : "))
reg_mounth= int(input("Enter your registration mounth : "))
reg_day= int(input("Enter your registration day : "))
current_year = datetime.date.today().year
age = current_year - birth_year
is_age_eligible = age>=MIN_AGE
registration_date = datetime.date(reg_year, reg_mounth, reg_day)
is_registration_eligible = registration_date <= REGISTRATION_CUTOFF
print("\n--- Your Eligibility Status ---")
if is_age_eligible and is_registration_eligible:
    print("CONGRATULATIONS! you are eligible for the exam.") 
elif not is_age_eligible:
    print("You are not eligible. You must be at least {MIN_AGE} years old. ")
elif not is_registration_eligible:
    print("You are not eligible. Your registration was after the cutoff date.")
else:
    print("You are not eligible")
