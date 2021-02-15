from typing import List

import requests
import collections

Episode = collections.namedtuple('Episode',
                                 'category, id, url, title, description')


def get_episode_by_title(keyword: str) -> List[Episode]:
    url = f'https://search.talkpython.fm/api/search?q={keyword}'
    # print(url)

    resp = requests.get(url)
    resp.raise_for_status()

    results = resp.json()
    episodes = []
    for r in results.get('results'):
        episodes.append(Episode(**r))

    return episodes
