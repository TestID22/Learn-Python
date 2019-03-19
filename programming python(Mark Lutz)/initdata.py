elliot = {'name':'Elliot Anderson', 'age': 32, 'pay':40000, 'job':['Hacker','CyberSecurity']}
darling = {'name':'Darling', 'age': 34, 'pay':10000, 'job':'Hacker'}
tyrell = {'name':'Tyrell Wellick', 'age': 35, 'pay':100000, 'job':'Tech Dir'}

fsociety = {}
fsociety['elliot'] = elliot
fsociety['darling'] = darling
fsociety['tyrell'] = tyrell



if __name__ == "__main__":
    for key in fsociety:
        print(key, '\n key=>', fsociety[key])