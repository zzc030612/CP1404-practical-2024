from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    silverservicetaxi = SilverServiceTaxi("My SilverServiceTaxi", 100, 2)
    silverservicetaxi.drive(18)
    print(silverservicetaxi)
    print(silverservicetaxi.get_fare())


main()