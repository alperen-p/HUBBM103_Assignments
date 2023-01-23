#Alperen Polat 2210356112
import os

patients_list = [] #This list contains my patients information
patients_name_list = [] #I created this list because ı wanted to reach patients_list argument easily. Example: when i call the Recommendation Hayriye I can control easily hayriye is in list or not. Again if hayrise is in list I can easily reach where is hayriye index in patients_list. 

def input_file():
    current_dir_path = os.getcwd()
    reading_file_name = "doctors_aid_inputs.txt"
    reading_file_path = os.path.join(current_dir_path, reading_file_name)
    global data
    with open(reading_file_path, "r", encoding='utf-8') as f:	 
        data = f.readlines()

input_file()

def output_file():
    current_dir_path = os.getcwd()
    writing_file_name = "doctors_aid_outputs.txt"
    writing_file_path = os.path.join(current_dir_path, writing_file_name)
    global output
    output = open(writing_file_path,"w",encoding='utf-8')

output_file()


def create(patient_name, diagnosis_accuracy, disease_name, disease_incidence, treatment_name, treatment_risk):
    if(patients_name_list.count(patient_name) != 0):
        return f"Patient {patient_name} cannot be recorded due to duplication."
    else:
        patients_list.append([patient_name, diagnosis_accuracy, disease_name, disease_incidence, treatment_name, treatment_risk])
        patients_name_list.append(patient_name)
        return f"Patient {patient_name} is recorded."



def remove(patient_name):
    if(patients_name_list.count(patient_name) != 0):
        patients_list.remove(patients_list[patients_name_list.index(patient_name)])#Like this. I controlled that name is in patient_name_list without iteration. If name is in list, I reached where is name in patients_list easily. So ı used patients_name_list.  
        patients_name_list.remove(patients_name_list[patients_name_list.index(patient_name)])
        return f"Patient {patient_name} is removed."
    else:
        return f"Patient {patient_name} cannot be removed due to absence."

#At the below function. I arranged number in format function like your output.txt. For example i setted first format bracket 8. This means 2 tab is here. 16 is 4 tab etc.   
def list():
    column ="{:<8}{:<12}{:<16}{:<12}{:<16}{}\n{:<8}{:<12}{:<16}{:<12}{:<16}{}".format("Patient","Diagnosis", "Disease", "Disease", "Treatment", "Treatment", "Name", "Accuracy", "Name", "Incidence", "Name", "Risk")
    output.write(column+"\n")
    output.write("-"*73+"\n") # 73 is length of one line
    for patient in patients_list:
        output.write("{:<8}{:.2f}%\t    {:<16}{:<12}{:<16}{:.0f}%\n".format(patient[0], float(patient[1])*100, patient[2], patient[3], patient[4], float(patient[5])*100)) #There is 4 space gap in string. Because if i use \t there. Windows txt application guess 8 blank but Mac guess 4 blank so I used 4 spaces just there. 


def probability(patient_name):
    if(patients_name_list.count(patient_name) != 0):
        diagnosis_accuracy = float(patients_list[patients_name_list.index(patient_name)][1])
        disease_indicence_list = patients_list[patients_name_list.index(patient_name)][3].split("/")
        disease_indicence_first_element = int(disease_indicence_list[0])
        disease_indicence_second_element = int(disease_indicence_list[1])
        global probability_value #I use global term because I don't want to calculate probability value in recommendation() function again. 
        probability_value = (disease_indicence_first_element*diagnosis_accuracy) / (((disease_indicence_second_element-disease_indicence_first_element) * (1-diagnosis_accuracy)) + (disease_indicence_first_element*diagnosis_accuracy)) # This line i used confusion matrix rule (True Positive / (True Positive + False Positive))
        return "Patient {} has a probability of {:g}% having {}.".format(patient_name,round(probability_value*100,2),patients_list[patients_name_list.index(patient_name)][2].lower())
    else:
        return "Probability for {} cannot be calculated due to absence.".format(patient_name)


def recommendation(patient_name):
    if(patients_name_list.count(patient_name) != 0):
        probability(patient_name) # I calculated probability_value calling probability function easily.
        if(probability_value < float(patients_list[patients_name_list.index(patient_name)][5])):
            return "System suggests {} NOT to have a treatment.".format(patient_name)
        else:
            return "System suggests {} to have a treatment.".format(patient_name)
    else:
        return "Recommendation for {} cannot be calculated due to absence.".format(patient_name)


"""
Firstly i splitted list using " " blank because I wanted to reach what is command. After that i splitted list using "," because parameter is written using "," input.txt
Then i removed command from parameter list. Because first parameter element consists command. For example, when ı splitted list using "," the first parameter element is
"create Hayriye" so i removed create command using removeprefix() function. Finally i removed blank that unnecessary in argument using strip() function. 
"""
for line in data:
    command = line.split(" ")
    if(command[0] == "create"):
        parameter_list = line.split(",")
        try:
            output_text = create(parameter_list[0].removeprefix("create").strip(), float(parameter_list[1].strip()), parameter_list[2].strip(), parameter_list[3].strip(), parameter_list[4].strip(), float(parameter_list[5].strip().removesuffix("\n")))
            output.write(output_text)
            output.write("\n")
        except Exception as ex:
            output.write("There are some errors in create() function"+ str(type(ex)) +"\n")
    elif(command[0] == "remove"):
        parameter_list = line.split(" ")
        try:
            output_text = remove(parameter_list[1].removesuffix("\n"))
            output.write(output_text)
            output.write("\n")
        except Exception as ex:
            output.write("There are some errors in remove() function"+ str(type(ex)) +"\n")
    elif(command[0].removesuffix("\n") == "list"):
        list()
    elif(command[0] == "probability"):
        parameter_list = line.split(" ")
        try:
            output_text = probability(parameter_list[1].removesuffix("\n"))
            output.write(output_text)
            output.write("\n")
        except Exception as ex:
            output.write("There are some errors in probability() function" + str(type(ex)) +"\n")
    elif(command[0] == "recommendation"):
        parameter_list = line.split(" ")
        try:
            output_text = recommendation(parameter_list[1].removesuffix("\n"))
            output.write(output_text)
            output.write("\n")
        except Exception as ex:
            output.write("There are some errors in recommendation() function"+ str(type(ex)) +"\n")

output.close()


     



