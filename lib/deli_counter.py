katz_deli = []

def line(person_in_line):
    lines_added = []

    for index in range(len(person_in_line)):
        lines_added.append(f"{index + 1}. {person_in_line[index]}")

    if lines_added:
        print("The line is currently: " + ' '.join(lines_added))
    else: 
        print("The line is currently empty.")

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    position = len(katz_deli)
    print(f"Welcome, {name}. You are number {position} in line.")

def now_serving(katz_deli):
    if katz_deli:
        serving_person = katz_deli.pop(0)
        print(f"Currently serving {serving_person}.")
    else:
        print("There is nobody waiting to be served!")