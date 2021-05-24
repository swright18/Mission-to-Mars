# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager



# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)



# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)




# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')




slide_elem.find('div', class_='content_title')



# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title




# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p



# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)




# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()




# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup




# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel



# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts



df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()




df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df




df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres
# 1 
url = 'https://marshemispheres.com/'
browser.visit(url)


html = browser.html
hemi = soup(html, 'html.parser')
main_url = hemi.find_all('div', class_='item')
titles=[]
hemisphere_img_urls=[]
for x in main_url:
    title = x.find('h3').text
    img_url = x.find('a')['href']
    hemi_img_url= url+img_url
    #print(hemi_img_url)
    #print(title)
    browser.visit(hemi_img_url)
    html = browser.html
    hemi = soup(html, 'html.parser')
    hemisphere_img_original= hemi.find('div',class_='downloads')
    hemisphere_img_url=hemisphere_img_original.find('a')['href']
    full_hemi_img_url=url+hemisphere_img_url
    #print(full_hemi_img_url)
    
    hemi_dict=dict({'title':title, 'img_url':full_hemi_img_url})
    hemisphere_img_urls.append(hemi_dict)



# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_img_urls

# 5. Quit the browser
browser.quit()




