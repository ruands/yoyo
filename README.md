# Weather Forecast API

Simple API that gives the forecast for a particular location.

## Setup steps
1. Start by creating a virtual environment by running `virtualenv -p python3.6 ve `. This will create an environment folder `ve` with Python 3.6.
2. Activate the environment with `source ./ve/bin/activate `. You should see `(ve)` in front of your directory. For example: `(ve) [~/personal/yoyo] $`.
3. Then install the requirements for the project by running `pip install -r requirements.txt`.
4. Run the migrations for Django with `./manage.py migrate`. We don't have any models for the project, but Django has some migrations that have to be run in order for it to function.
5. You should now be able to run the Django server with `./manage.py runserver 0.0.0.0:8000`.

## Usage

### /api/locations/\<location>/
Returns the forecast for `location`.

**Required Parameters:**
- location - the location for which a forecast is requested

**Optional Parameters:**
- days - the number of days to calculate the forecast for. The default and max is 3 days as limited by the external API. Usage: `http://127.0.0.1:8000/api/locations/johannesburg/?days=1`

**Response:**

200 Ok:
```
{
    "maximum": 11.1,
    "minimum": -0.1,
    "average": 5.63,
    "median": 7.25
}
```
