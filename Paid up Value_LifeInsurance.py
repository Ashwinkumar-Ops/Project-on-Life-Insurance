#Paid up value = ((Number of premiums paid / Total number of premiums payable) * Sum Insured) + Bonus (if any)


paidup_val = 0 #Paid up value

policy_no = int(input("Please provide Policy Number: ")) #Policy Number

policy_hldname = str(input("Please provide Policy Holders Name: ")) #Policy Holders Name

policy_type = input("Please provide Policy Plan Type\nType T-Tradition ; U-Unit LinkedInsurance Plan: ") #Policy Plan Type: T-Tradition ; U-Unit LinkedInsurance Plan

number_ann_prem_paid = int(input("Number of premiums paid (in years): ")) #Number of premiums paid-Annual

number_ann_prem_payable = int(input("Number of premiums payable or policy premium paying term (in years): ")) #Total number of premiums payable-Annual

sum_insured = int(input("Please provide Sum Insured: ")) #Sum Insured

bonus = int(input("Please provide Bonus, if applicable: ")) #Bonus (if any)

print("\n ***** Thank you for your Input ***** ",end="\n")

print("\n")

print("***************************", "End Of Output", "***************************\n")

error = 0

if number_ann_prem_paid <= 3:
    error += 1
    print("Error:", error, end=": ")
    print("\nThe Policy Number:", policy_no, "of", policy_hldname, "is Lapsed without any paid up value.",end="\n")
    sum_insured = 0
    bonus = 0

print("\n")

if policy_type == "U":
    error += 1
    print("Error:", error, end=": ")
    print("\nThe Policy Number:", policy_no, "of", policy_hldname, "is ULIP, paid up value is not applicable for ULIP.\n")
    sum_insured = 0
    bonus = 0


print("***************************", "Error: ", error, "***************************\n")

paidup_val = (((number_ann_prem_paid / number_ann_prem_payable) * sum_insured) + bonus)

print("Final Decision:\n")

print("The paid up value for Policy Number: ", policy_no, "of", policy_hldname, "is" , paidup_val)

print("\n")

print("***************************", "End Of Line", "***************************\n")

print("\n")

print(" ***** Have a Nice Day ***** ",end="\n")
