from logging import raiseExceptions
import pickle

Ask = input('Enter "N" for new model and "O" for old: ')
if Ask == 'N':
    neurons = [0 for x in range(400)]
elif  Ask == 'O':
    with open('neurons.pickle', 'rb') as f:
        neurons = pickle.load(f)
else:
    raise Exception('incorent answer for question "Enter "N" for new model and "O" for old"')
ExitCondition = False
while not ExitCondition:
    NextCommand = input('Enter command(enter "help" for help): ')
    if NextCommand == 'help':
        pass
    if NextCommand == 'exit':
        ExitCondition = True

