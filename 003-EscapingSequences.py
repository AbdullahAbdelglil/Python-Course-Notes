#------------------------------
# Escape Sequences Characters
# 1- "\b" -> Back Space
# 2- "\" -> escape any special character, including (\, ', ", enter)
# 3- "\n" -> new line
# 4- "\r" -> Carriage return: Anything written after \r overwrites the existing text on the same line.
# 5- "\t" -> Horizontal tab
# 6- "\xhh" -> character hex-vale
#------------------------------

# "\b" usage:
print("hello\bworld") # will remove 'o' of hello;

# "\" usages:
print(""
      "hello \
       world \
       im abdullah"
      ) # write in multiple line (escape new lines)

print("desktop\\pycharm") # write '\' character in the text

print("my name is \"Abdullah\", and my age is \'23\' ") # escape special characters (", ') in the text

# "\r" usage:
print("python\rhello")

# "\xhh"
print("\x4f")