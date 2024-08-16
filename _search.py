from fuzzywuzzy import fuzz
import time
from _configs import search_config
import threading

lock = threading.Lock()


def search(name: str, search: str, results: list):
    """Read the items in the crate and test them for the item, including related searches."""
    with open(f"{search_config.directory}/{name}", "r") as file:
        items = file.read().split("\n")

    local_results = {}
    for item in items:
        item_cleaned = item.strip().lower()

        # Fuzzy matching to find close matches
        if fuzz.ratio(item_cleaned, search) >= search_config.correction or fuzz.ratio(item_cleaned, f"the {search}") >= search_config.correction:
            local_results[item] = f"{name.strip('.txt')}<br>"

    # Adding related searches
    if not local_results:
        for item in items:
            item_cleaned = item.strip().lower()
            if fuzz.partial_ratio(item_cleaned, search) >= search_config.related:
                local_results[f"{item} (related)"] = f"{name.strip('.txt')}<br>"
                time.sleep(0.1)

    with lock:
        for item, result in local_results.items():
            if item in results:
                results[item] += result
            else:
                results[item] = result
