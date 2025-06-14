import unittest
from builder import OfficePCBuilder, GamingPCBuilder, ServerPCBuilder
from facade import ComputerOrderFacade
from order import OrderManager

class TestBuilder(unittest.TestCase):
    def test_office_builder_cpu(self):
        """Перевірка, що OfficePCBuilder додає CPU Intel i3"""
        b = OfficePCBuilder()
        b.reset(); b.add_cpu()
        self.assertIn("Intel i3", b.get_result().list_parts())

    def test_office_builder_gpu(self):
        """Перевірка, що OfficePCBuilder додає інтегровану відеокарту"""
        b = OfficePCBuilder()
        b.reset(); b.add_gpu()
        self.assertIn("Integrated GPU", b.get_result().list_parts())

    def test_office_builder_ram(self):
        """Перевірка, що OfficePCBuilder додає 8GB оперативної пам’яті"""
        b = OfficePCBuilder()
        b.reset(); b.add_ram()
        self.assertIn("8GB RAM", b.get_result().list_parts())

    def test_gaming_builder_cpu(self):
        """Перевірка, що GamingPCBuilder додає CPU Intel i9"""
        b = GamingPCBuilder()
        b.reset(); b.add_cpu()
        self.assertIn("Intel i9", b.get_result().list_parts())

    def test_gaming_builder_gpu(self):
        """Перевірка, що GamingPCBuilder додає NVIDIA RTX 4080"""
        b = GamingPCBuilder()
        b.reset(); b.add_gpu()
        self.assertIn("NVIDIA RTX 4080", b.get_result().list_parts())

    def test_gaming_builder_ram(self):
        """Перевірка, що GamingPCBuilder додає 32GB оперативної пам’яті"""
        b = GamingPCBuilder()
        b.reset(); b.add_ram()
        self.assertIn("32GB RAM", b.get_result().list_parts())

    def test_server_builder_cpu(self):
        """Перевірка, що ServerPCBuilder додає CPU AMD EPYC"""
        b = ServerPCBuilder()
        b.reset(); b.add_cpu()
        self.assertIn("AMD EPYC", b.get_result().list_parts())

    def test_server_builder_gpu(self):
        """Перевірка, що ServerPCBuilder додає GPU None (відсутній)"""
        b = ServerPCBuilder()
        b.reset(); b.add_gpu()
        self.assertIn("None", b.get_result().list_parts())

    def test_server_builder_ram(self):
        """Перевірка, що ServerPCBuilder додає 64GB ECC RAM"""
        b = ServerPCBuilder()
        b.reset(); b.add_ram()
        self.assertIn("64GB ECC RAM", b.get_result().list_parts())

    def test_builder_parts_count(self):
        """Перевірка, що GamingPCBuilder додає рівно 3 частини"""
        b = GamingPCBuilder()
        b.reset()
        b.add_cpu()
        b.add_gpu()
        b.add_ram()
        parts = b.get_result().list_parts()
        self.assertEqual(len(parts), 3)

class TestFacade(unittest.TestCase):
    def setUp(self):
        """Ініціалізація фасаду перед кожним тестом"""
        self.facade = ComputerOrderFacade()

    def test_facade_office(self):
        """Перевірка, що фасад створює Office комп’ютер з правильними частинами"""
        comp = self.facade.create_computer("office")
        parts = comp.list_parts()
        self.assertIn("Intel i3", parts)
        self.assertIn("Integrated GPU", parts)
        self.assertIn("8GB RAM", parts)

    def test_facade_gaming(self):
        """Перевірка, що фасад створює Gaming комп’ютер з правильними частинами"""
        comp = self.facade.create_computer("gaming")
        parts = comp.list_parts()
        self.assertIn("Intel i9", parts)
        self.assertIn("NVIDIA RTX 4080", parts)
        self.assertIn("32GB RAM", parts)

    def test_facade_server(self):
        """Перевірка, що фасад створює Server комп’ютер з правильними частинами"""
        comp = self.facade.create_computer("server")
        parts = comp.list_parts()
        self.assertIn("AMD EPYC", parts)
        self.assertIn("None", parts)
        self.assertIn("64GB ECC RAM", parts)

    def test_facade_invalid_type(self):
        """Перевірка, що фасад кидає ValueError для невідомого типу комп’ютера"""
        with self.assertRaises(ValueError):
            self.facade.create_computer("supercomputer") 

class TestOrderManager(unittest.TestCase):
    def setUp(self):
        """Ініціалізація менеджера замовлень перед кожним тестом"""
        self.manager = OrderManager()

    def test_create_order_office(self):
        """Перевірка створення офісного комп’ютера через менеджер замовлень"""
        comp = self.manager.create_order("office")
        self.assertIn("Intel i3", comp.list_parts())

    def test_create_order_gaming(self):
        """Перевірка створення ігрового комп’ютера через менеджер замовлень"""
        comp = self.manager.create_order("gaming")
        self.assertIn("NVIDIA RTX 4080", comp.list_parts())

    def test_create_order_server(self):
        """Перевірка створення серверного комп’ютера через менеджер замовлень"""
        comp = self.manager.create_order("server")
        self.assertIn("64GB ECC RAM", comp.list_parts())

    def test_order_list_length(self):
        """Перевірка кількості замовлень після створення кількох комп’ютерів"""
        self.manager.create_order("office")
        self.manager.create_order("gaming")
        self.assertEqual(len(self.manager.orders), 2)

    def test_list_orders_returns_parts_lists(self):
        """Перевірка, що метод list_orders повертає список списків частин комп’ютерів"""
        self.manager.create_order("office")
        orders_parts = self.manager.list_orders()
        self.assertIsInstance(orders_parts, list)
        self.assertIsInstance(orders_parts[0], list)

    def test_create_order_invalid_type_raises(self):
        """Перевірка, що створення замовлення з невідомим типом кидає ValueError"""
        with self.assertRaises(ValueError):
            self.manager.create_order("quantum")

if __name__ == '__main__':
    unittest.main()
