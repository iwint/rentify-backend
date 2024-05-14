from src.utils.db_actions import DBActions
from icecream import ic
from src.models.listings import Listing


db_actions = DBActions()


class ListingService:

    def create_listing(self, listing: Listing):
        db_actions.add_data_to_db(
            'listings', listing.dict(), "Error creating listing")
        return db_actions.get_data_from_db('listings', listing.dict(), "Error retrieving listing")

    def get_all_listings(self):
        return db_actions.get_all_data_from_db('listings', "Error retrieving listings")
