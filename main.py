from Frontend.QueryExecuter import QueryExecuter

local_vars = {}

def handle_command(command):
    try:
        # here is the point where we write our code
        result = QueryExecuter.execute(command,local_vars)
        if result is not None:
            print(result)
    except Exception as e:
        print("Error:", str(e))

# Start the REPL
def start_repl():
    print("Welcome to Ak-Lite Database !!")
    while True:
        command = input("db >>> ")
        if command == "exit":
            break
        handle_command(command)

if __name__ == "__main__":
    start_repl()

