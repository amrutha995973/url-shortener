url_map = {}

def shorten_url(long_url):
    short = str(len(url_map) + 1)
    url_map[short] = long_url
    return short

def get_url(short_url):
    return url_map.get(short_url, "Not found")

# Example usage
short = shorten_url("https://example.com")
print(short)
print(get_url(short))
