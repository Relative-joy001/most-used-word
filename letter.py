
# define the most used word function

def most_used_letter(word):

    count_let = dict()

    # 1st condition:
    # Iterration of each letter and get the count
    for letter in word:
        if letter in count_let:
            count_let[letter] += 1
        else:
            count_let[letter] = 1

    #2nd condition
    most_used = list()
    max_letter = 0

    # finding the max letter
    # Iterration for the max value in count_let
    for num in count_let.values(): # count_let values collect the value from the count_let dictionary
        if num > max_letter:
            max_letter = num
    # condition if no letter repeat in the word
    if num == max_letter:
        no_max_let_result = f"There no most used letter in the word: {word}"
        return no_max_let_result
    else:
        # Iterration for geting letter and leter count in the word.
        for items, item_count in count_let.items():
            # use this condition if most_used is a empty string
            #if item_count >= max_letter:
            #most_used = items
            #max_letter = item_count

            # adding letters to the most used list
            if item_count == max_letter:
                most_used.append(items)

        max_let_result = f"The most used letter in the word: {word} = {most_used}. It appear {max_letter} times."
        return max_let_result  
        
    
print(most_used_letter("better"))

# print(most_used_letter("best"))
