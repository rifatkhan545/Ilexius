def vowel_count(given):
    given = given.lower()
    count = 0
    vowel = ['a', 'e', 'i', 'o', 'u']
    for x in given:
        if x in vowel:
            count += 1
    return count

print(vowel_count("Its a beautiful world"))


