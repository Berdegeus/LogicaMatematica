## user inputs N propositions, if all true print true 

# user input
n = int(input("Quantas preposições? "))
# create a list of propositions
propositions = []
# for each proposition
for i in range(n):
    # user input
    proposition = input("Valor da proxima proposição: ")
    # add to list
    propositions.append(proposition)

# if all are true
if all(proposition == "true" for proposition in propositions):
    print("true")
# if one is false
else:
    print("false")


               
