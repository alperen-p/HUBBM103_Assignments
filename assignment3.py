import os
import sys
alphabet_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] #I use alphabet letter list for row names
stadium_data = {} #I use this dict for data. Each key has 2d list value. So ı can reach all data easily 

reading_file = sys.argv[1]
global data #I declared data as global so ı can reach input.txt at end of the script.
with open(reading_file, "r", encoding='utf-8') as f:	 
    data = f.readlines()
        
current_dir_path = os.getcwd()
writing_file_name = "output.txt"
writing_file_path = os.path.join(current_dir_path, writing_file_name)
global output
output = open(writing_file_path,"w",encoding='utf-8')

#We can create seats that have row and column using this function
def create_category(category_name, number_of_rows, number_of_columns):
    if category_name not in stadium_data:
        data_element = [['X' for j in range(number_of_columns)] for i in range(number_of_rows)] #I use list compherension for 2d list. 
        stadium_data[category_name] = data_element
        print("The category '{}' having {} seats has been created".format(category_name,number_of_rows*number_of_columns))
        output.write("The category '{}' having {} seats has been created\n".format(category_name,number_of_rows*number_of_columns))
    else:
        print("Warning: Cannot create the category for the second time. The stadium has already {}".format(category_name))
        output.write("Warning: Cannot create the category for the second time. The stadium has already {}\n".format(category_name))

#We can sell ticket with some parameter using this function 
def sell_ticket(customer_name, state_of_seat, category_name, seat_info):
    try: #I use try catch exception to catch index exception if customer select wrong place out of range. I throw except message
        if("-" not in seat_info):
            data_values = stadium_data[category_name]
            if(data_values[int(alphabet_letter.index(seat_info[0:1]))][int(seat_info[1:])] == "X"):
                if(state_of_seat == "full"):
                    data_values[int(alphabet_letter.index(seat_info[0:1]))][int(seat_info[1:])] = "F" # F is full ticket
                    stadium_data[category_name] = data_values
                elif(state_of_seat == "student"):
                    data_values[int(alphabet_letter.index(seat_info[0:1]))][int(seat_info[1:])] = "S" # S is student ticket
                    stadium_data[category_name] = data_values
                elif(state_of_seat == "season"):
                    data_values[int(alphabet_letter.index(seat_info[0:1]))][int(seat_info[1:])] = "T" # T is season ticket
                    stadium_data[category_name] = data_values
                print("Success: {} has bought {} at {}".format(customer_name, seat_info, category_name))
                output.write("Success: {} has bought {} at {}\n".format(customer_name, seat_info, category_name))
            else:
                print("Warning: The seat {} cannot be sold to {} since it was already sold!".format(seat_info, customer_name))
                output.write("Warning: The seat {} cannot be sold to {} since it was already sold!\n".format(seat_info, customer_name))
        else:
            data_values = stadium_data[category_name]
            isEmpty = True
            for i in range(int(seat_info[1:seat_info.index("-")]), int(seat_info[seat_info.index("-")+1:])+1):
                if(data_values[int(alphabet_letter.index(seat_info[0:1]))][i] == "X"):
                    continue
                else:
                    isEmpty = False
                    print("Warning: The seats {} cannot be sold to {} due some of them have already been sold!".format(seat_info, customer_name))
                    output.write("Warning: The seats {} cannot be sold to {} due some of them have already been sold!\n".format(seat_info, customer_name))
                    break
            if(isEmpty == True):
                print("Success: {} has bought {} at {}".format(customer_name, seat_info, category_name))
                output.write("Success: {} has bought {} at {}\n".format(customer_name, seat_info, category_name))
                for i in range(int(seat_info[1:seat_info.index("-")]), int(seat_info[seat_info.index("-")+1:])+1):
                    if(state_of_seat == "full"):
                        data_values[int(alphabet_letter.index(seat_info[0:1]))][i] = "F"
                        stadium_data[category_name] = data_values
                    elif(state_of_seat == "student"):
                        data_values[int(alphabet_letter.index(seat_info[0:1]))][i] = "S"
                        stadium_data[category_name] = data_values
                    elif(state_of_seat == "season"):
                        data_values[int(alphabet_letter.index(seat_info[0:1]))][i] = "T"
                        stadium_data[category_name] = data_values
    except IndexError:
        data_values = stadium_data[category_name]
        if("-" not in seat_info):
            if((int(alphabet_letter.index(seat_info[0:1])) > len(data_values)) and (int(seat_info[1:]) > len(data_values[0]))):
                print("Error: The category {} has less row and column than the specified index {}!".format(category_name, seat_info))
                output.write("Error: The category {} has less row and column than the specified index {}!\n".format(category_name, seat_info))
            else:
                if(int(alphabet_letter.index(seat_info[0:1])) > len(data_values)):
                    print("Error: The category {} has less row than the specified index {}!".format(category_name, seat_info))
                    output.write("Error: The category {} has less row than the specified index {}!\n".format(category_name, seat_info))
                elif(int(seat_info[1:]) > len(data_values[0])):
                    print("Error: The category {} has less column than the specified index {}!".format(category_name, seat_info))
                    output.write("Error: The category {} has less column than the specified index {}!\n".format(category_name, seat_info))
        else:
            if((int(alphabet_letter.index(seat_info[0:1])) > len(data_values)) and (int(seat_info[seat_info.index("-")+1:]) > len(data_values[0]))):
                print("Error: The category {} has less row and column than the specified index {}!".format(category_name, seat_info))
                output.write("Error: The category {} has less row and column than the specified index {}!\n".format(category_name, seat_info))
            else:
                if(int(alphabet_letter.index(seat_info[0:1])) > len(data_values)):
                    print("Error: The category {} has less row than the specified index {}!".format(category_name, seat_info))
                    output.write("Error: The category {} has less row than the specified index {}!\n".format(category_name, seat_info))
                elif(int(seat_info[seat_info.index("-")+1:]) > len(data_values[0])):
                    print("Error: The category {} has less column than the specified index {}!".format(category_name, seat_info))
                    output.write("Error: The category {} has less column than the specified index {}!\n".format(category_name, seat_info))

