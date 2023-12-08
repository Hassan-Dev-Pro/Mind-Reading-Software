alphabets =str("A   B   C   D\n"
            "E   F   G   H\n"
            "I   J   K   L\n"
            "M   N   O   P\n"
            "Q   R   S   T\n"
            "U   Y   W   X\n"
            "Y   Z")

alph_matrix=[['a','b','c','d'],
             ['e','f','g','h'],
             ['i','j','k','l'],
             ['m','n','o','p'],
             ['q','r','s','t'],
             ['u','y','w','x'],
             ['y','z','','']]
first_round = [[], [], [], [], [], [], [], []]
def starter():
    user_in_len=int(input("So Can you tell me Total letters in your word: "))
    breaker=0
    while breaker<user_in_len:
        user_col_in=int(input(f"Can you tell me your {breaker} letter of the word in Which Column:"))
        if user_col_in==0 or 1 or 2 or 3:
            for row in alph_matrix:
                first_round[breaker].append([row[user_col_in]])

        else:
            print("Wrong Input please Enter Column 0 to 3:>")
        breaker=breaker+1
"""-------------------------------------------------------------------"""
def second_round_display():
    # print('\n')
    for row in first_round:
        for element in row:
            print(element, end='\t|\t')
        print()
"""-------------------------------------------------------------------"""
def second_round():
    result=[]
    final_Guess=""
    print("Round Round\nLet's do one more time ")
    user_in_len = int(input("So Can you tell me Total letters in your word: "))
    breaker = 0
    while breaker < user_in_len:
        user_sec_in = int(input(f"Can you tell me your {breaker} letter of the word in Which Column:"))
        if user_sec_in == 0:
            g = first_round[breaker][user_sec_in]
            result.append(g)
        elif user_sec_in == 1:
            g = first_round[breaker][user_sec_in]
            result.append(g)
        elif user_sec_in == 2:
            g = first_round[breaker][user_sec_in]
            result.append(g)
        elif user_sec_in == 3:
            g = first_round[breaker][user_sec_in]
            result.append(g)
        elif user_sec_in == 4:
            g = first_round[breaker][user_sec_in]
            result.append(g)
        elif user_sec_in == 5:
            g = first_round[breaker][user_sec_in]
            result.append(g)
        elif user_sec_in == 6:
            g = first_round[breaker][user_sec_in]
            result.append(g)

        breaker = breaker + 1


    for inner_list in result:
        for sub_list in inner_list:
            for letter in sub_list:
                final_Guess += letter

    print(final_Guess)




"""-------------------------------------------------------------------"""
def intro():
    print("Are you Ready for amazing Guess Game:>")
    print("Can You think a word or name in your mind don't tell me:")

"""-------------------------------------------------------------------"""
def main():
    print(alphabets)
    intro()
    starter()
    print(first_round)
    second_round_display()
    second_round()

"""-------------------------------------------------------------------"""

if __name__ == "__main__":
    main()