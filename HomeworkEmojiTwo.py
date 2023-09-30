def main():
smiled_str = input('Enter a string with emoji: ')
smile_dict = {}

for smile in smiled_str:
    if smile not in smile_dict:
        smile_dict[smile] = 1
    else:
        smile_dict[smile] += 1

print('Number of each emoji:')
for key, value in smile_dict.items():
    print(f'{key} - {value}')
if name == "main":
main()