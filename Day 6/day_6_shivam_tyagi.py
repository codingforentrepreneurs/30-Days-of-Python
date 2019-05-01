import datetime
time=datetime.date.today()

default_names = ["Justin", "john", "Emilee", "Jim", "Ron", "Sandra", "veronica", "Whitney"]
default_amounts = [123.32, 94.23, 124.32, 323.4, 23, 322.122323, 32.4, 99.99]
unf_message = """Hi {name}! 
Thank you for the purchase on {date}. 
We hope you are exicted about using it. Just as a
reminder the purcase total was ${total}.
Have a great one!

Team CFE
"""
msg=unf_message.replace("!"," ")
msg1=msg.split()
def capital(msg1):
    text=[]
    j=0
    for i in msg1:
        text.append(i.capitalize())

    return text
text=capital(msg1)
text1=" "
text2=text1.join(text)


def details(names,amount):
     j=0
     for i in names:
             print(text2.format(name=i,date=time,total=amount[j]))
             j=j+1


details(default_names,default_amounts)
