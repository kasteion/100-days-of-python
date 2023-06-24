
with open("./input/letters/starting_letter.txt") as letter:
    letter_format = letter.read()

with open("./input/names/invited_names.txt") as names:
    for name in names:
        new_letter = letter_format.replace("[name]", name.strip())
        with open(f"./output/ready_to_send/letter_to_{name.strip().lower()}.txt", mode="w") as letter:
            letter.write(new_letter)
