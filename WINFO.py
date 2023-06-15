import os
import requests
from bs4 import BeautifulSoup

# ANSI escape sequences for colorful output
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

def save_html_and_css(url):
    # HTTP GET request bhejen
    response = requests.get(url)
    
    # HTML aur CSS ko alag-alag variables mein store karen
    html_code = response.text
    
    soup = BeautifulSoup(html_code, 'html.parser')
    
    # CSS code ko extract karen
    css_code = ""
    stylesheets = soup.find_all('link', rel='stylesheet')
    for stylesheet in stylesheets:
        stylesheet_url = stylesheet.get('href')
        if stylesheet_url.startswith('http'):
            css_response = requests.get(stylesheet_url)
            css_code += css_response.text + "\n"
        else:
            css_code += requests.compat.urljoin(url, stylesheet_url) + "\n"
    
    # txt folder banaye (agar nahi hai)
    if not os.path.exists('txt'):
        os.makedirs('txt')
    
    # HTML aur CSS ko alag-alag files mein save karen
    with open('txt/website.html', 'w', encoding='utf-8') as html_file:
        html_file.write(html_code)
        
    with open('txt/styles.css', 'w', encoding='utf-8') as css_file:
        css_file.write(css_code)
    
    print(f"{GREEN}HTML aur CSS files saved successfully.{RESET}")

def get_website_details(url):
    # HTTP GET request bhejen
    response = requests.get(url)
    
    # HTML code ko parse karen
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Website details extract karen
    title = soup.title.string.strip()
    description = soup.find('meta', {'name': 'description'})
    keywords = soup.find('meta', {'name': 'keywords'})
    
    print(f"{BLUE}Website Details:")
    print(f"{YELLOW}Title: {RESET}{title}")
    if description:
        print(f"{YELLOW}Description: {RESET}{description.get('content')}")
    if keywords:
        print(f"{YELLOW}Keywords: {RESET}{keywords.get('content')}")
    print()

def get_website_url():
    # Display the WINFO title and design
    print(f"{YELLOW}  _______   ______   .__   __.  _______ ")
    print(f" /  _____| /  __  \\  |  \\ |  | |   ____|")
    print(f"|  |  __  |  |  |  | |   \\|  | |  |__   ")
    print(f"|  | |_ | |  |  |  | |  . `  | |   __|  ")
    print(f"|  |__| | |  `--'  | |  |\\   | |  |____ ")
    print(f" \\______|  \\______/  |__| \\__| |_______|")
    print(RESET)

    print("Select an option:")
    print(f"{YELLOW}1. Enter website URL manually")
    print(f"2. Load website URL from a file{RESET}")
    
    choice = input(f"{YELLOW}Enter your choice (1 or 2): {RESET}")
    
    if choice == "1":
        website_url = input(f"{YELLOW}Enter the website URL: {RESET}")
        get_website_details(website_url)
        save_html_and_css(website_url)
   
