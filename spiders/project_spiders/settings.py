# -*- coding: utf-8 -*-

# Importing Django stuff
import sys
import django
from django.conf import settings

# Scrapy settings for project_spiders project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'project_spiders'

SPIDER_MODULES = ['spiders.project_spiders.spiders']
NEWSPIDER_MODULE = 'spiders.project_spiders.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'project_spiders (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html# download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True
COOKIES_DEBUG = True

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'X-JAVASCRIPT-ENABLED': 'True',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, sdch, br',
    'accept-language': 'en-US,en;q=0.8',
    'cache-control': 'max-age=0',
    'cookie': '__cfduid=d84cade476442454c29ee229cd8cacebc1492104290; device_view=full; console_user=eshandas; recognized=1; master_access_token=3d260201.6195cdb0e7ba3d137fb2692d221367cc; oauth2_global_js_token=75c2c139c8b3450156bf8b430f8f7f74; _ga=GA1.2.740194336.1492104291; _gat_UA-62227314-1=1; ext_name=jaehkpjddfdgiiefcnhahapilbejohhj; session_id=b0bc251ec6316a9a6d8b2b3a076d30cb; _px3=10fbfdae5e221bd7ac9e1f5f75ee3455abf216cc7bd38cdcbeedd34286cf25a0:AJMDw8Ccga9vkrFQ8HRhwd3X2LTdNELjAhgkad0z3bpUrWVuTB9BjW4cGs5qtkYz6OGhp5LuMRUbIBzIUkRncQ==:1000:LCDNDCBexwXCyQjP+woQgO81Gh+tYVeaPpajDRlHfHA/BuTjYQapufS+uFBMPgEqRuUXYWfSVT0M1ijiTEMzqGjPtHzjVcvyLmh8HBPouUW7Bpvy9+UJoq9vMqiMdv8UgVLhO6qOpWzrpE9j+pQchzPNNDGPO4Xr6ITzGyJCj68=; visitor_id=49.207.53.171.1492104310552995; current_organization_uid=424283538535596033; company_last_accessed=d3488003; qt_visitor_id=23.57.75.57.1358008008468156; XSRF-TOKEN=2f6b8e8dcf423ad5dbff5e9bacc4bc52',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'project_spiders.middlewares.ProjectSpidersSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'project_spiders.middlewares.MyCustomDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'spiders.project_spiders.pipelines.ProjectSpidersPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# Setting up Django context
sys.path.append(settings.BASE_DIR)  # Absolute project path
django.setup()
