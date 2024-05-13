from src.models.listing import Listing
from src.services.listing import ListingService

listing_service = ListingService()

class ListingController:
    
    async def create_listing(self, listing: Listing):
        return listing_service.create_listing(listing)