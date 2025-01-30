team_structure = {
    "Robert Downey": {
        "role": "Project Manager",
        "experience_years": 0,
        "TLs": {
            "Mark": {
                "role": "Team Lead",
                "experience_years": 8,
                "team": {
                    "Leonardo": {"role": "Junior Developer", "experience_years": 1, "mentor": "Mark"},
                    "Alexandra": {"role": "Junior Developer", "experience_years": 1, "mentor": "Mark"}
                }
            },
            "Samuel": {
                "role": "Team Lead",
                "experience_years": 8
            },
            "Paul": {
                "role": "Team Lead",
                "experience_years": 8,
                "team": {
                    "Fergal": {"role": "Senior Developer", "experience_years": 4.5, "mentor": "Paul"}
                }
            },
            "Tom": {
                "role": "Team Lead",
                "experience_years": 8,
                "team": {
                    "Jerry": {"role": "Junior Developer", "experience_years": 1.5, "mentor": "Tom"},
                    "John": {"role": "Junior Developer", "experience_years": 1.6, "mentor": "Tom"}
                }
            }
        }
    },
    "Anne Hathaway": {
        "role": "Project Manager",
        "experience_years": 0,
        "TLs": {
            "Chris": {
                "role": "Team Lead",
                "experience_years": 5,
                "team": {
                    "James": {
                        "role": "Team Lead",
                        "experience_years": 0,
                        "team": {
                            "Jennifer": {"role": "Senior Developer", "experience_years": 3.8},
                            "Scott": {"role": "Senior Developer", "experience_years": 3.8},
                            "Sophie": {"role": "Senior Developer", "experience_years": 3.8}
                        }
                    }
                }
            },
            "Pratt": {
                "role": "Team Lead",
                "experience_years": 5
            },
            "Emma": {
                "role": "Team Lead",
                "experience_years": 5
            },
            "Will": {
                "role": "Team Lead",
                "experience_years": 5,
                "team": {
                    "Ryan": {"role": "Senior Developer", "experience_years": 3.5, "manager": "Will"},
                    "Edge": {"role": "Senior Developer", "experience_years": 3, "manager": "Will"}
                }
            },
            "Smith": {
                "role": "Team Lead",
                "experience_years": 5,
                "team": {
                    "Walker": {"role": "Senior Developer", "experience_years": 2.7, "manager": "Smith"},
                    "Diana": {"role": "Senior Developer", "experience_years": 2.7, "manager": "Smith"}
                }
            }
        }
    }
}

#a.
def employee_name_by_pm(pm_name,team_structure):
    employees = []
    if pm_name in team_structure:
        pm_data = team_structure[pm_name]
        for tl_name, tl_data in pm_data["TLs"].items():
            employees.append(tl_name)
            if "team" in tl_data:
                for emp_name, emp_data in tl_data["team"].items():
                    employees.append(emp_name)
                    if "team" in emp_data:
                        for name in emp_data["team"].keys():
                            employees.append(name)       
                    

    return employees

pm_name = input("Please give the project manager name to display all employees' names: ")
print(employee_name_by_pm(pm_name,team_structure))

#b.
def employee_name_filter_experience(exp_years,team_structure):
    employee = []

    for pm_name in team_structure.keys():
        pm_data = team_structure[pm_name]
        for tl_name, tl_data in pm_data["TLs"].items():
            if pm_data["TLs"][tl_name]["experience_years"]>exp_years:
                employee.append(tl_name)
            if "team" in tl_data:
                for emp_name, emp_data in tl_data["team"].items():
                    if tl_data["team"][emp_name]["experience_years"]>exp_years:
                        employee.append(emp_name)
                    if "team" in emp_data:
                        for name in emp_data["team"].keys():
                            if emp_data["team"][name]["experience_years"]>exp_years:
                                employee.append(name) 
    return employee

try:
	experience_years = int(input("Please Enter experience years to filter(more than) the employee name: "))
	print(employee_name_filter_experience(experience_years,team_structure))
except:
	print("Invalid Input")

#c.
def update_experience_years(new_exp_years,lower_limit,upper_limit,team_structure):

    for pm_name in team_structure.keys():
        pm_data = team_structure[pm_name]
        for tl_name, tl_data in pm_data["TLs"].items():
            if (pm_data["TLs"][tl_name]["experience_years"]>lower_limit) and (pm_data["TLs"][tl_name]["experience_years"]<upper_limit):
                pm_data["TLs"][tl_name]["experience_years"] = new_exp_years
            if "team" in tl_data:
                for emp_name, emp_data in tl_data["team"].items():
                    if (tl_data["team"][emp_name]["experience_years"]>lower_limit) and (tl_data["team"][emp_name]["experience_years"]<upper_limit):
                        tl_data["team"][emp_name]["experience_years"] = new_exp_years
                    if "team" in emp_data:
                        for name in emp_data["team"].keys():
                            if (emp_data["team"][name]["experience_years"]>lower_limit) and (emp_data["team"][name]["experience_years"]<upper_limit):
                                emp_data["team"][name]["experience_years"] = new_exp_years

    return team_structure

