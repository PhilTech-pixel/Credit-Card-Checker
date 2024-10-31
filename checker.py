#Check the validity of credit card numbers using the Lehn's Algorithm


#Ask user for the credit card number

cardNumber = int(input("Enter your card number(No Spaces): "))

if len(str(cardNumber)) < 16 or len(str(cardNumber)) > 16:
    print("Invalid card number, please try again.")
else:
    print("Your card number is:", cardNumber)


#print(str(cardNumber)[0])

#Double the value of every second digit

#Make the numbers into a list

converted = [int(x) for x in str(cardNumber)]

#print(converted)


notAltered = converted[1] + converted[3] + converted[5] + converted[7] + converted[9] + converted[11] + converted[13] + converted[15]
#print("Sum of not altered is",notAltered)

cardUser = 4478150139565111

altered = [converted[0] *2, converted[2] *2, converted[4] *2,converted[6] *2,converted[8] *2,converted[10] *2,converted[12] *2,converted[14] *2]
#print(altered)

reduced = [num - 9 if num > 9 else num for num in altered]
#print(reduced)
completed = sum(reduced)

total = completed + notAltered
#print(total)

if total % 10 == 0:
    print("The credit card number is valid")
else:
    print("The credit card number is not valid")







#print(second[2])


