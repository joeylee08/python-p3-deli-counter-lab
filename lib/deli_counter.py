katz_deli = []

def line(katz_deli : list):
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:
        prefix = "The line is currently: "
        suffix = " ".join([f"{katz_deli.index(person) + 1}. {person}" for person in katz_deli])
        print(prefix + suffix)
    
def take_a_number(katz_deli : list, person):
    katz_deli.append(person)
    print(f"Welcome, {person}. You are number {katz_deli.index(person) + 1} in line.")


def now_serving(katz_deli: list):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        person = katz_deli.pop(0)
        print(f"Currently serving {person}.")
