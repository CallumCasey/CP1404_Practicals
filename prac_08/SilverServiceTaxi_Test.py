from Prac_08.SilverServiceTaxi import SilverServiceTaxi

def main():
    my_silver_service_taxi = SilverServiceTaxi("Silver Service Taxi", 100, 2)
    my_silver_service_taxi.drive(18)
    print(my_silver_service_taxi)
    print("Your fare is:", my_silver_service_taxi.get_fare())


main()

