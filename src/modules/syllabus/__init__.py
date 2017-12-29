#

if __name__ == "__main__":
    __path = os.path.abspath(os.path.dirname(__file__))
    __example = os.path.join(__path, 'example.syllabus')

    syllabus = open(__example, 'r')

    sylla_dict = syllabus.read()
    syllabus.close()

    dictionary = eval(sylla_dict)
    print(dictionary)
