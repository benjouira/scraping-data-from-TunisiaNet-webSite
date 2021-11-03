import scrapy

class sidatascraper(scrapy.Spider) :
    name='tripadvisor'
    start_urls=['https://www.tripadvisor.fr/Hotel_Review-g297941-d581157-Reviews-Iberostar_Mehari_Djerba-Djerba_Island_Medenine_Governorate.html']
    def parse(self, response):
      
        for comments in response.css('div.cWwQK'):
           
            yield{
                    'comment': comments.css("div.pIRBV span::text").get(),
                    'raiting': comments.css("div.emWez span::attr(class)").get(),
                    
                       }
        nextpage=response.css("a.next.ui_button").attrib['href']
        if nextpage is not None:
            yield response.follow(nextpage, callback=self.parse)