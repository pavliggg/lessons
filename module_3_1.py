calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()

def is_contains(string, search_list):
    count_calls()
    f = False
    for i in search_list:
        if string.lower() in i.lower():
            f = True
            break
    return f
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)