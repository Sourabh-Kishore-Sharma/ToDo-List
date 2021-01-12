import sys
import datetime


#Function to print the CLI usage
def menu():
    return print("""Usage :-
    $ ./todo add "todo item"  # Add a new todo
    $ ./todo ls               # Show remaining todos
    $ ./todo del NUMBER       # Delete a todo
    $ ./todo done NUMBER      # Complete a todo
    $ ./todo help             # Show usage
    $ ./todo report           # Statistics""")


#Function to add a new todo
def add(text):
    with open("todo.txt","a") as file:
        file.write(text+"\n")
    return print("Added todo: \"{}\"".format(text))


#Function to print all the pending todo
def ls():
    with open("todo.txt","r") as file:
        lines=file.readlines()
        line_num=len(lines)
        for line in reversed(lines):
            print("[{}] {}".format(line_num,line),end="")
            line_num-=1


#Function to generate report.i.e Number of pending & completed todo.
def report():
    pending=0
    completed=0
    date=datetime.datetime.today().strftime('%d/%m/%Y')
    try:
        with open("todo.txt","r") as file:
            lines=file.readlines()
            pending=len(lines)
    except:
        pass
    try:
        with open("done.txt","r") as file:
            lines=file.readlines()
            completed=len(lines)
    except:
        pass
    return print("{} Pending : {} Completed : {}".format(date,pending,completed))


#Function to make a todo task done
def done(i):
    with open("todo.txt","r") as file:
        lines=file.readlines()
    original=int(i)-1
    removed_todo=lines.pop(original)
    with open("todo.txt","w") as file:
        file.write("".join(lines))
    with open("done.txt","a") as file:
        date=datetime.datetime.today().strftime('%d/%m/%Y')
        file.write("x "+date+" "+removed_todo)
    return print("Marked todo #{} as done.".format(i))


#Function to delete a todo task.
def delete(i):
    with open("todo.txt","r") as file:
        lines=file.readlines()
    original=int(i)-1
    removed_todo=lines.pop(original)
    with open("todo.txt","w") as file:
        file.write("".join(lines))
    return print("Deleted todo #{}".format(i))


if __name__=="__main__":
    try:
        param=sys.argv[1].lower()
    except:
        menu()
        exit()

    if param == "help":
        menu()
    elif param == "add":
        text=sys.argv[2]
        add(text)
    elif param == "ls":
        ls()
    elif param == "report":
        report()
    elif param == "done":
        i=sys.argv[2]
        done(i)
    elif param == "del":
        i=sys.argv[2]
        delete(i)
    else:
        menu()
