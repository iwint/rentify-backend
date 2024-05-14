from src.models.listings import Listing
from src.services.listings import ListingService
from icecream import ic

listing_service = ListingService()


class ListingController:

    def create_listing(self, listing: Listing):
        return listing_service.create_listing(listing)

    def get_all_listings(self):
        return listing_service.get_all_listings()
