## Python-Common-Coding-Tools
Assortment of common python tools (Boolean expressions, Dictionaries, Tuples, etc.)

Interpretation: The meaning of Python being an interpreted language is that it does not compile before running. The code is read and interpreted line by line at run time. There are both benefits and pitfalls to interpretation. It is easy and fast to test out code and to make simple programs with little or lesser code than a language like C++. One problem of an interpreted language is that it is slower to process than a comparable C++ compiled program. 

Boolean expressions: For a Boolean expression within Python, and evaluation is either True or False. Tests or comparisons can be done, such as (x == y) to return whether the variables have an equal value. This can be used in a multitude of ways, a tool to check for items within a list or dictionary as well as a myriad of other implementations and all numbers are true except for zero or things such as empty lists. The Boolean feature of Python is very similar to C++

Short circuit evaluation: In Pythons short circuit evaluation, if two expressions or statements are divided by an or, if the first is true then then second half of the expression is ignored as it is not necessary for it to check its validity. A statement like (1 > 0) or (1 < 0), since the first grouping is true then the (1 < 0) is bypassed or ignored to save processing time. This is similarly implemented when using the keyword and, if the left side is false, the whole statement is false, and it is unnecessary to test the second condition. I believe that this is essentially the same in C++ except for the keywords used and the general syntax. 

Numeric types: With numeric types in Python, we can use the function type() to return the type of the parameter entered. A number such as 6 will return integer type, yet 6.0 will return float. There is also a complex number type in Python. If and equation is done between and integer and a float, when this is done, the integer is converted to a float and a float is returned. This very general view of numbers differs from how C++ views numbers and their type. This is because C++ is a compiled language and it must first know how much memory to set aside for the number, therefore a keyword such as int, float, double or long must be associated with a variable for it to be valid. 

Strings: Strings in python are assigned to a variable by being contained in either single or double quotation marks. You can use the print function to print out a string or index through each character like an array or list. Strings can be concatenated, and dictionaries and lists are not type dependent, so a list may hold strings, integers, and floats as well. This varies from C++ which does not allow multiple types within a singular container unless a class or structure is created to get around this problem. 

Arrays: There are no arrays in Python, their comparison would be lists. I don’t believe that this is a shortcoming for the language because there are other comparable tools that may be used. 

Lists: Python lists are comparable to traditional arrays, yet they are much more versatile, they are not type dependent, they can contain strings, dictionaries, or even other lists. They are much more versatile, I believe, than a traditional array as seen in C++. They also differ from arrays in that they can be changed, and they allow duplicates within them. 

Tuples: A tuple is similar to lists, but it is not changeable and therefore less flexible. They are more like an array in C++ because of this distinction. Their order is unchanging, but they similarly allow duplicates. A tuple can also be any combination of data types, unlike C++ arrays. 

Slices: Slice is a function within Python that returns a portion or “slice” of something such as a list or a string. The function parameter can optionally have a starting position, otherwise defaulting to the beginning, secondly it must contain an end point at least, thirdly it can optionally have a step. To be honest, I’m not sure if this is what you were looking for or a different term slicing that I am not familiar with.

Index range checking: In C++ there is no bounds checking but one can use expressions to check input ranges. In Python if you call for an index that is out of range, a False will be returned. You can similarly use a set of expressions to test the index range of a container using the len() function.

Dictionaries: Python dictionaries are another type of container which has a key and value pairing. They are mapped this way so that when a dictionary is searched for a key, the value attached to it will be returned if the key exists within the dictionary. Like other Python containers, dictionaries are not type specific. Dictionaries are changeable but cannot contain duplicates. I don’t know of any simple dictionary types within C++, I believe something comparable may be a map, but this is not something I have experience with. 

If statement: The if statement is straightforward and comparable to what I have seen in other languages, except of course for syntax. An if statement tests a condition, if it is true, it will perform the code block indented below it, otherwise it will bypass the following code and move to the next portion of the program. I believe that this is important in all programming languages. 

Switch statement: Not available in Python. Unlike C++, Python has no pre-defined switch-case tool and must use tome other means to switch between cases, an option may be if, elif statements. 

For loop: The for loop is like the if statement in that it is comparable to other languages I have seen. Items can be indexed with the for loop in their entirety or a range function may be implemented with a starting, stopping and incrementation parameter list. 

While loop: As stated above, the while loop is very similar to all languages I have seen. While an expression tests true, then the following code block will be implemented until the condition fails. 

Indentation to denote code blocks: Indentation within Python is a requirement; it defines what code is associated with other code. Something like an if statement must be followed by a colon and then an indentation on the following lines which belong to the statement. Unlike how C++ uses {} to contain code pertaining to a statement, Python only uses indentation. 

Type binding: I don’t know of any type binding in Python like C++ where a type keyword must be associated with a variable. Python does not require a type to be defined when a variable is created. I’m unsure if there is a way to force a type upon a variable as in C++ where something like and integer can be statically casted as a float.

Type checking: Displayed in numeric type program and explanation above. The type() function can return the type of a variable or container. 

Functions: Functions are comparable in Python to what I have seen in C++ in that it defines a function with or without parameters and contains a block of code. The code is only performed when called. Although functions are not necessarily required, they are essentially everywhere in Python programs. Not only are user defined functions implemented frequently, as are built in functions and functions brought in from imports. 

One other feature – your choice: Classes/Objects – Python can implement OOP with the use of classes and objects of classes to structure programming and make logic cleaner and more concise. After a class is defined, any number of objects can be created using the class making the code simpler and easier to understand, debug or change. 

Overall critique of the language: I think that Python is a phenomenal language. It seems much less convoluted than a language such as C++ and therefore aids in fast programming. Python is also extremely flexible, as it is not required for types to be defined and different types can be combined in the same container. While I am still new to the language, I believe that if I, or anyone learned the language, they would be able to code faster and more concisely to solve problems in a more direct way. 