try:
	new_exp_years = eval(input("Please enter new experience years: "))
	lower_limit = eval(input("Please enter lower limit of experience years: "))
	upper_limit = eval(input("Please enter upper limit of experience years: "))
	print(update_experience_years(new_exp_years,lower_limit,upper_limit,team_structure))
except:
	print("Invalid Input")

#f.
def check_employee_exp_years_less(exp_years,team_structure):
    employee = []

    for pm_name in team_structure.keys():
        pm_data = team_structure[pm_name]
        for tl_name, tl_data in pm_data["TLs"].items():
            if pm_data["TLs"][tl_name]["experience_years"]<exp_years:
                employee.append(tl_name)
            if "team" in tl_data:
                for emp_name, emp_data in tl_data["team"].items():
                    if tl_data["team"][emp_name]["experience_years"]<exp_years:
                        employee.append(emp_name)
                    if "team" in emp_data:
                        for name in emp_data["team"].keys():
                            if emp_data["team"][name]["experience_years"]<exp_years:
                                employee.append(name) 
    return employee

try:
	experience_years = int(input("Please Enter experience years to filter(less than) the employee name: "))
	print(check_employee_exp_years_less(experience_years,team_structure))
except:
	print("Invalid Input")

#g.
def update_role(_name,role,team_structure):
    for pm_name in team_structure:
        if pm_name == _name:
            team_structure[pm_name]["role"] = role
            break
        pm_data = team_structure[pm_name]
        for tl_name, tl_data in pm_data["TLs"].items():
            if tl_name == _name:
                pm_data["TLs"][tl_name]["role"] = role
                break
            if "team" in tl_data:
                for emp_name, emp_data in tl_data["team"].items():
                    if emp_name == _name:
                        tl_data["team"][emp_name]["role"] = role
                        break
                    if "team" in emp_data:
                        for name in emp_data["team"].keys():
                            if name == _name:
                                emp_data["team"][name]["role"] = role
                                break
    
    return team_structure

emp_name = input("Enter employee name for update role: ")
new_role = input("Enter new role for that employee: ")
print(update_role(emp_name,new_role,team_structure))

#d.
def display_lead_exp_years(role,team_structure):
    exp_years = []

    for pm_name in team_structure.keys():
        if team_structure[pm_name]["role"] == role:
            if team_structure[pm_name]["experience_years"] == 0:
                exp_years.append("NA")
            else:
                exp_years.append(team_structure[pm_name]["experience_years"])
        pm_data = team_structure[pm_name]
        for tl_name, tl_data in pm_data["TLs"].items():
            if pm_data["TLs"][tl_name]["role"] == role:
                if pm_data["TLs"][tl_name]["experience_years"] == 0:
                    exp_years.append("NA")
                else:
                    exp_years.append(pm_data["TLs"][tl_name]["experience_years"])
            if "team" in tl_data:
                for emp_name, emp_data in tl_data["team"].items():
                    if tl_data["team"][emp_name]["role"] == role:
                        if tl_data["team"][emp_name]["experience_years"] == 0:
                            exp_years.append("NA")
                        else:
                            exp_years.append(tl_data["team"][emp_name]["experience_years"])
                    if "team" in emp_data:
                        for name in emp_data["team"].keys():
                            if emp_data["team"][name]["role"] == role:
                                if emp_data["team"][name]["experience_years"] == 0:
                                    exp_years.append("NA")
                                else:
                                    exp_years.append(emp_data["team"][name]["experience_years"])

    return exp_years

_role = input("Enter role for display all employee experience years are under that role: ") 
print(display_lead_exp_years(_role,team_structure))

#e.
def add_team_members(left_emp_name, assign_emp_name, team_structure):
	team_member = ''
	for pm_name in team_structure:
		pm_data = team_structure[pm_name]
		for tl_name, tl_data in pm_data["TLs"].items():
		    if tl_name == left_emp_name:
		    	try:
		    		team_member = pm_data["TLs"][tl_name]["team"]
		    		deletion_emp = pm_data["TLs"]
		    		break
		    	except:
		        	print("That employee with not any team")
     		
		if team_member!='':
			for tl_name, tl_data in pm_data["TLs"].items():
				if "team" in tl_data:
					for emp_name, emp_data in tl_data["team"].items():
						if emp_name == assign_emp_name:
							tl_data["team"][emp_name]["team"] = team_member
							break
						if "team" in emp_data:
							for name in emp_data["team"].keys():
								if name == assign_emp_name:
								       	emp_data["team"][name]["team"] = team_member
								       	break					       	
	try:						       	
		for member_name in team_member.keys():
				team_member[member_name]["manager"] = assign_emp_name
		del deletion_emp[left_emp_name]	
		return team_structure
	except:
		print("Team is not.")			                   

left_emp_name = input("Enter employee name that left the company: ")
assign_emp_name = input("Enter employee name that role is assign to that employee: ")
print(add_team_members(left_emp_name, assign_emp_name, team_structure))
