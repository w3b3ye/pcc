prompt = "\nPlease enter the name of a city."
prompt += "\nEnter 'quit' when you finished."

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"\nI would love to go to {city.title()}!")