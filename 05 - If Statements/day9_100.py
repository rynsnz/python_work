# Set values for filing status
file_status = 'single'
adj_gross_income = 143_000
married = False
live_with_spouse = False

# Amount of Roth IRA Contributions That You Can Make for 2022
if (file_status == 'single' or file_status == 'head of household'\
or (married == True and file_status == 'married filing separately'\
and live_with_spouse == False)):
    if adj_gross_income < 129_000:
        print('You can contribute up to the limit.')
    elif 129_000 <= adj_gross_income < 144_000:
        print('You can contribute a reduced amount.')
    elif adj_gross_income >= 144_000:
        print('You are not allowed to contribute.')