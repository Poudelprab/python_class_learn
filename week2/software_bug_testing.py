#asking user to enter project name, bug id, and bug description 
pname = input("Enter your project name: ")
bugid= int(input("Enter your bug id: "))
bugdesc= input("Enter your bug description: ")

#asking user to enter bug severity score(1-5)
bugseverity= int(input("Enter your bug severity score (1-5): "))

# asking users to entr estimated hours to fix the bug
estimated_hours = float(input("Enter the estimated hours to fix the bug: "))

#asking for the developers hourly rate
hourly_rate = float(input("Enter the developer's hourly rate: "))

#asking whether the bug is reproducible or not
reproducible = input("Is the bug reproducible? (yes/no): ")
reproducible = reproducible.lower() == "yes"  
#calculating the estimated fixing cost
estimated_cost = estimated_hours * hourly_rate

#calculating testing time (25% of the fixing hours)
testing_time = estimated_hours * 0.25

#calculating the total estimated development time and cost, including testing
total_estimated_time = estimated_hours + testing_time
total_estimated_cost = total_estimated_time * hourly_rate


is_critical = bugseverity >= 4
long_fix = estimated_hours > 8
expensive = total_estimated_cost > 1000
urgent = is_critical and reproducible

print("\n" + "=" *30)
print("     Bug Report Summary")
print("=" *30)
print(f" Project name:{pname}")
print(f" Bug ID: {bugid}")
print(f" Bug Description: {bugdesc}")
print(f" Bug Severity Score: {bugseverity}")
print(f" Estimated Hours to fix: {estimated_hours:.2f} hours")
print(f" Developer's Hourly Rate: ${hourly_rate:.2f}")
print(f" Estimated Fixing Cost: ${estimated_cost:.2f}")
print(f" Testing Time: {testing_time:.2f} hours")
print(f" Total Estimated Development Time: {total_estimated_time:.2f} hours")
print(f" Is Critical: {is_critical}")
print(f" Long Fix: {long_fix}")
print(f" Expensive: {expensive}")
print(f" Urgent: {urgent}")
print("=" *30)
