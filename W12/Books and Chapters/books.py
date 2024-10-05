largest_chapters = -1
largest_book = ""

select = input ("Which volume of scriptures would you like to learn about? ")

with open ("books_and_chapters.txt") as file:

    for data in file:

        data = data.strip()
        parts = data.split(":")

        book = parts [0]
        chapters = int (parts [1])
        scripture = parts [2]

        if scripture.lower() == select.lower():

            print ()
            print (f"Scripture: {scripture}, Book: {book}, Chapters: {chapters}")

            if chapters > largest_chapters:

                largest_chapters = chapters
                largest_book = book

print ()
print (f"The book with the most chapters in the {select.title()} is {largest_book}.")
print (f"It has {largest_chapters} chapters.")