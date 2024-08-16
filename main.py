import os
import threading
from _configs import search_config
from _search import search


results = {}
threads = []
lock = threading.Lock()

DIR = os.scandir(search_config.directory)
database = [x.name for x in DIR]


def main(search_query):
    """Search the database for a crate and provide related searches."""

    if not search_query:
        return

    # Clear previous results
    results.clear()

    # Search for exact and related matches
    for x in database:
        thread = threading.Thread(
            target=search, args=(x, search_query, results))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return results
