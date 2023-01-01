# In a group of 23 people, there is a 50.7% chance that two people will share a birthday date.
# If we take pairs of people, then one person can pair with 22 other, the second person can pair with 21 other people,
# not including the last person.
from Sources import CommonNames

CMN_NAMES = list(CommonNames.get_csv_names())  # set of all names in commonNames.csv file; contains 447055 names.
people = [i for i in range(23)]  # change later the people to random names


# print(people)
def ran_ppl(num_of_ppl: int):
    """
    The function receives number of people to run, and selects randomly from the master list.
    @param num_of_ppl: Number of people to be checked.
    @return: a list of n people chosen randomly
    """
    from random import randint
    chosen_ppl = set()  # The returned set of names randomly chosen.
    random_numbers = list()  # A list to keep track of chosen random numbers
    for i in range(num_of_ppl):
        ran_num = randint(0, len(CMN_NAMES) - 1)  # Choose a random number from 0 to the length of the names list.
        while ran_num in random_numbers:  # if this number has been pulled:
            ran_num = randint(0, len(CMN_NAMES) - 1)  # skip and later draw another random number
        else:
            random_numbers.append(ran_num)
            name = CMN_NAMES[ran_num].lower()
            name = name.title()  # style the name to be lowercase and Titled.
            chosen_ppl.add(name)  # adds the fixed name to the set of chosen people.
    # print(chosen_ppl)
    # print(len(chosen_ppl))
    return chosen_ppl


def assign_birthdays(ppl: set):
    """
    Assigns a random date (dob) for each man in people list.
    @param ppl: List (or set) of people to assign birthdays to.
    @return: Dict of ppl name as keys and dob as values.
    """
    import datetime
    import random
    # year, month, day
    # print(datetime(1, 12, 31))
    birthdays = dict()
    for dude in ppl:
        month = random.randint(1, 12)
        if month == 2:  # February
            day = random.randint(1, 28)
        elif month in [4, 6, 9, 11]:  # if month has 30 days.
            day = random.randint(1, 30)
        else:  # January, March, May
            day = random.randint(1, 31)
        bd = datetime.date(1600, month, day)  # we assume its a leap year for ease of calculation.
        bd_formatted = datetime.date.strftime(bd, "%d %B")  # formats the date to words; outputs str
        # print(bd_formatted)
        # print(type(bd_formatted))
        birthdays[dude] = bd_formatted
    print(birthdays)
    return birthdays


def bd_ppl_print(bds: dict):
    """
    Receives a dict of birthdays, converts to list of dicts, sorts the list by date, prints in tabular format name
    and dob.
    @param bds: Dictionary of name as key and dob as value.
    @return: function's purpose is to print; returns None.
    """
    from Sources import style
    import datetime
    listed_bds = list()
    for key, value in bds.items():
        listed_bds.append({"Name": key, "DOB": value})  # converting the dict to list of dict for ease of sorting.
    listed_bds.sort(key=lambda x: datetime.datetime.strptime(x['DOB'], '%d %B'))  # sorts the list of dicts by date.
    print(listed_bds)
    # receives the dict from assign_birthdays func and prints the bds in a tabular, clean format.
    print(style.Colors.BOLD + style.Colors.BLUE + f'{"Human Name":<20} |\t {"Birthday":<20} {"|":<20}' +
          style.Colors.END)  # title
    for i in listed_bds:  # for every dict in the ordered listed dictionaries.
        for v in i.values():  # for every value in a dictionary
            print(f'{v:<20}', end=" |\t ")  # prints the name and dob sorted by date, in a tabular format.
        print()  # prints a newline for formatting