# We can cancel ticket using this function
def cancel_ticket(category_name, seat_info):
    try:
        data_values = stadium_data[category_name]
        if(data_values[int(alphabet_letter.index(seat_info[0:1]))][int(seat_info[1:])] != "X"):
            data_values[int(alphabet_letter.index(seat_info[0:1]))][int(seat_info[1:])] = "X"
            stadium_data[category_name] = data_values
            print("Success: The seat {} at '{}' has been canceled and now ready to sell again".format(seat_info, category_name))
            output.write("Success: The seat {} at '{}' has been canceled and now ready to sell again\n".format(seat_info, category_name))
        else:
            print("Error: The seat {} at '{}' has already been free! Nothing to cancel".format(seat_info, category_name))
            output.write("Error: The seat {} at '{}' has already been free! Nothing to cancel\n".format(seat_info, category_name))
    except IndexError as ex:
        print("Error: The category '{}' has less column than the specified index {}!".format(category_name, seat_info))
        output.write("Error: The category '{}' has less column than the specified index {}!\n".format(category_name, seat_info))

# We can use this function to learn total earning money
def balance(category_name):
    data_values = stadium_data[category_name]
    sum_of_students = 0
    sum_of_full = 0
    sum_of_season = 0
    for i in range(len(data_values)):
        for j in range(len(data_values[i])):
            if(data_values[i][j] == "F"):
                sum_of_full += 1
            if(data_values[i][j] == "S"):
                sum_of_students += 1
            if(data_values[i][j] == "T"):
                sum_of_season += 1
    print("Category report of '{}'".format(category_name))
    output.write("Category report of '{}'\n".format(category_name))
    print("-"*(21 + len(category_name)))
    output.write("-"*(21 + len(category_name)))
    output.write("\n")
    print("Sum of students = {}, Sum of full pay = {}, Sum of season ticket = {}, and Revenues = {} Dollars".format(sum_of_students, sum_of_full, sum_of_season, (sum_of_students*10 + sum_of_full*20 + sum_of_season*250)))
    output.write("Sum of students = {}, Sum of full pay = {}, Sum of season ticket = {}, and Revenues = {} Dollars\n".format(sum_of_students, sum_of_full, sum_of_season, (sum_of_students*10 + sum_of_full*20 + sum_of_season*250)))        

# We can use this function for show layout of tribun
def show_category(category_name):
    data_values = stadium_data[category_name]
    print("Printing category layout of {}".format(category_name))
    output.write("Printing category layout of {}\n".format(category_name))
    for i in range(len(data_values), 0, -1):
        print("{:<2}".format(alphabet_letter[i-1]), end="")
        output.write("{:<2}".format(alphabet_letter[i-1]))
        for state_of_seat in data_values[i-1]:
            print("{:<3}".format(state_of_seat), end="")
            output.write("{:<3}".format(state_of_seat))
        print("")
        output.write("\n")
    for k in range(len(data_values[0])):
        print("{:>3}".format(k), end="")
        output.write("{:>3}".format(k))
    print("")
    output.write("\n")

# Here i read input.txt and i call function looking first command
for line in data:
    command = line.split()
    if(command[0] == "CREATECATEGORY"):
        category_name = command[1]
        multiple_rows_and_columns = command[2].replace("\n","")
        number_of_rows = int(multiple_rows_and_columns[0:multiple_rows_and_columns.index("x")])
        number_of_columns = int(multiple_rows_and_columns[multiple_rows_and_columns.index("x")+1:])
        create_category(category_name, number_of_rows, number_of_columns)
    if(command[0] == "SELLTICKET"):
        customer_name = command[1]
        state_of_seat = command[2]
        category_name = command[3]
        command[-1] = command[-1].replace("\n","")
        i=4
        while(i < len(command)):
            seat_info = command[i]
            sell_ticket(customer_name, state_of_seat, category_name, seat_info)
            i+=1
    if(command[0] == "CANCELTICKET"):
        category_name = command[1]
        command[-1] = command[-1].replace("\n","")
        i=2
        while(i < len(command)):
            seat_info = command[i]
            cancel_ticket(category_name, seat_info)
            i+=1
    if(command[0] == "BALANCE"):
        category_name = command[1].replace("\n","")
        balance(category_name)
    if(command[0] == "SHOWCATEGORY"):
        category_name = command[1].replace("\n","")
        show_category(category_name)

output.close()
# Alperen Polat 2210356112