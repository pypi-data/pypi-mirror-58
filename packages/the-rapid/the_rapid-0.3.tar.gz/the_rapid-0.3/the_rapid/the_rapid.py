from config import Config
import requests
import json


def get_stops():
    """Opens the stops.txt file and returns its contents as a json object.

    Returns:
        A json object containing locations and their corresponding addresses."""
    with open("stops.txt") as json_file:
        stops = json.load(json_file)
    return stops


class TheRapid:

    def __init__(self, api_key, origin__location, destination_location):

        # Google directions API key
        self.__api_key = api_key
        self.__stops = get_stops()
        self.__origin_address = self.__get_origin_address(origin__location)
        self.__destination_address = self.__get_destination_address(destination_location)
        # None state is changed when get_route is called
        self.__api_response = None
        # None state is changed after __get_api_response is called within get_route
        self.__route_data = None

    def __get_origin_address(self, origin):
        for location in self.__stops:
            if location == origin:
                origin_address = self.__stops[location]
                return origin_address

        raise KeyError("Provided origin argument <{}> is invalid.".format(origin))

    def __get_destination_address(self, destination):
        for location in self.__stops:
            if location == destination:
                destination_address = self.__stops[location]
                return destination_address

        raise KeyError("Provided destination argument <{}> is invalid.".format(destination))

    def __set_route_data_format(self):
        """Creates the 'format' for the route data json which will later be populated. Adjusts accordingly to how many
        transfers the route has.

        Returns:
            A dictionary with pre-defined keys, but no values."""
        route_data = {}
        for stop_set in self.__api_response:
            route_data[stop_set] = {"bus_line": "", "origin": "", "departure_time": "", "destination": "",
                                    "arrival_time": "", "duration": "", "distance": ""}
        return route_data

    def __get_api_response(self):
        """Sends a request to the Google Directions API and retrieves the dictionaries within the response that contain
        the route data.

        Returns:
            Dictionary(s) with the route data."""
        request_url = "https://maps.googleapis.com/maps/api/directions/json?origin={}&destination={}&mode=transit&" \
                      "transit_mode=bus&transit_routing_preference=less_walking&key={}".format(self.__origin_address,
                                                                                            self.__destination_address,
                                                                                            self.__api_key)

        api_response = json.loads(requests.get(request_url).text)
        if api_response["status"] == "REQUEST_DENIED":
            raise ValueError(api_response["error_message"])

        parsed_api_response = {}
        stop_num = 0
        # Block parses through the API response until all transit_details dictionaries are retrieved
        for route_info in api_response["routes"]:
            for leg_info in route_info["legs"]:
                for step_info in leg_info["steps"]:
                    if "transit_details" in step_info:
                        stop_num += 1
                        # There could be more than one stop if there is a line transfer
                        parsed_api_response["stop_set_" + str(stop_num)] = step_info

        return parsed_api_response

    def __get_bus_line(self):
        for stop_set in self.__api_response:
            self.__route_data[stop_set]["bus_line"] = self.__api_response[stop_set]["transit_details"]["line"] \
                ["short_name"]

    def __get_origin_stop(self):
        for stop_set in self.__api_response:
            self.__route_data[stop_set]["origin"] = self.__api_response[stop_set]["transit_details"]["departure_stop"] \
                ["name"]

    def __get_departure_time(self):
        for stop_set in self.__api_response:
            self.__route_data[stop_set]["departure_time"] = self.__api_response[stop_set]["transit_details"] \
                ["departure_time"]["text"]

    def __get_destination_stop(self):
        for stop_set in self.__api_response:
            self.__route_data[stop_set]["destination"] = self.__api_response[stop_set]["transit_details"] \
                ["arrival_stop"]["name"]

    def __get_arrival_time(self):
        for stop_set in self.__api_response:
            self.__route_data[stop_set]["arrival_time"] = self.__api_response[stop_set]["transit_details"] \
                ["arrival_time"]["text"]

    def __get_route_duration(self):
        for stop_set in self.__api_response:
            self.__route_data[stop_set]["duration"] = self.__api_response[stop_set]["duration"]["text"]

    def __get_route_distance(self):
        for stop_set in self.__api_response:
            self.__route_data[stop_set]["distance"] = self.__api_response[stop_set]["distance"]["text"]

    def get_route(self):
        """Sets the format for the route data json, sends the request to the Google Directions API and gets the
        response, and populates route_data.

        Returns:
            A dictionary(s) with the route data."""
        self.__set_route_data_format()
        self.__get_api_response()
        self.__get_bus_line()
        self.__get_origin_stop()
        self.__get_departure_time()
        self.__get_destination_stop()
        self.__get_arrival_time()
        self.__get_route_duration()
        self.__get_route_distance()

        return self.__route_data
