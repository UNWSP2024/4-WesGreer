# Movie Ticket Program
# written by Wesley Greer on 2/12/2026

def main():
    ######################
    tickets = 0

for m in range(5):
    movie = input('What is a movie you would like to see in theatre? ')
    extra_tix = float(input('How many tickets would you like for this movie? '))
    if extra_tix < 0:
        print('Error: Please enter a valid number of tickets')
        extra_tix = int(input("How many tickets would you like for this movie? "))
    else: pass
    tickets += extra_tix
print("Your total number of tickets is:", tickets)
    ######################


if __name__ == '__main__':
    main()
