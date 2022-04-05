from abc import * # 추상클래스를 위해 반드시 import

# 추상클래스를 생성한다.
class DeliveryStore(metaclass=ABCMeta):
	# 추상메소드
	@abstractmethod
	def set_order_list(self, order_list):
		pass

	@abstractmethod
	def get_total_price(self):
		pass

class Food:
	def __init__(self, name, price):
		self.name = name
		self.price = price

# class 자식클래스(부모클래스)
class PizzaStore(DeliveryStore):
	def __init__(self):
		menu_names = ["Cheese", "Potato", "Shrimp", "Pineapple", "Meatball"]
		menu_prices = [11100, 12600, 13300, 21000, 19500];
		self.menu_list = []
		for i in range(5):
			self.menu_list.append(Food(menu_names[i], menu_prices[i]))

		self.order_list = []

	# 부모클래스 DeliveryStore의 추상메소드 구현
	def set_order_list(self, order_list):
		for order in order_list:
			self.order_list.append(order)

	def get_total_price(self):
		total_price = 0
		for order in self.order_list:
			for menu in self.menu_list:
				if order == menu.name:
					total_price += menu.price
		return total_price 

def solution(order_list):
	'''
	추상클래스는 미구현 추상메소드를 한개 이상 가지는 클래스로 자식클래스에서 해당 추상메소드를 반드시 구현하도록 강제한다.
	그 방법으로 추상메소드를 구현하지 않아도 import 시에는 에러가 없으나, 객체를 생성할 때 에러가 발생한다.
	
	TypeError: Can't instantiate abstract class @@@ with abstract method @@@

	추상메소드를 생략하면, 클래스 기능을 한다.(객체도 생성가능)
	'''
	delivery_store = PizzaStore()

	delivery_store.set_order_list(order_list)
	total_price = delivery_store.get_total_price()
	return total_price