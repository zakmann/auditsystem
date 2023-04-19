import inquirer

def registration():
    print ("Registration")

def ret_record():
    print ("Retrieve Patient Record")

def ret_auditid():
    print ("Retrieve Auditor Id")

def verification():
    print ("Verification")

def log_info():
    print ("Audit Log Info")


if __name__ == "__main__":

    print ("Secure Decentralized Audit System")
    questions = [
        inquirer.Text("user", message="Please enter your username", validate=lambda _, x: x != "."),
        inquirer.Password("password", message="Please enter your password"),
        inquirer.List(
            "task",
            message="What would you like to do?",
            choices=["Registration", "Retrieve Patient Record", "Retrieve Auditor Id", "Verification", "Audit Log Info", "EXIT"],
        ),
        inquirer.Confirm(
            "correct",
            message="Continue?",
            default=False,
        ),
    ]

    answers = inquirer.prompt(questions)
    print(answers)

    task = answers["task"]
    options = {"Registration" : registration,
               "Retrieve Patient Record" : ret_record,
               "Retrieve Auditor Id" : ret_auditid,
               "Verification" : verification,
               "Audit Log Info": log_info,
               "EXIT": exit }
    options[task]()
               
               

