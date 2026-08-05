states = {"q0", "q1", "q2"}
alphabet = {"a", "b"}

transitions = {
    ("q0", "a"): "q1",
    ("q0", "b"): "q0",
    ("q1", "a"): "q1",
    ("q1", "b"): "q2",
    ("q2", "a"): "q1",
    ("q2", "b"): "q0"
}

initial_state = "q0"
final_states = {"q2"}

string = input("Enter string: ")

current_state = initial_state
valid = True

for symbol in string:
    if symbol not in alphabet:
        valid = False
        break
    current_state = transitions[(current_state, symbol)]

if valid and current_state in final_states:
    print("Accepted")
else:
    print("Rejected")