def create_pairs(ppl: set):
    """
    Function creates pairs of people in ppl list. i.e. for 23 people, the function will pair human 0 with humans 1-23,
    human 1 with humans 2-23, and so on..
    @param ppl: Set of people to create pairs from.
    @return: Dict of people and their pairs.
    """
    pairs = dict()
    # i_pairs = [i for i in range(1, len(ppl))]  # List comprehension in the size of the ppl list.
    ppl_to_pair = list(ppl)  # convert the ppl set to list, so it could be indexed.
    ppl_to_pair = ppl_to_pair[1:]  # choose the list from the second index to the end.
    man_pairs = [man for man in ppl_to_pair]  # List comprehension in the size of the ppl list, minus the first one.
    pairs_sum = 0  # the sum of possible pairs; result should be 253 for 23 ppl.
    for man in ppl:  # for each people in the people's list
        pairs[man] = list(man_pairs)
        pairs_sum += len(pairs[man])
        # print(man, "len is", len(pairs[man]))
        if len(pairs[man]) == 0:
            continue
        man_pairs.pop(0)
    print(pairs)
    print("There are", pairs_sum, "pairs.")
    return pairs


def match_bds(bds: dict, pairs: dict):
    """
    Finds people with the same dob from dict of pairs.
    Function wasn't tested if 3 or more people share a dob, probably will not find well since it works with pairs, and
    it is not the idea behind the birthday paradox.
    @param bds: Dict of people and their dob (suggested from assign_birthdays func).
    @param pairs: Dict of people and their pairs (suggested from create_pairs func).
    @return: Prints results and returns dict of people and their matches; dob as key and list of people sharing the dob
    in a list.
    """
    matching_bds = dict()
    for human in pairs.items():
        for pair in human[1]:  # for each pair in the list of the pairs;
            if bds[human[0]] == bds[pair]:  # if the birthday of the first human is paired with the second human's bd.
                print(f'{human[0]} is sharing a birthday with {pair} on {bds[human[0]]}.')
                print(f'{human[0]}\'s birthday is on {bds[human[0]]}.')
                print(f'{pair}\'s birthday is on {bds[pair]}.')
                matching_bds[bds[human[0]]] = [human[0], pair]
    return matching_bds


def successful_pairs(matching_bds: dict, num_of_ppl: int):
    """
    If matching birthdays were found, function prints how much were found out of total number of people checked.
    @param matching_bds: Dict of matching bds (suggested from match_bds func).
    @param num_of_ppl: Number of people in ppl list (known as n in computations.
    @return: Currently just prints, might add statistical data in the future.
    """
    # function should see how many values are in the successful pairs dictionary, and justify the statistics.
    num_results = len(matching_bds.keys())
    if num_results > 0:
        print(f'I have found {num_results} pair out of {num_of_ppl} people.')
    # add statistics data


def probability(total_days=365, num_of_ppl=23):
    from Sources import style
    import math
    n = total_days
    k = num_of_ppl
    try:
        v_nr = (math.factorial(n)) / (math.factorial(n - k))
    except OverflowError:  # If number is too large for python to calculate.
        return None  # Cannot calculate due to large number.
    except ValueError:  # factorial() not defined for negative values
        return None  # Cannot calculate due to negative factorial.
    v_t = n ** k
    p_a = v_nr / v_t
    p_b = 1 - p_a
    print("Chances two pairs will" + style.Colors.BOLD + " not " + style.Colors.END + "share a birthday: ", end="")
    print(f'{p_a:.3%}')
    print("Chances two pairs will share a birthday: ", end="")
    print(f'{p_b:.3%}')
    return p_b


def num_ppl():
    num_of_ppl = int(input("Enter the amount of people you'd like to manually enter: "))
    while type(num_of_ppl) != int or num_of_ppl <= 0:
        num_of_ppl = int(input("Error, please enter a valid number: "))
    return num_of_ppl


def choose_name():
    # should choose 1 people each time
    # .
    name = input('Choose human name: ')
    # check input?
    return name


def choose_bdd():
    print("Enter the date of birth in DD MMMM format.")
    print("For example, 02 February")
    bdd = input(">>> ")
    # write a check for input
    return bdd


