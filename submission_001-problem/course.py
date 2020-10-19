

def create_outline():
    """
    TODO: implement your code here
    """
    print("Course Topics:")

    topics = {"Introduction to Python", "Tools of the Trade","How to make decisions", "How to repeat code", "How to structure data", "Functions", "Modules"}
    sorted_topics = sorted(topics)
    
    for i in sorted_topics:
        print("*", i)

    print("Problems:")

    problems = map(lambda x: "* " + x + ' : Problem 1, Problem 2, Problem 3', sorted_topics)
    print("\n".join(problems))

    print("Student Progress:")
    
    students = [
    (["Tdo", "Introduction to Python", "Problem 2","[STARTED]"]),
    (["Teboho", "How to make decisions", "Problem 1","[COMPLETED]"]),
    (["Lilo", "How to repeat code", "Problem 3","[GRADED]"])]

    students = sorted(list(students), key=lambda student: student[3], reverse=True)
    num = 1
    
    for count in students:
        print(str(num) + ".", "-".join(count[:3]), count[3])
        num += 1


if __name__ == "__main__":
    create_outline()
