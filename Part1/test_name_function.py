import unittest
from names import get_formatted_name

class NamedTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
    
    def test_first_last_middle_name(self):
        """Do names like 'Janis Mindoza Joplin' work?"""
        formatted_name = get_formatted_name('janis','joplin','mindoza')
        self.assertEqual(formatted_name, 'Janis Mindoza Joplin')

if __name__ == '__main__':
    unittest.main()

# Explanation of using __name__ == '__main__' from stackoverflow
# The simplest explanation for the __name__ variable (imho) is the following:

# Create the following files.

# # a.py
# import b
# and

# # b.py
# print "Hello World from %s!" % __name__

# if __name__ == '__main__':
#     print "Hello World again from %s!" % __name__
# Running them will get you this output:

# $ python a.py
# Hello World from b!
# As you can see, when a module is imported, Python sets globals()['__name__'] in this module to the module's name. Also, upon import all the code in the module is being run. As the if statement evaluates to False this part is not executed.

# $ python b.py
# Hello World from __main__!
# Hello World again from __main__!
# As you can see, when a file is executed, Python sets globals()['__name__'] in this file to "__main__". This time, the if statement evaluates to True and is being run.