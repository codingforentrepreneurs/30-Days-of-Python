from datetime import date

names = ["Justin", "john", "Emilee", "Jim", "Ron", "Sandra", "veronica", "Whitney"]
amounts = [123.32, 94.23, 124.32, 323.4, 23, 322.122323, 32.4, 99.99]
message = """Hi {name}! 

                Thank you for the purchase on {date}. 
                We hope you are exicted about using it. Just as a
                reminder the purcase total was ${amount}
                Have a great one!

                Team CFE
                """

def format_messages(names, amounts, message):

        the_date = date.today().strftime("%d/%m/%Y")

        formatted_messages = []

        index = 0

        for index in range(0, len(names)):

                name = names[index]
                amount = "%.2f" % (amounts[index])

                formatted_message = message.format(
                        name=name[0].upper()+name[1:].lower(),
                        date=the_date,
                        amount=amount)

                index += 1

                formatted_messages.append(formatted_message)

                print(formatted_message)

        return formatted_messages

format_messages(names,amounts, message)