def choose_people(num_of_ppl: int):
    ppl = dict()
    for man in range(num_of_ppl):
        name = choose_name()
        bdd = choose_bdd()
        ppl[name] = bdd
    return ppl


def choose_mode():
    print('Please choose code running mode, with a number between 1 and 3.')
    print('1. Auto Mode - the machine chooses random people and assigns random birthdates.')
    print('2. Manual Mode - you will choose 23 people and assign their birthdates; csv file can be chosen as well.')
    print('3. Semi Mode - you will choose a number of people, the machine will choose the rest.')

    mode = int(input('>>> '))
    while type(mode) != int or mode not in [1, 2, 3]:
        mode = int(input('Error, please choose a number between 1 and 3.'))

    # update later to switch and case
    if mode == 1:
        # run Auto mode, call auto function
        print("You've chosen Automatic Mode.")
    elif mode == 2:
        # Manual mode
        print("You've chosen Manual Mode.")
        usr_csv = use_csv()  # Checks if user has a csv to upload
        manual_ppl = dict()
        if usr_csv == False:  # if user doesnt have csv file
            num_of_ppl = num_ppl()
            ppl = choose_people(num_of_ppl)
            print(ppl)
        else:  # if user have a csv file
            manual_ppl = usr_csv()
    elif mode == 3:
        # semi mode
        print("You've chosen Semi Mode.")
        print(
            "You will enter manually the number of people you'd like to check, and the machine would check the rest, up until 23.")
        num_of_ppl = num_ppl()
        ppl = choose_people(num_of_ppl)
        print(ppl)
        auto_runs = 23 - num_of_ppl
        # write code here to let the machine run the random code for auto_runs times.


# choose_mode() - check me


def bdd_csv():
    import csv
    print("Please make sure your first column is people's name and the second column is their birthdate, "
          "in the following format: ")
    print("DD MMMM; i.e. - 02 February./n/n")
    print("Please move the CSV file to the same folder with this code.")
    f_name = input("Please enter the file name without extension: ")
    # run check here for extension
    f_name += ".csv"
    print("Is there a header in your file?")
    print("Enter 1 if there is a header.")
    print("Enter 0 if there is no header.")
    hdr = int(input(">>> "))
    while type(hdr) != int or hdr not in [0, 1]:
        hdr = int(input("Please enter a valid answer, between 0 and 1: "))
    with open(f_name) as f_manual_names:
        f_reader = csv.reader(f_manual_names, delimiter=',')
    line = 0
    f_ppl = dict()
    for row in f_reader:
        if hdr == 1 and row == 0:  # if the first line is header
            # print(f'Header: {", ".join(row)}')
            # ignore the header
            line += 1
        elif hdr == 1 and row != 0:
            f_ppl[row[0]] = row[1]
        else:  # if there is no header
            # print(row[0])
            f_ppl[row[0]] = row[1]  # adds name as key and bdd as value to dict
            line += 1

    return f_ppl


# bdd_csv() - check me


def use_csv():
    print("Do you want to upload a csv file?")
    print("Enter 0 for No, and 1 for Yes.")
    csv_exist = int(input(">>> "))
    while type(csv_exist) != int or hdr not in [0, 1]:
        csv_exist = int(input("Please enter a valid answer, between 0 and 1: "))
    if csv_exist == 0:
        return False
    elif csv_exist == 1:
        return bdd_csv()


def main():
    # create an if statement to check if user wants to enter manually people with dates or let the machine run auto.
    num_of_ppl = num_ppl()
    ppl = ran_ppl(num_of_ppl=num_of_ppl)
    bds = assign_birthdays(ppl)
    bd_ppl_print(bds)
    pairs = create_pairs(ppl)
    matching_bds = match_bds(bds=bds, pairs=pairs)
    probability(num_of_ppl=num_of_ppl)
    print("\n\n-----------------------------------")
    successful_pairs(matching_bds=matching_bds, num_of_ppl=num_of_ppl)


if __name__ == "__main__":
    main()
