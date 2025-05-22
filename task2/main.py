from command_centre import CommandCentre
from aircraft import Aircraft
from runway import Runway


def main():
    command_centre = CommandCentre()

    runway = Runway("A1")
    command_centre.set_runway(runway)

    aircraft1 = Aircraft("Flight 101", command_centre)
    aircraft2 = Aircraft("Flight 202", command_centre)

    aircraft1.request_landing()
    aircraft2.request_landing()


if __name__ == "__main__":
    main()
