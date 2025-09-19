with open('Pythonfile.txt', 'r') as file:
    count = sum(1 for line in file)
    print(f'Total number of lines: {count}')