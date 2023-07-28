import csv
from prisma import Prisma


def main() -> None:
    prisma = Prisma()
    prisma.connect()

    with open("user_data.csv", "r") as students_csv:
        students_reader = csv.reader(students_csv, delimiter=",")
        students_list = []
        student_emails = []
        for row in students_reader:
            student_emails.append(row[3])
            if (len(row[1]) > 0):
                students_list.append({"name": row[0], "phone": row[2], "email": row[3], "Team": {
                                     "connect": {"id": row[1]}}})
            else:
                students_list.append(
                    {"name": row[0], "phone": row[2], "email": row[3]})


        prisma.member.delete_many({"email": {"not_in": student_emails}})
        print(students_list)
        prisma.member.create_many(data=students_list, skip_duplicates=True)


if __name__ == "__main__":
    main()
