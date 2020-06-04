print("Exceptions can be caught using a try-except block")

thinkers = ["Plato", "PlayDo", "Gumby"]
while True:
    try:
        thinker = thinkers.pop()
        print(thinker)
    except IndexError as e:
        print(e)
        break
