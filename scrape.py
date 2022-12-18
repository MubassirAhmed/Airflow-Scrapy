from airflowScrapy.spiders.tester import testSpider
from scrapy.crawler import CrawlerProcess
from datetime import datetime
from scrapy.utils.project import get_project_settings

def main():
    
    # Dynamically determining s3 name
    dateTime = datetime.now()
    s3FileName = dateTime.strftime('%Y-%m-%d_Time-%H-%M{}'.format('.csv'))
    settings = get_project_settings()
    settings.update({  'FEEDS': {"s3://linkedin-scraper-1/linkedin/{}.csv".format(s3FileName): {"format": "csv"}}  })
    
    # Executing spider
    process = CrawlerProcess(settings)
    process.crawl(testSpider)
    process.start()
    
if __name__ == '__main__':
    main()