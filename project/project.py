#Lyrica only supports English songs for now. The songs are scraped from AZ Lyrics site.

from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import requests
import sys
from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        # Logo
        self.image('Lyrica.png', 80, 8,50)
        self.ln(10)
        # font
        self.set_font('helvetica', 'BU', 50)
        self.cell(80)
        # Title
        self.cell(30, 10, song_name.upper(), align='C')
        # Line break
        self.ln(30)

    # Page footer
    def footer(self):
        # Set position of the footer
        self.set_y(-15)
        # set font
        self.set_font('helvetica', 'I', 8)
        # Page number
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align='C')

def get_url(song,artist):
    url = f"https://search.azlyrics.com/search.php?q={song}+{artist}&x=118d989895eeb850cd93fe0be9272cc623bacfe34e9911e23328565e68e5ce79"
    return url

def get_request(song,artist):
    url=get_url(song,artist)
    request = requests.get(url).text
    only_table_tags = SoupStrainer("table")
    doc = BeautifulSoup(request, "html.parser", parse_only=only_table_tags)


    for link in doc.find_all('a'):
        dat = link.get('href')
        if dat =="":
            sys.exit("INVALID DATA")
        get_contents(dat,song)
        break

def get_in_txt(lyrics):
    Lyrics = lyrics.split('\n')
    f1 = open("Lyrica.txt", 'w')
    for Lyric in Lyrics:
        f1.write(Lyric)
        f1.write("\n")

def get_contents(link,song):
    req_link = requests.get(link).text
    data = BeautifulSoup(req_link, "html.parser")
    lyrics = data.find_all("div",attrs={"class":"col-xs-12 col-lg-8 text-center"})[0].find_all("div")[5].get_text()
    print("\n")
    os.system('cls')
    if '+' in song:
        print("\n",song.replace("+"," ").upper(),"\n\n")
    elif '+' not in song:
        print("\n",song.upper(),"\n\n")
    try:
        print(lyrics.strip())
        get_in_txt(lyrics.strip())
        to_pdf(song)
    except UnicodeEncodeError:
        os.system('cls')
        sys.exit("!!!!ONLY ENGLISH SONGS ARE SUPPORTED.SO YOUR SONG CANNOT BE CONVERTED TO A PDF!!!")


def get_data(song_name,artist_name):

    if " " in song_name:
        song=song_name.replace(" ", "+")
    else:
        song = song_name


    if " " in artist_name:
        artist=artist_name.replace(" ", "+")
    else:
        artist = artist_name

    get_request(song,artist)

def get_song():
    song_name=input("Song: ")
    return song_name.strip()

def get_artist():
    artist_name=input("Artist name: ")
    return artist_name.strip()


def main():
    artist_name = get_artist()
    get_data(song_name,artist_name)

def get_input():
    dat = input ("\n\nDo you want the lyrics to be converted to a pdf (y/n)? ")
    return get_permission(dat)


def get_permission(dat):
    if dat == "y":
        return "y"
    elif dat =="n":
        return "n"
    else:
        sys.exit("!!!ENTER A VALID RESPONSE AND TRY AGAIN")

def welcome_page():
    print("-------WELCOME TO LYRICA-------")


def to_pdf(song):
    dat = get_input()
    if dat == "y":
        print("\n\n")
        print("!!!THIS MIGHT TAKE SOME TIME PLEASE WAIT!!!")

        pdf = PDF('P', 'mm', 'Letter')

        pdf.alias_nb_pages()

        pdf.set_auto_page_break(auto = True, margin = 15)

        pdf.add_page()

        pdf.set_font('times', '', 20)

        f = open("Lyrica.txt", "r")

        for x in f:
            pdf.cell(200, 10, txt = x, align = 'C')
            pdf.ln(10)

        pdf.output(f'{song}.pdf')
        os.system('cls')

        print("\n!!!YOUR PDF IS READY!!!")
        print("\n-------THANKYOU FOR USING LYRICA-------")

    elif dat =="n":
        os.system('cls')
        sys.exit("-------THANKYOU FOR USING LYRICA-------")

if __name__ == "__main__":
    os.system('cls')
    welcome_page()
    song_name = get_song()
    main()