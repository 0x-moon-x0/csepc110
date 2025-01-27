print ()
print ("In this program, you can look up information about life expectancy from all across the world throughout the years.")
print ()

life_expectancies = []

overall_min_life = 9999999999999
min_life = 9999999999999
overall_max_life = 0
max_life = 0

repeat = "yes"

while repeat.lower() == "yes":

    choice = input ("Would you like to look up a COUNTRY or a YEAR (C/Y)? ")

    if choice.upper() == "C":

        print ()
        search = input ("Enter the country of interest: ")

    elif choice.upper() == "Y":

        print ()
        search = input ("Enter the year of interest: ")

    else:

        print ()
        print ("Please input a valid answer.")

    with open ("life-expectancy.csv") as file:

        next (file)

        for data in file:

            data = data.strip()
            parts = data.split(",")

            country = parts [0]
            year = parts [2]
            life_expectancy = float(parts [3])

        # overall lowest life expectancy worldwide through all times

            if life_expectancy < overall_min_life:

                overall_min_life = life_expectancy
                overall_min_country = country
                overall_min_year = year

            # overall highest life expectancy worldwide through all times

            if life_expectancy > overall_max_life:

                overall_max_life = life_expectancy
                overall_max_country = country
                overall_max_year = year

            if search == year:

                life_expectancies.append(life_expectancy)

                # lowest life expectancy worldwide according to the user's search

                if life_expectancy < min_life:

                    min_life = life_expectancy
                    min_country = country

                # highest life expectancy worldwide according to the user's search

                if life_expectancy > max_life:

                    max_life = life_expectancy
                    max_country = country

                average = sum (life_expectancies) / len (life_expectancies)
            
            elif search.title() == country:

                life_expectancies.append(life_expectancy)

                # lowest life expectancy in the country of request at a specific year

                if life_expectancy < min_life:

                    min_life = life_expectancy
                    min_year = year

                # highest life expectancy in the country of request at a specific year

                if life_expectancy > max_life:

                    max_life = life_expectancy
                    max_year = year

                average = sum (life_expectancies) / len (life_expectancies)

        print ()
        print (f"The overall maximum life expectancy is: {overall_max_life} from {overall_max_country} in {overall_max_year}")
        print (f"The overall minimum life expectancy is: {overall_min_life} from {overall_min_country} in {overall_min_year}")

        if choice.upper() == "C":
            print ()
            print (f"For {search.title()}:") # i kept getting errors when looking up countries that consist of 2+ words, so i changed .capitalize() to .title()
            print ()
            print (f"The average life expectancy through the years was {average:.2f}")
            print (f"The maximum life expectancy was in {max_year} with {max_life}")
            print (f"The minimum life expectancy was in {min_year} with {min_life}")
        
        elif choice.upper() == "Y":
            print ()
            print (f"For the year {search}:")
            print ()
            print (f"The average life expectancy across all countries was {average:.2f}")
            print (f"The maximum life expectancy was in {max_country} with {max_life}")
            print (f"The minimum life expectancy was in {min_country} with {min_life}")
    
    print ()
    repeat = input ("Would you like to look something up once more (yes/no)? ")
    print ()

print ("Goodbye.")