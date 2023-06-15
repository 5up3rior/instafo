
import requests
from bs4 import BeautifulSoup

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
    
    # HTML ko .txt file mein save karen
    with open('website.html', 'w', encoding='utf-8') as html_file:
        html_file.write(html_code)
        
    # CSS ko .txt file mein save karen
    with open('styles.css', 'w', encoding='utf-8') as css_file:
        css_file.write(css_code)
    
    print("HTML aur CSS files saved successfully.")

# Website ka URL input len
website_url = input("Enter the website URL: ")

# save_html_and_css() function ko call karen
save_html_and_css(website_url)
