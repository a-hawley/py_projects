import requests
from bs4 import BeautifulSoup


def get_page():
    # This function is to grab the HTML, parse it for the title, and return title/url
    try:
        request = requests.get(url='https://en.wikipedia.org/wiki/Special:Random/')

        html = request.text
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find('h1', id='firstHeading')

        return title.text.strip(), request.url

    except requests.RequestException as e:
        print('Error: ' + str(e))


def main():

    exit_flag = False
    counter = 0

    # Here, we will start user input
    while not exit_flag:
        if counter == 0:
            start = input('Welcome! Do you want to generate a random webpage? \n(Y/N)\n').lower().strip()
        else:
            start = input('Do you want to generate another random webpage?\n(Y/N)\n').lower().strip()

        if start == 'n':
            print('Thanks for visiting, and have a great day!')
            exit_flag = True
        elif start != 'y':
            print('Please enter either Y or N\n')
        else:
            title, url = get_page()
            counter += 1
            print(title + '\n' + url)


main()
