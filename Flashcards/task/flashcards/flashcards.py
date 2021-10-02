print("Input the number of cards:")
number_of_cards = int(input())

flashcards = []
for card_number in range(1, number_of_cards + 1):
    print(f"The term for card #{card_number}:")
    term = input()
    print(f"The definition for card #{card_number}:")
    definition = input()
    flashcards.append([term, definition])

for flashcard in flashcards:
    print(f'Print the definition of "{flashcard[0]}":')
    answer = input()
    if answer == flashcard[1]:
        print("Correct!")
    else:
        print(f'Wrong. The right answer is "{flashcard[1]}".')
