from modules.Syllabus import *
from modules.Teacher import *

main = Syllabus("example.syllabus")

main["teachers"] = {}
print(main.make())
main.write("example")
main.exit()