import data
import helpers
class TestUrbanRoutes:

    def test_set_route(self):
        # Add in S8
        print(f"Route set from {data.ADDRESS_FROM} to {data.ADDRESS_TO}")
        pass

    def test_select_plan(self):
        # Add in S8
        print(" function created for select plan ")
        pass

    def test_fill_phone_number(self):
        # Add in S8
        print(f"Phone number filled: {data.PHONE_NUMBER}")
        pass

    def test_fill_card(self):
        # Add in S8
        print(f"Card details filled: Number={data.CARD_NUMBER}, Code={data.CARD_CODE}")
        pass

    def test_comment_for_driver(self):
        # Add in S8
        print(f"Message for driver: {data.MESSAGE_FOR_DRIVER}")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Add in S8
        print("Function created for order blanket and handkerchiefs")
        pass

    def test_order_2_ice_creams(self):
        # Add in S8
        print("Function created for order 2 ice creams")
        for i in range(2):  # Loop iterates twice
            print(i)
        pass

    def test_car_search_model_appears(self):
        # Add in S8
        print("Function created for car search model appears")
        pass

    @classmethod
    def test_setup_class(cls):
        # Add in S8
        # Urban Routes URL from data.py
        url = data.URBAN_ROUTES_URL

        # Check if the server is reachable
        if helpers.is_url_reachable(url):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")
            pass




