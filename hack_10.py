"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    list_result = []

    new_result = result.replace("o","0").replace("i","1").replace("a","@").upper()

    for letter in new_result:
        list_result.append(letter)
        list_result

    return list_result
