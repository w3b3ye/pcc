def print_name(fname, lname, **args):
    """Simple function to see arbitory arguments"""
    name = {}
    name.update({'first':fname,'last':lname})
    name.update(args)
    return name

#fav_players = {'Cricket':'Sachin','Soccer':'XXX'}
#print(print_name('tom','dick',fav_players))
print(print_name('tom','dick',cricket='Sachin',soccer='XYZ'))