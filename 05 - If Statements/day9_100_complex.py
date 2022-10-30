# Understand Roth IRA Contributions for 2022
if (married == True and file_status == 'joint') or widow == True:
    if adj_gross_income < 204000:
        print('You can contribute up to the limit.')
    elif 204000 <= adj_gross_income < 214000:
        print('You can contribute a reduced amount.')
    else: print('You are not allowed to contribute.')

elif (married == True and file_status == 'separate'):
    if live_with_spouse == True:
        if adj_gross_income < 10000:
            print('You can contribute a reduced amount.')
        elif adj_gross_income >= 10000:
            print('You are not allowed to contribute.')

elif (file_status == 'single'\
    or file_status == 'head of household'\
    or (married == True and live_with_spouse == False)):
    if adj_gross_income < 129_000:
        print('You can contribute up to the limit.')
    elif 129_000 <= adj_gross_income < 144_000:
        print('You can contribute a reduced amount.')
    elif adj_gross_income >= 144_000:
        print('You are not allowed to contribute.')