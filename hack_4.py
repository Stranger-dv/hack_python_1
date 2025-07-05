"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    result = "fooziman"
    last_letter = result.replace(result[-1], result[-1].upper())
    return last_letter

print(fn_hack_4())