from PyPDF2 import PdfReader
from os import listdir
import json
import shortuuid


def get_info(path, category, book):
    with open(path, "rb") as f:
        pdf = PdfReader(f)
        info = pdf.metadata
        pages = len(pdf.pages)
    author = info.author
    creator = info.creator
    producer = info.producer
    subject = info.subject
    title = info.title
    if title is not None and not author is not None:
        return {
            "id": shortuuid.uuid(),
            "category": category,
            "path": path,
            "short_name": title[:5],
            "full_name": title,
            "author": author,
        }
    elif author is not None and title is None:
        return {
            "id": shortuuid.uuid(),
            "category": category,
            "path": path,
            "short_name": book[:5],
            "full_name": book,
            "author": author,
        }
    elif title is not None and author is None:
        return {
            "id": shortuuid.uuid(),
            "category": category,
            "path": path,
            "short_name": title[:5],
            "full_name": title,
            "author": "No Author",
        }
    else:
        return {
            "id": shortuuid.uuid(),
            "category": category,
            "path": path,
            "short_name": "No title",
            "full_name": "No title",
            "author": "No Author",
        }


if __name__ == "__main__":
    files = (
        listdir("./library/aviation-studies/")
        + listdir("./library/business/")
        + listdir("./library/computer-science/")
        + listdir("./library/engineering/")
        + listdir("./library/health-sciences/")
        + listdir("./library/humanities/")
        + listdir("./library/mathematics/")
        + listdir("./library/physical-sciences/")
        + listdir("./library/social-sciences/")
        + listdir("./library/theology/")
    )

    categoriesList = listdir("./library/")
    if categoriesList.__contains__("booklist.json"):
        categoriesList.remove("booklist.json")
    jsonStruct = []
    for category in categoriesList:
        print(category)
        tempName = "./library/" + category + "/"
        booksSection = listdir(tempName)
        for book in booksSection:
            fullPath = tempName + book
            jsonStruct.append(get_info(fullPath, category, book))
    print(jsonStruct)
    with open("booklist.json", "w") as write_file:
        json.dump({"books": jsonStruct}, write_file)
    print("Done Writing")
