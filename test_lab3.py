import unittest
import AirportVehicleTracker as av
class TestVehicleCreation(unittest.TestCase):

    def test_light_plane(self):
        plane = av.LightPlane(10, 5, 3, 100)
        self.assertEqual(plane.type, "Лёгкий самолёт")
        self.assertEqual(plane.category, "Летательный аппарат")
        self.assertEqual(plane.fuel_volume, 10)

    def test_cargo_plane(self):
        plane = av.CargoPlane(20, 3, 2, 50, 25.5)
        self.assertEqual(plane.type, "Грузовой самолёт")
        self.assertEqual(plane.cargo_weight, 25.5)

    def test_passenger_plane(self):
        plane = av.PassengerPlane(30, 6, 3, 150, 80, 75)
        self.assertEqual(plane.seats, 80)
        self.assertEqual(plane.passengers, 75)

    def test_light_helicopter(self):
        heli = av.LightHelicopter(15, 7, 3, 90)
        self.assertEqual(heli.type, "Лёгкий вертолет")

    def test_attack_helicopter(self):
        heli = av.AttackHelicopter(25, 4, 1, 60, 4)
        self.assertEqual(heli.rockets, 4)

    def test_fighter(self):
        fighter = av.Fighter(18, 5, 2, 80, 6)
        self.assertEqual(fighter.type, "Истребитель")
        self.assertEqual(fighter.rockets, 6)

    def test_tanker(self):
        tanker = av.Tanker(40, 2, 1, 70, 0, 120, "Заправлен")
        self.assertEqual(tanker.required_position, 120)
        self.assertEqual(tanker.gas_station, "Заправлен")

    def test_bus(self):
        bus = av.Bus(22, 45, 30, 25, 60)
        self.assertEqual(bus.passengers, 25)
        self.assertEqual(bus.required_position, 60)

class TestVehicleGeneration(unittest.TestCase):

    def test_generate_vehicle_returns_vehicle(self):
        for cls in av.vehicles_classes:
            with self.subTest(cls=cls):
                v = av.generate_vehicle(cls)
                self.assertIsInstance(v, av.Vehicle)
                self.assertTrue(hasattr(v, 'fuel_volume'))
                self.assertTrue(hasattr(v, 'location'))

    def test_generate_vehicles_list_length(self):
        av.generate_vehicles()
        self.assertEqual(len(av.vehicles_list), 20)
        self.assertTrue(all(isinstance(v, av.Vehicle) for v in av.vehicles_list))

if __name__ == '__main__':
    unittest.main()