import requests
from bs4 import BeautifulSoup
import os


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_page():

    # This function is to grab the HTML, parse it for the title, and return title/url
    try:
        request = requests.get(url='https://en.wikipedia.org/wiki/Special:Random/')

        html = request.text
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find(id='firstHeading').text.strip()
        url = request.url
        url = url.replace('(', '%28')
        url = url.replace(')', '%29')

        return title, url

    except requests.RequestException as e:
        print('Error during request: ' + str(e))


def main():

    try:
        exit_flag = False
        counter = 0
        titles = []

        # Here, we will start user input
        while not exit_flag:
            if counter == 0:
                start = input('Welcome! Do you want to generate a random webpage? \n(Y/N)\n').lower().strip()
                clear_console()

            else:
                start = input('Do you want to generate another random webpage?\n(Y/N)\n').lower().strip()
                clear_console()

            if start == 'n':
                print('Thanks for visiting!')
                exit_flag = True
            elif start != 'y':
                print('Please enter either Y or N')
            else:
                title, url = get_page()
                counter += 1
                titles.append(f'{title}\n{url}')
                print(f'{title}\n{url}\n')
    except Exception as e:
        print(f'I don\'t know how you did it, but theres an error:\n{str(e)}')

    if titles:
        print(f'While you were here, you generated {counter} pages:\n')
        for i in titles:
            print(i)


main()
