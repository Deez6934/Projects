from bs4 import BeautifulSoup
import requests
# Used to display the text of any wiki page the user enters the url of.


def scraper(iurl):  # Main function which scrapes the page

    # Used to get the unprocessed data of the page
    html_text = requests.get(url=iurl)

    # Uses Beatifulsoup and the lxml html parser to process the data for further use.
    soup = BeautifulSoup(html_text.content, 'lxml')

    # gets the title of the page
    title = soup.find('h1', class_='firstHeading mw-first-heading').text

    # finds and grabs all the paragraphs of the page we want to display
    paragraphs = soup.find_all('p')

    print("\n\n")
    print(title, "\n\n")

    for para in paragraphs:
        i = para.text
        print(i)


def main():  # Main
    cont = True
    print('''Welcome to a very basic wiki page scraper.\n''')

    while cont == True:
        iurl = str(
            input("Please enter the url of the wiki page you want scraped:"))
        scraper(iurl)
        ch = str(input('Do you wish to scrape another page?(Y/N):'))
        while True:
            if ch in ['Y', 'y', 'yes']:
                pass
                break
            elif ch in ['N', 'n', 'no']:
                cont = False
                break
            else:
                print('Please choose yes to proceed or no to exit.')


main()
