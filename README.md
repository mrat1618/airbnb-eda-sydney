# Sydney AirBnB: exploratory data analysis

This analysis of Sydney AirBnB data was conducted as a part of the Udacity Data Science Nanodegree course. You can find the full set of analysis scripts and notebooks in this repository. A more consumer friendly Medium blog post can be found [here](https://medium.com/@humulene/what-is-your-airbnb-choice-for-next-time-you-are-in-sydney-5db6dcb201d8).

## Project Motivation
If you're travelling somewhere, the biggest challenge would be finding good, reasonably priced accommodation. Starting from the air ticket, Sydney is an expensive travel destination, particularly when compared to Asia. However, the experience you would get travelling in Australia is so unique. Sydney in particular is surrounded by a lot of beaches, national parks and tourist attractions. There is a wide variety of places you can visit within a few hours either by a vehicle or simply by using public transportation. Here, we use AirBnB accommodation data to find out:
 - What neighbourhood has most listings?
 - What is the average AirBnB cost in Sydney?
 - What amenities can you get?

More insights and in-dept data exploration can be found inside `airbnb-eda-sydney.ipynb`

## Requirements
 - python (3.7)
 - pandas (1.2.4)
 - numpy (1.20.3)
 - seaborn (0.11.1)
 - matplotlib (3.3.4)

## File in the repository
 - `airbnb-eda-sydney.ipynb`: Exploratory data analysis
 - `utils/datawrangling.py`: Data wrangling modules
 - `utils/plotting.py`: Plotting related modules

### Visualisations (inside `figs/` folder)
 - [`price.png`](figs/price.png): Sydney AirBnB price distribution
 - [`sydney-airbnb-amenities.png`](figs/sydney-airbnb-amenities.png): Most listed (first 10) amenities by room type
 - [`sydney-airbnb-amenities-50.png`](figs/sydney-airbnb-amenities-50.png): Most listed (first 50) amenities by room type
 - [`sydney-airbnb-rooms.png`](figs/sydney-airbnb-rooms.png): Number of AirBnB rooms by type and neighbourhood. (A few zoomed versions are also available)
 - [`sydney-airbnb-rooms-price.png`](figs/sydney-airbnb-rooms-price.png): AirBnB average price by neighbourhood and room type

## Results
A more consumer friendly summery (Medium blog post) can be found [here](https://medium.com/@humulene/what-is-your-airbnb-choice-for-next-time-you-are-in-sydney-5db6dcb201d8).

## Acknowledgements
The dataset used in this project is publicly available at <http://insideairbnb.com/get-the-data.html>