def age_assignment(*names, **age_info):
    output_list = []
    new_line = "\n"
    for k in age_info:
        for name in names:
            if k in name:
                output_list.append(f"{name} is {age_info[k]} years old.")
    return new_line.join(sorted(output_list))
        
print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))