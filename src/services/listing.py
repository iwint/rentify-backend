from src.models.listing import Listing


class ListingService:

    async def create_listing(self, listing: Listing):
        return listing.dict()
