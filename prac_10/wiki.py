"""
CP1404/CP5632 - Practical 10
Wikipedia API & Python Library
"""
import wikipedia

search_topic = input("Search: ")
while search_topic != "":
    try:
        topic_summary = wikipedia.summary(f"{search_topic}", sentences=5)
        topic_page = wikipedia.page(search_topic)
        print(topic_page.title)
        print(topic_summary)
        print(topic_page.url)
        search_topic = input("Search: ")
    except wikipedia.exceptions.DisambiguationError as topics:
        print(topics)
