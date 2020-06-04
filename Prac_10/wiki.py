import wikipedia


def main():
    user_input = input("Please enter the phrase or title to search: ")
    while user_input != "":
        try:
            web_page = wikipedia.page(user_input)
            print(web_page.title)
            print(web_page.summary)
            print(web_page.url)
        except wikipedia.exceptions.DisambiguationError as e:
            for i, option in enumerate(e.options, 1):
                print("{}. {}".format(i, option))
        except wikipedia.exceptions.PageError:
            print("Page not found.")
        user_input = input("Please enter the phrase or title to search: ")
    print("Thank You!")


main()
