# How to destructure Dictionaries in Python

a_dict = {
    'first': 'bobby',
    'last': 'hadz',
    'site': 'bobbyhadz.com'
}

first, last, site = a_dict.values()
print(first)  # 👉️ bobby
print(last)  # 👉️ hadz
print(site)  # 👉️ com