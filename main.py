from airflowScrapy.spiders.tester import testSpider
from scrapy.crawler import CrawlerRunner
from datetime import datetime 
from scrapy.utils.project import get_project_settings
import os
from scrapy.utils.log import configure_logging
from twisted.internet import reactor

def main():
    
    # Properly importing settings.py
    # settings_file_path = 'airflowScrapy.settings' # The path seen from root, ie. from main.py
    # os.environ.setdefault('SCRAPY_SETTINGS_MODULE', settings_file_path)
    configure_logging()
    settings = get_project_settings()
    
    # s3 name setup
    dateTime = datetime.now()
    s3FileName = dateTime.strftime('%Y-%m-%d_Time-%H-%M{}'.format('.csv'))
    settings.update({  'FEEDS': {"s3://linkedin-scraper-1/linkedin/{}".format(s3FileName): {"format": "csv"}}  })
    
    # This is here to make it easy to turn off S3. Just comment everything above, and uncomment everthing below
    #settings = get_project_settings()
    
    # Executing spider
    runner = CrawlerRunner(settings)
    
    d = runner.crawl(testSpider)
    d.addBoth(lambda _: reactor.stop())
    reactor.run()
    
    
    
if __name__ == '__main__':
    main()