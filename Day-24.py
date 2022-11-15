def minion_game(string):
    # your code goes here
    score = {'Stuart': 0, 'Kevin': 0}
    string_len = len(string)

    for i in range(string_len):
        if string[i] not in "aeiouAEIOU":
            score['Stuart'] += (string_len-i)
        else:
            score['Kevin'] += (string_len-i)

    if score['Stuart'] > score['Kevin']:
        print(f"Stuart {score['Stuart']}")
    elif score['Stuart'] < score['Kevin']:
        print(f"Kevin {score['Kevin']}")
    else:
        print('Draw')
if __name__ == '__main__':
    s = input()
    minion_game(s)