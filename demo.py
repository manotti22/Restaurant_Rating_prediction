from RestaurantRating.pipeline.pipeline import Pipeline
from RestaurantRating.logger import logging
from RestaurantRating.exception import RestaurantRatingException
import warnings
warnings
def main():
    try:

        pipeline = Pipeline()
        pipeline.run_pipeline()
        
    except Exception as e:
        logging.error(f"{e}")
        print(e)

if __name__=="__main__":
    main()


if __name__=="__main__":
    main()