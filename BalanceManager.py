from collections import defaultdict

def get_command_results(commands):
    banks = defaultdict(set) # map bank to users
    balances = defaultdict(int) # map user to balances

    for command in commands:
        t = command[0]
        if t == "INIT":
            usr, balance = commands[1], command[2]
            # set balance
            balances[usr] = balance
            for bank in commands[2:]:
                banks[bank].add(usr)

        
    
