# Scrapy settings for airflowScrapy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'airflowScrapy'

SPIDER_MODULES = ['airflowScrapy.spiders']
NEWSPIDER_MODULE = 'airflowScrapy.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 16

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}
RETRY_HTTP_CODES = [429]
# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html


DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
    'scrapy_fake_useragent.middleware.RetryUserAgentMiddleware': 401,
    'airflowScrapy.middlewares.TooManyRequestsRetryMiddleware': 543,
    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    'rotating_proxies.middlewares.BanDetectionMiddleware': 620,

}


FAKEUSERAGENT_PROVIDERS = [
    'scrapy_fake_useragent.providers.FakeUserAgentProvider',  # This is the first provider we'll try
    'scrapy_fake_useragent.providers.FakerProvider',  # If FakeUserAgentProvider fails, we'll use faker to generate a user-agent string for us
    'scrapy_fake_useragent.providers.FixedUserAgentProvider',  # Fall back to USER_AGENT value
]

# Fallback User_Agent
USER_AGENT = 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'


ROTATING_PROXY_LIST = [
'45.224.255.126:9692',
'192.3.48.176:6169',
'154.85.100.80:5121',
'45.128.245.33:9044',
'186.179.7.188:8265',
'185.230.46.102:5751',
'45.127.248.127:5128',
'209.127.183.126:8224',
'141.98.135.130:7080',
'198.23.239.134:6540',
'64.137.95.130:6613',
'23.247.105.4:5068',
'185.101.169.112:6656',
'45.128.247.14:7515',
'5.183.34.106:6457',
'2.59.21.247:7777',
'104.144.3.253:6332',
'192.3.48.64:6057',
'45.154.56.161:7179',
'179.61.248.97:5188',
'193.23.245.97:8668',
'103.53.216.113:5197',
'134.73.188.42:5132',
'161.123.33.41:6064',
'216.74.118.200:6355',
'66.78.32.185:5235',
'193.8.94.208:9253',
'45.128.76.88:6089',
'192.186.176.144:8194',
'184.174.24.251:5261',
'198.23.128.2:5630',
'181.177.94.220:7794',
'104.148.5.211:6222',
'45.86.72.205:6352',
'170.244.93.194:7755',
'182.54.239.201:8218',
'45.140.13.166:9179',
'104.227.133.89:7151',
'144.168.143.57:7604',
'80.253.249.242:5285',
'45.192.138.108:6750',
'45.72.40.235:9329',
'154.95.36.80:6774',
'64.137.100.133:5188',
'23.236.182.205:7754',
'45.158.187.189:7198',
'64.137.94.224:6447',
'154.92.122.235:5305',
'23.250.83.161:6170',
'91.214.65.189:6036',
'216.173.111.59:6769',]

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'airflowScrapy.pipelines.AirflowscrapyPipeline': 300,
#}
AWS_ACCESS_KEY_ID = 'AKIAYUJWZRTZRRGQ3JVV'
AWS_SECRET_ACCESS_KEY = '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'

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = True

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
