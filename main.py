# This function is used to display menu to the user
def menu():
    print("***************** Books Management ******************")
    print("1. Add new book\n2. Find a book\n3. Display books\n4. Borrow book\n5. Return book\n6. End the program")
    user_choice = int(input("What's your choice :"))
    return user_choice


# function to add new book
def add_book():
    book_number = input("Enter book number : ")
    title = input("Enter title : ")
    author_name = input("Enter name of main author : ")
    publisher = input("Enter publisher details :")
    year_publication = int(input("Year of publication : "))
    no_of_copies = int(input(" No. of copies : "))
    available_copies = int(input(" Available copies : "))
    text = book_number + "," + title + "," + author_name + "," + publisher + "," + str(year_publication) + "," + str(
        no_of_copies) + "," + str(available_copies)+"\n"
    try:
        write_to_file("books.txt", text)
        print("Book added successfully")
    except FileNotFoundError:  # if any issue adding data to file
        print("Error adding file.")


# function to write data to file
def write_to_file(filename, data):
    file = open(filename, "a")  # append mode
    file.writelines(data)
    file.close()


# function to find a book
def find_book(book_number):
    file = open("books.txt","r")
    lines = file.readlines()
    flag = False
    for line in lines:
        if len(line) > 1:
            if book_number == line.split(",")[0]:
                flag = True
                break
    return flag
# function to display books
def display_books():
    print("********************************")
    print("1. Display by author\n2. Display by publisher\n3. Display by year of publication\n4. display all")
    choice = int(input(" yOur choice : "))
    file = open("books.txt", "r")
    lines = file.readlines()

    if choice == 1:
        author_name = input(" Enter author name : ")
    elif choice == 2:
        publisher_name = input(" Enter publisher name : ")
    elif choice == 3:
        year = int(input(" Enter year : "))
    print("********************************")
    print("Available books are: ")
    print("________________________________________________________________________________________________")
    print("| Book_number| Title_of_Book| Author_Name| Publisher_Name | Year |no_of_copies |available_copies|")
    print("________________________________________________________________________________________________")
    flag = False
    for line in lines:
        if len(line) > 1:
            data = line.rstrip('\n').split(",")
            if choice == 1:
                if data[2] == author_name:
                    display_selected_books(data)
                    flag = True
            elif choice == 2:
                if data[3] == publisher_name:
                    display_selected_books(data)
                    flag = True
            elif choice == 3:
                if int(data[4]) == year:
                    display_selected_books(data)
                    flag = True
            elif choice == 4:
                display_selected_books(data)
                flag = True
            else :
                print("Wrong selection!!")
    if not flag:
        print(" No Data found")
        print("________________________________________________________________________________________________")

# function to display books based on choice
def display_selected_books(data):

    print("|", data[0].ljust(10, ' '), "|", data[1].ljust(12, ' '), "|", data[2].ljust(10, ' '), "|",
    data[3].ljust(14, ' '), "|", data[4].ljust(4, ' '), "|", data[5].ljust(11, ' '), "|",
    data[6].ljust(14, ' '), "|")
    print("________________________________________________________________________________________________")
# main function
if __name__ == '__main__':
    choice = menu()  # check the choice
    while choice != 6:
        if choice == 1:
            add_book()
        elif choice == 2:
            book_number = input("Enter book number to search : ")
            flag = find_book(book_number)
            if flag:
                print(f"Book with number {book_number} found")
            else:
                print("Book not found!!")
        elif choice == 3:
            display_books()
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        elif choice == 6:
            pass
        else:
            print("Wrong input!!")
        choice = menu()
