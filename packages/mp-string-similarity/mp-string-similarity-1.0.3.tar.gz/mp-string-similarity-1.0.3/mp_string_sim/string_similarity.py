import re
from strsimpy.jaro_winkler import JaroWinkler
from collections import defaultdict, Counter

class String_Sim():
  def __init__(self, k):
    super().__init__(k)

  def word_cloud(self, names, top=5, delimiters=[' ']):
    # Word Cloud will take a list of names and return a count of words
    # this is intended to find common words used multiple times in a given
    # implementation.
    word_counts = defaultdict(int) 
    total_words = 0
    for name in names:
      for word in split(name, delimiters):
        word_counts[word] += 1 
        total_words += 1
      top_words = Counter(word_counts).most_common(top)
    return (top_words, total_words)

  def split(self, name, delimiters, maxsplit=0):
      regexpattern = '|'.join(map(re.escape, delimiters))
      return re.split(regexpattern, name, maxsplit)

  def similarity(self, names, limit = .6):
    ## Given a list of events return the events that have a similarity > .6
    ## Should this return a metric?
    ## What happens when an event is similar to > 1 event

    similar_events = defaultdict(list)
    similar_event_count = 0
    jarowinkler = JaroWinkler()
    for event_name in names:
      for compared_event in names:
        if event_name == compared_event: 
          continue
        if jarowinkler.similarity(event_name, compared_event) > limit:
          similar_events[event_name].append(compared_event)
          similar_event_count += 1
    ##  Am I double counting events?
    similarity = similar_event_count  / len(names) ** 2
    return (similar_events, similarity)