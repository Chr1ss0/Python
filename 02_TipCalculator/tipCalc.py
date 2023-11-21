print('Welcome to the Tip-Calculator')
total_amount = input('What was the total bill?\n$ ')
total_people = input('How many People are you?\n')
tip = input('How much to you want to tip? 10,12,15,20%?')
amount_each = float(total_amount) * (int(tip) / 100 + 1) / int(total_people)
amount_format = "{:.2f}".format(amount_each)

print(f'Each person habe to pay {amount_format} $') 