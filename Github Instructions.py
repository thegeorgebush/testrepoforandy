##github for idiots:
##Push changes to repo:
##git add .
##git commit -m "(message)"
##git push origin

##PUll changes from repo:
##git pull

#### With Pay rate and hours worked
#getting hours/overtime/bi-weekly paycheck


pay_rate = float(input('Input your hourly pay rate: '))
ot_rate = pay_rate * 1.5

hours = float(input('Input weekly scheduled hours: '))

if hours > 40:
    ot = (hours - 40)
elif hours < 40:
    ot = 0
elif hours == 40:
    ot = 0

reg_hours = hours - ot

paycheck= ((reg_hours*pay_rate)+(ot*ot_rate))*2




gross_income = paycheck *(26)
gross_income_1 =float(gross_income) 

print('gross income: ', gross_income)

#tax estimations
#used to check if elif below

#found error in bracket 5

tax_1 = .1
tax_2 =.12
tax_3 =.22
tax_4 =.24
tax_5=.32
tax_6=.35
tax_7=.37
bracket_1 = 10000
bracket_2= 40525
bracket_3 = 86375
bracket_4 = 164925
bracket_5 =209425
bracket_6 =523600



if gross_income_1 < bracket_1:
    fed_tax = bracket_1 * gross_income_1
elif gross_income_1 < bracket_2:
    fed_tax = tax_2 * (gross_income_1 - bracket_1) + tax_1*(bracket_1)
elif gross_income_1 < bracket_3:
    fed_tax = tax_3* (gross_income_1-bracket_2) + (tax_2*(bracket_2-bracket_1))+ tax_1*(bracket_1)
elif gross_income_1 < bracket_4:
    fed_tax = tax_4* (gross_income_1-bracket_3) + (tax_3*(bracket_3-bracket_2))+ (tax_2*(bracket_2-bracket_1))+ tax_1*(bracket_1)
elif gross_income_1 < bracket_5:
    fed_tax = tax_5* (gross_income_1-bracket_4)+(tax_4*(bracket_4-bracket_3))+(tax_3*(bracket_3-bracket_2))+(tax_2*(bracket_2-bracket_1))+ tax_1*(bracket_1)
elif gross_income_1 < bracket_6:
    fed_tax = tax_6*(gross_income_1-bracket_5)+ (tax_5* (bracket_5-bracket_4))+(tax_4*(bracket_4-bracket_3))+(tax_3*(bracket_3-bracket_2))+(tax_2*(bracket_2-bracket_1))+ tax_1*(bracket_1)
elif gross_income_1>bracket_6:
    fed_tax = tax_7*(gross_income_1-bracket_6)+(tax_6* (bracket_6-bracket_5))+ (tax_5* (bracket_5-bracket_4))+(tax_4*(bracket_4-bracket_3))+(tax_3*(bracket_3-bracket_2))+(tax_2*(bracket_2-bracket_1))+ tax_1*(bracket_1)
#ss&mc

if gross_income_1 < 142800:
    entitlements= .062*gross_income_1+.0145*gross_income_1
elif gross_income_1 > 142800:
    entitlements=.062*(142800)+.0145*142800


net_income = gross_income_1-fed_tax-entitlements

print('paycheck is: ', paycheck)
print('gross income is: ',gross_income_1)
print('tax is: ',fed_tax)
print('entitlements are: ', entitlements)
print('net income is: ',net_income)

# financial advice????????? from me?????

# given assumptions with 
## emergency fund == 6x monthly expenses
##50% spending for expenses
##20% savings
##30%spending

#ratios rent ~~ 50% of net income
#variable costs food,car,utilities, ~~ 20%
#spending ~~ 20% of net income
#savings ~~ 10% of NI


rent_cost_ideal = (net_income*.5)/12

vc_ideal = (net_income*.2)/12

spending_ideal = net_income*.2

savings_ideal = net_income*.1

print('your ideal monthly rent is: ', rent_cost_ideal)
print('your ideal monthly expenses are: ', vc_ideal)
print('your ideal yearly spending is: ', spending_ideal)
print('your ideal yearly savings are: ', savings_ideal)


net_new = net_income
gross_new = gross_income_1


#checking if user is living within their means

rent_monthly = float(input('Input rent: '))

rent_yr = rent_monthly *12

food_expense = float(input('Input weekly food cost: '))

car = str(input('Do you have a car: '))

savings = float(input('How much do you save per year: '))


if car == 'yes':
    car_expense_monthly = 120
else:
    car_expense_monthly = 0

if car == 'yes':
    gas_monthly = 60
else:
    gas_monthly =0

utilities = float(input('Input total utility expenses: '))
total_expenses = car_expense_monthly + gas_monthly + food_expense*52 + rent_yr + utilities
monthyl_expenses = total_expenses/12

#feedback for rent cost
if rent_monthly > rent_cost_ideal:
    difference = rent_monthly - rent_cost_ideal
    print('you are over paying rent by: ', difference)
elif rent_monthly==rent_cost_ideal:
    difference =0
    print('you are matching your ideal rate ')
elif rent_monthly< rent_cost_ideal:
    difference = rent_cost_ideal-rent_monthly
    print('you can afford to pay this much more in rent: ', difference)


#feedback for expenses


if total_expenses> vc_ideal:
    dif = monthyl_expenses-vc_ideal
    print('your expenses are too high:', dif)
elif monthyl_expenses==vc_ideal:
    dif = 0
    print('your expenses are matching: ')
elif monthyl_expenses<vc_ideal:
    dif = vc_ideal-total_expenses
    print('you are below budget for expenses by: ', dif)


#feedback for savings


if savings>savings_ideal:
    different = savings-savings_ideal
    print('you are saving above your goal by: ', different)
elif savings==savings_ideal:
    different = 0
    print('you are saving correctly: ')
elif savings<savings_ideal:
    different = savings_ideal-savings
    print('you need to save more by: ',different)
















