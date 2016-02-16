Place your catalog project in this directory.

# Item Catalog
- to run, `python applicaton.py`
- in browser, open http://localhost:5000


## Branches:

Master
- latest version using item names as queries
- throws errors if item query fails
- need to implement 404 for null db calls

user-item-ids
- implement using item and category IDs
- add 404 checking for .one() orm call errors?


## Notes

- pictures pulled from placeimg (slow)
- add images to static dir later
- add rss feed of catalog?
