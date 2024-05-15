from src.utils.db_actions import DBActions
from icecream import ic
from src.models.listings import Listing
from fastapi import HTTPException, status
import uuid

db_actions = DBActions()


class ListingService:

    def create_listing(self, listing: Listing):

        listing_payload = listing.dict()
        listing_payload['listing_id'] = uuid.uuid4()

        db_actions.add_data_to_db(
            'listings', listing_payload, "Error creating listing")
        return db_actions.get_data_from_db('listings', listing.dict(), "Error retrieving listing")

    def get_all_listings(self):
        return db_actions.get_all_data_from_db('listings', "Error retrieving listings")

    def get_listing_by_id(self, listing_id: str):
        ic(listing_id)
        listing = db_actions.get_data_from_db(
            'listings', {"listing_id": listing_id}, "Error retrieving listing")
        ic(listing)
        try:
            if listing:
                return listing
            else:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, detail="Listing not found")
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Listing not found")
