employee = { 
			'name': 'Dale', # str
			'gender': 'Male', # can be 'Male' or 'Female'
			'age': 31, # int
			'is_regular': True, # bool
	}

print(employee)

def is_insured(employee):
    insured_state = 'not insured'
    if employee['is_regular']:
        insured_state = 'insured'
    elif employee['gender'] == 'Male' and employee['age'] == 30:
        insured_state = 'insured'
    elif employee['gender'] == 'Female' and employee['age'] == 25:
        insured_state = 'insured'
    
    print(employee['name'], 'is', insured_state)

is_insured(employee)
