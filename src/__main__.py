from modules.Syllabus import *
from modules.Teacher import *

main = Syllabus("example.syllabus")

main["meta", "author"] = "Kiselev Nikolay"

main.write("example", make=True)


# BETA HTML LAYOUT?

a = input("""Are you ready for html print
Will create file __test.html
And open browser? (y/n) """)

print("\n\n")

if a == "y" or a == "yes" or a == "ye" or a == "yep" or a == "ja" or a == "yea" or a == "д" or a == "да":
    first = open('test.html', 'r')
    HTML = first.read()
    first.close()
    second = open('__test.html', 'w')
    second.write(HTML.format(main.html()))
    second.close()
    print("Pleae, weit, brozer")
    __import__("webbrowser").open_new_tab('__test.html')
else:
    print(main.com())
