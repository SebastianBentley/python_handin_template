class NotEnoughStudentsException(Exception):
    pass

def closest_to_complete(lst):
    sorted_students = sorted(lst, key=lambda x: x.etcs_progression(), reverse=True)

    if(len(sorted_students) < 3):
        raise NotEnoughStudentsException()

    return sorted_students[0:3]


def closest_to_csv(lst):
    try:
        students = closest_to_complete(lst)
        print("Let's just pretend this writes to a csv file.")
    except NotEnoughStudentsException:
        print("Not enough students!")


    
