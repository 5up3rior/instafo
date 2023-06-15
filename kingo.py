import os
import requests
from bs4 import BeautifulSoup

def save_html_and_css(url, combine_files):
    response = requests.get(url)
    
    html_code = response.text
    
    soup = BeautifulSoup(html_code, 'html.parser')
    
    css_code = ""
    stylesheets = soup.find_all('link', rel='stylesheet')
    for stylesheet in stylesheets:
        stylesheet_url = stylesheet.get('href')
        if stylesheet_url.startswith('http'):
            css_response = requests.get(stylesheet_url)
            css_code += css_response.text + "\n"
        else:
            css_code += requests.compat.urljoin(url, stylesheet_url) + "\n"
    
    if not os.path.exists('txt'):
        os.makedirs('txt')
    
    if combine_files:
        combined_code = f"{html_code}\n\n<style>\n{css_code}\n</style>"
        with open('txt/website_combined.html', 'w', encoding='utf-8') as combined_file:
            combined_file.write(combined_code)
        print("Combined HTML and CSS file saved successfully.")
    else:
        with open('txt/website.html', 'w', encoding='utf-8') as html_file:
            html_file.write(html_code)
            
        with open('txt/styles.css', 'w', encoding='utf-8') as css_file:
            css_file.write(css_code)
        
        print("HTML and CSS files saved successfully.")

def get_website_details(url):
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    description = soup.find('meta', {'name': 'description'})
    keywords = soup.find('meta', {'name': 'keywords'})
    
    print("Website Details:")
    if description:
        print("Description:", description.get('content'))
    if keywords:
        print("Keywords:", keywords.get('content'))
    print()

def get_website_url():
    print("Select an option:")
    print("1. Enter website URL manually")
    print("2. Load website URL from a file")
    print("3. Combine CSS and HTML into a single file")
    
    choice = input("Enter your choice (1, 2, or 3): ")
    
    if choice == "1":
        website_url = input("Enter the website URL: ")
        get_website_details(website_url)
        save_html_and_css(website_url, False)
    elif choice == "2":
        # Load URL from a file
        # Add your code here
        pass
    elif choice == "3":
        website_url = input("Enter the website URL: ")
        get_website_details(website_url)
        save_html_and_css(website_url, True)
