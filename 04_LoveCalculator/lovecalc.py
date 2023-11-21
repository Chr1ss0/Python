print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
name_together = name1.lower() + name2.lower()
name_t = name_together.count('t')
name_r = name_together.count('r')
name_u = name_together.count('u')
name_e = name_together.count('e')
count_true = name_t + name_r + name_u + name_e
name_l = name_together.count('l')
name_o = name_together.count('o')
name_v = name_together.count('v')
name_le = name_together.count('e')
count_love = name_l + name_o + name_v + name_le
score = str(count_true)+str(count_love)

if int(score) < 10 or int(score) > 90:
    print(f'Your score is {count_true}{count_love} you go together like coke and mentos.')
elif int(score) >= 40 and int(score) <= 50:
    print(f'Your score is {count_true}{count_love}, you are alright together.')
else: 
    print(f'Your score is {count_true}{count_love}.')