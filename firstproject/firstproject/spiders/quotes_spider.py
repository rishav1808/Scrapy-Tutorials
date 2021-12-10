import scrapy

class QuotesSpider(scrapy.Spider): #Inherits from the Spider class
    name="quotes_spider" #Name of the Spider, can be anything

    def start_requests(self): #Inbuild method helps to scrape the webpages
        urls=[  #Collection of webpages through which we can scrape data
            "http://quotes.toscrape.com/page/1/",
            "http://quotes.toscrape.com/page/2/",
        ] 
        #Generator function
        for url in urls: 
            #Request method is similar to what I have done earlier url= ,requests a url and the callback tells 
            #what to do with that URL
            yield scrapy.Request(url=url,callback=self.parse)
    #How to get the information from the website
    def parse(self, response):
        page_id=response.url.split("/")[-2] #Just to get the no. from the url
        filename= f"quotes{page_id}.html"# Creates a file for one webpage to store data

        with open(filename,"wb") as f: #After creating the file, the data crawled is stored here and then saved
            f.write(response.body)
        self.log(f'Saved file {filename}')

        
#New #New1  #New2  #New3 #New4 #New5 #New6 #New7 #New8 #New9 #New10 #New11 #New12 #New13 #New14 #New15 #New16 #New17 #New18 #New19 #New20 #New21 #New22
