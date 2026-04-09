from colorama import init, Fore, Style

# Initialize colorama for Windows
init(autoreset=True)

def print_success(message):
    print(Fore.GREEN + message)

def print_warning(message):
    print(Fore.YELLOW + message)

def print_error(message):
    print(Fore.RED + message)

def print_info(message):
    print(Fore.CYAN + message)

def print_header(message):
    print(Fore.CYAN + Style.BRIGHT + message)

def colored_message(status, message):
    if message.startswith("✅"):
        print_success(message)
    elif message.startswith("⚠️"):
        print_warning(message)
    elif message.startswith("❌"):
        print_error(message)
    else:
        print_info(message)