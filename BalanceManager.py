from collections import defaultdict

def get_command_results(commands):
    banks = defaultdict(set) # map bank to users
    users = defaultdict(int) # map user to balances
