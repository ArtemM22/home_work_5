from typing import Dict, Callable

# Декоратор для обробки помилок введення користувача
def input_error(func: Callable):
   
   # Декоратор для обробки помилок введення користувача
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
        except KeyError:
            return "Contact not found."
    return inner


@input_error
def add_contact(args: list, contacts: Dict[str, str]) -> str:
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args: list, contacts: Dict[str, str]) -> str:
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args: list, contacts: Dict[str, str]) -> str:
    name = args[0]
    return f"{name}: {contacts[name]}"


@input_error
def show_all(_: list, contacts: Dict[str, str]) -> str:
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def parse_input(user_input: str):
    try:
        parts = user_input.split()
        command = parts[0].lower()
        args = parts[1:]
        return command, args
    except IndexError:
        return "", []


def main():
    contacts = {}
    commands = {"add": add_contact, "change": change_contact, "phone": show_phone, "all": show_all,}

    while True:
        user_input = input("Enter a command: ")

        if user_input.lower() in ("exit", "close", "bye"):
            print("Good bye!")
            break

        command, args = parse_input(user_input)

        if command in commands:
            result = commands[command](args, contacts)
            print(result)
        else:
            print("Unknown command.")

        if not command:
            print("Enter a command.")
            continue

if __name__ == "__main__":
    main()