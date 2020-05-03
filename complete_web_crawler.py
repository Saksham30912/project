#Finish crawl web
import urllib.request

def get_page(url):
    # This is a simulated get_page procedure so that you can test your
    # code on two pages "http://xkcd.com/353" and "http://xkcd.com/554".
    # A procedure which actually grabs a page from the web will be 
    # introduced in unit 4.
    try:
    	return urllib.request.urlopen(url).read().decode("utf-8")
    except:
        return ""
    return ""

def get_next_target(page):
    start_link = page.find("<a href=")
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)


def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            union(tocrawl,get_all_links(get_page(page)))
            crawled.append(page)
            print(crawled)
    return crawled




print(crawl_web("https://udacity.github.io/cs101x/urank/"))