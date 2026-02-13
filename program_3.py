# Average Rainfall Program
# Written by Wesley Greer on 2/13/2026

def main():
    ######################
print('This program will calculate average rainfall over a period of years.')
years = int(input('How many years would you like to calculate for? '))
month_total = 0
for y in range(1, (years + 1)):
    for month in range(1, 13):
        print('How many inches of rainfall were there in year ', y, ', month ', month, "?", sep="")
        month_rain = float(input('Enter Here: '))
        if month_rain < 0:
            print('Please enter a valid number')
            month_rain = float(input('Enter Here: '))
        else: pass
        month_total += month_rain
month_average = month_total / (years * 12)
print('The total number of months is', years * 12)
print('The total rainfall is', month_total, 'inches')
print('The average rainfall per month is', month_average, 'inches per month')
    ######################    


if __name__ == '__main__':
    main()
