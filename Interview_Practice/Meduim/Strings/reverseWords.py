
def revString(separated_string, start, end):
    while start < end:
        separated_string[start] , separated_string[end] =  separated_string[end], separated_string[start]
        start += start
        end -= end
        return separated_string

def reverseWord(s):
    word_start = 0
    separated_string = [char for char in s]
    print(separated_string)
    length = len(separated_string) -1
    for i in range(length):
        if separated_string[i] == ' ':
            print(separated_string[word_start: i])
            separated_string = revString(separated_string, word_start, i - 1)
            word_start = i + 1
        elif i == length:
            separated_string = revString(separated_string, word_start, length)
    reversed_words = "".join(separated_string)
    reversed_words_list = reversed_words.split()
    reversed_reversed = reversed(reversed_words_list)

    result = list(reversed_reversed)
    return " ".join(result)
        


if __name__ == "__main__":
    s = "Sky is blue and dog barks" # "skrab god dna eulb si ykS"

    print("result : ",reverseWord(s))
