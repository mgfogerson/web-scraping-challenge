import pandas as pd
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
import time

def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
#all url's
    url = 'https://redplanetscience.com/'
    new_url = "https://spaceimages-mars.com"
    pd_url = "https://galaxyfacts-mars.com"
#scrape for article name and content
    browser.visit(url)
    time.sleep(1)
    for x in range (1):
        html = browser.html
        soup = bs(html, 'html.parser')    
        news_title = soup.find('div', class_='content_title').text
        news_body = soup.find('div', class_='article_teaser_body').text
#scrape for featured image
    browser.visit(new_url)
    time.sleep(1)
    for x in range (1):
        html = browser.html
        soup = bs(html, 'html.parser')    
        image = soup.find('img', class_='headerimage fade-in')
        ftd_img=("https://spaceimages-mars.com/" + (image['src']))
#scrape for Mars facts
    mars_table = pd.read_html(pd_url, header=0)
    mars_df = mars_table[0]
    html_table = mars_df.to_html()
#hemisphere images
    hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "https://marshemispheres.com/images/valles_marineris_enhanced-full.jpg"},
    {"title": "Cerberus Hemisphere", "img_url": "https://marshemispheres.com/images/full.jpg"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://marshemispheres.com/images/schiaparelli_enhanced-full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://marshemispheres.com/images/syrtis_major_enhanced-full.jpg"},
]
#store data in dictionary
    mars_data = {
        "news_title": news_title,
        "news_body": news_body,
        "featured_": ftd_img,
        "hemi_urls": hemisphere_image_urls,
        "marstable": html_table
    }
#quit browser
    browser.quit()
    #return results
    return mars_data




    