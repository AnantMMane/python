print('-' * 30)
print('Food Tracker App')
print('-' * 30)
print()

print('Its Saturday. Should I eat cake and ice-cream today?')

weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
answers = []

for i in weekdays:
    print(f'Did you eat healthy on {i}?')
    answer = input("'Y' or 'N'")
    if answer == 'Y':
        answers.append(answer)

print()
print('calculating the answer...')

if len(answers) == 6:
    print('Yes. You can eat the cake and ice-cream today.')
elif len(answers) == 5:
    print('May be. Lay off ice-cream today.')
else:
    print('Cake is the lie and so the ice-cream!')
