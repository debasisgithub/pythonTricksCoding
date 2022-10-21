def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo."""
    echoed_text = ""
    for i in range(repetitions,0,-1):
        #print(i)
        echoed_text += f"{text[-i:]}\n"
    return f"{echoed_text.lower()}."

'''
These below blocks will execute when you run the .py code file as a script from your command line:
When you run the file as a script by passing the file object to your Python interpreter, the expression __name__ == "__main__" returns True
like from shell bash: $ python NameAndMainIdiom.py
'''
if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))
    
#At the same time, if you import echo() in another module or a console session, then the nested code won’t run:    
from NameAndMainIdiom import echo
>>> print(echo("Please help me I'm stuck on a mountain"))

'''
Nesting code under if __name__ == "__main__" allows you to cater to different use cases:
Script: When run as a script, your code prompts the user for input, calls echo(), and prints the result.
Module: When you import echo as a module, then echo() gets defined, but no code executes. You provide echo() to the main code session without any side effects.
'''

'''
Sometimes, developers use the name-main idiom to add test runs to a script that combines code functionality and tests in the same file:
Although it is not a best approach altogether.
'''
import unittest

def add(a: int, b: int) -> int:
    return a + b

class TestAdder(unittest.TestCase):
    def test_add_adds_two_numbers(self):
        self.assertEqual(add(1, 2), 3)

if __name__ == "__main__":
    unittest.main()
    
'''
With this setup, you can run tests against your code when you execute it as a script:
It’s still possible to import the module and use the function that you’ve defined there. 
The unit test won’t run unless you execute the module in the top-level code environment.
While this works for small files, it’s generally not considered good practice. 
It’s not advised to mix tests and code in the same file. Instead, write your tests in a separate file. 
Following this advice generally makes for a more organized code base. This approach also removes any overhead, such as the need to import unittest in your main script file.
'''    