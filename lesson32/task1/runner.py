from file_manager import write_to_file
from variables import WIKI_URL, FILE_NAME, TWITTER_URL, FACEBOOK_URL
from requests_manager import get_content


if __name__ == '__main__':
    response = get_content(WIKI_URL + FILE_NAME)
    write_to_file('wiki', response.text, response.encoding)
    response = get_content(TWITTER_URL + FILE_NAME)
    write_to_file('twitter', response.text, response.encoding)
    response = get_content(FACEBOOK_URL + FILE_NAME)
    write_to_file('facebook', response.text, response.encoding)
    print()
