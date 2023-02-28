BOT_NAME = 'amazon'

SPIDER_MODULES = ['amazon.spiders']
NEWSPIDER_MODULE = 'amazon.spiders'

ROBOTSTXT_OBEY = False

AUTOTHROTTLE_ENABLED = True

REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'

FEEDS = {
    'data/%(name)s/%(name)s_%(time)s.json': {
        'format': 'json',
        'encoding': 'utf8',
        'overwrite': True
    }
}