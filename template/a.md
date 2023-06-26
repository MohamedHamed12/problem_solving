# design pattern

- sources
    - GitHub
        
        1-https://gist.github.com/dmmeteo/f630fa04c7a79d3c132b9e9e5d037bfd
        
        2-https://github.com/RefactoringGuru/design-patterns-python/blob/main/src/Singleton/Conceptual/ThreadSafe/main.py
        
        3-https://refactoring.guru/design-patterns/behavioral-patterns
        
        4-https://github.com/faif/python-patterns/blob/master/patterns/creational/prototype.py
        
        ***5-https://github.com/Sean-Bradley/Design-Patterns-In-Python/tree/master*** 
        
    - youtube
        
        1-https://www.youtube.com/@m_reda/playlists
        
        2-
        
    
- solid principle
    - Single Responsibility Principle
        
        
        ```python
        '''
        A class should have only one job.
        If a class has more than one responsibility, it becomes coupled.
        A change to one responsibility results to modification of the other responsibility.
        '''
        
        class Animal:
            def __init__(self, name: str):
                self.name = name
            
            def get_name(self) -> str:
                pass
        
            def save(self, animal: Animal):
                pass
        
        '''
        more one responsibility
        to solve this 
        '''
        
        class Animal:
            def __init__(self, name: str):
                    self.name = name
            
            def get_name(self):
                pass
        
        class AnimalDB:
            def get_animal(self) -> Animal:
                pass
        
            def save(self, animal: Animal):
                pass
        
        '''
        When designing our classes, we should aim to put related features together, 
        so whenever they tend to change they change for the same reason. 
        And we should try to separate features if they will change for different reasons. - Steve Fenton
        '''
        ```
        
    - Open-Closed Principle
        
        ```python
        """
        Open-Closed Principle
        Software entities(Classes, modules, functions) should be open for extension, not modification.
        """
        class Animal:
            def __init__(self, name: str):
                self.name = name
            
            def get_name(self) -> str:
                pass
        
        animals = [
            Animal('lion'),
            Animal('mouse')
        ]
        
        def animal_sound(animals: list):
            for animal in animals:
                if animal.name == 'lion':
                    print('roar')
        
                elif animal.name == 'mouse':
                    print('squeak')
        
        animal_sound(animals)
        
        """
        The function animal_sound does not conform to the open-closed principle because it cannot be closed against new kinds of animals.
        If we add a new animal, Snake, We have to modify the animal_sound function.
        You see, for every new animal, a new logic is added to the animal_sound function. 
        This is quite a simple example. When your application grows and becomes complex, 
        you will see that the if statement would be repeated over and over again 
        in the animal_sound function each time a new animal is added, all over the application.
        """
        
        animals = [
            Animal('lion'),
            Animal('mouse'),
            Animal('snake')
        ]
        
        def animal_sound(animals: list):
            for animal in animals:
                if animal.name == 'lion':
                    print('roar')
                elif animal.name == 'mouse':
                    print('squeak')
                elif animal.name == 'snake':
                    print('hiss')
        
        animal_sound(animals)
        
        """
        How do we make it (the animal_sound) conform to OCP?
        """
        
        class Animal:
            def __init__(self, name: str):
                self.name = name
            
            def get_name(self) -> str:
                pass
        
            def make_sound(self):
                pass
        
        class Lion(Animal):
            def make_sound(self):
                return 'roar'
        
        class Mouse(Animal):
            def make_sound(self):
                return 'squeak'
        
        class Snake(Animal):
            def make_sound(self):
                return 'hiss'
        
        def animal_sound(animals: list):
            for animal in animals:
                print(animal.make_sound())
        
        animal_sound(animals)
        
        """
        Animal now has a virtual method make_sound. We have each animal extend the Animal class and implement the virtual make_sound method.
        Every animal adds its own implementation on how it makes a sound in the make_sound. 
        The animal_sound iterates through the array of animal and just calls its make_sound method.
        Now, if we add a new animal, animal_sound doesn’t need to change. 
        All we need to do is add the new animal to the animal array.
        animal_sound now conforms to the OCP principle.
        """
        
        """
        Another example:
        Let’s imagine you have a store, and you give a discount of 20% to your favorite customers using this class:
        When you decide to offer double the 20% discount to VIP customers. You may modify the class like this:
        """
        
        class Discount:
            def __init__(self, customer, price):
                self.customer = customer
                self.price = price
        
            def give_discount(self):
                    if self.customer == 'fav':
                        return self.price * 0.2
                    if self.customer == 'vip':
                        return self.price * 0.4
        
        """
        No, this fails the OCP principle. OCP forbids it. If we want to give a new percent discount maybe, to a diff. 
        type of customers, you will see that a new logic will be added.
        To make it follow the OCP principle, we will add a new class that will extend the Discount. 
        In this new class, we would implement its new behavior:
        """
        
        class Discount:
            def __init__(self, customer, price):
                self.customer = customer
                self.price = price
        
            def get_discount(self):
                    return self.price * 0.2
        
        class VIPDiscount(Discount):
            def get_discount(self):
                return super().get_discount() * 2
        
        """
        If you decide 80% discount to super VIP customers, it should be like this:
        You see, extension without modification.
        """
        
        class SuperVIPDiscount(VIPDiscount):
            def get_discount(self):
                return super().get_discount() * 2
        ```
        
    - Liskov Substitution Principle
        
        ```python
        """
        Liskov Substitution Principle
        A sub-class must be substitutable for its super-class.
        The aim of this principle is to ascertain that a sub-class can assume the place of its super-class without errors. 
        If the code finds itself checking the type of class then, it must have violated this principle.
        Let’s use our Animal example.
        """
        
        def animal_leg_count(animals: list):
            for animal in animals:
                if isinstance(animal, Lion):
                    print(lion_leg_count(animal))
                elif isinstance(animal, Mouse):
                    print(mouse_leg_count(animal))
                elif isinstance(animal, Pigeon):
                    print(pigeon_leg_count(animal))
                
        animal_leg_count(animals)
        
        """
        To make this function follow the LSP principle, we will follow this LSP requirements postulated by Steve Fenton:
        If the super-class (Animal) has a method that accepts a super-class type (Animal) parameter. 
        Its sub-class(Pigeon) should accept as argument a super-class type (Animal type) or sub-class type(Pigeon type).
        If the super-class returns a super-class type (Animal). 
        Its sub-class should return a super-class type (Animal type) or sub-class type(Pigeon).
        Now, we can re-implement animal_leg_count function:
        """
        
        def animal_leg_count(animals: list):
            for animal in animals:
                print(animal.leg_count())
                
        animal_leg_count(animals)
        
        """
        The animal_leg_count function cares less the type of Animal passed, it just calls the leg_count method. 
        All it knows is that the parameter must be of an Animal type, either the Animal class or its sub-class.
        The Animal class now have to implement/define a leg_count method.
        And its sub-classes have to implement the leg_count method:
        """
        
        class Animal:
            def leg_count(self):
                pass
        
        class Lion(Animal):
            def leg_count(self):
                pass
        
        """
        When it’s passed to the animal_leg_count function, it returns the number of legs a lion has.
        You see, the animal_leg_count doesn’t need to know the type of Animal to return its leg count, 
        it just calls the leg_count method of the Animal type because by contract a sub-class of Animal class must implement the leg_count function.
        """
        ```
        
    - Interface Segregation Principle
        
        ```python
        """
        Interface Segregation Principle
        Make fine grained interfaces that are client specific
        Clients should not be forced to depend upon interfaces that they do not use.
        This principle deals with the disadvantages of implementing big interfaces.
        Let’s look at the below IShape interface:
        """
        
        class IShape:
            def draw_square(self):
                raise NotImplementedError
            
            def draw_rectangle(self):
                raise NotImplementedError
            
            def draw_circle(self):
                raise NotImplementedError
        
        """
        This interface draws squares, circles, rectangles. class Circle, Square or Rectangle implementing the IShape 
        interface must define the methods draw_square(), draw_rectangle(), draw_circle().
        """
        
        class Circle(IShape):
            def draw_square(self):
                pass
        
            def draw_rectangle(self):
                pass
            
            def draw_circle(self):
                pass
        
        class Square(IShape):
            def draw_square(self):
                pass
        
            def draw_rectangle(self):
                pass
            
            def draw_circle(self):
                pass
        
        class Rectangle(IShape):
            def draw_square(self):
                pass
        
            def draw_rectangle(self):
                pass
            
            def draw_circle(self):
                pass
        
        """
        It’s quite funny looking at the code above. class Rectangle implements methods (draw_circle and draw_square) it has no use of, 
        likewise Square implementing draw_circle, and draw_rectangle, and class Circle (draw_square, draw_rectangle).
        If we add another method to the IShape interface, like draw_triangle(),
        """
        
        class IShape:
            def draw_square(self):
                raise NotImplementedError
            
            def draw_rectangle(self):
                raise NotImplementedError
            
            def draw_circle(self):
                raise NotImplementedError
            
            def draw_triangle(self):
                raise NotImplementedError
        
        """
        the classes must implement the new method or error will be thrown.
        We see that it is impossible to implement a shape that can draw a circle but not a rectangle or a square or a triangle. 
        We can just implement the methods to throw an error that shows the operation cannot be performed.
        ISP frowns against the design of this IShape interface. clients (here Rectangle, Circle, and Square) should not be forced to depend on methods that they do not need or use. 
        Also, ISP states that interfaces should perform only one job (just like the SRP principle) any extra grouping of behavior should be abstracted away to another interface.
        Here, our IShape interface performs actions that should be handled independently by other interfaces.
        To make our IShape interface conform to the ISP principle, we segregate the actions to different interfaces.
        Classes (Circle, Rectangle, Square, Triangle, etc) can just inherit from the IShape interface and implement their own draw behavior.
        """
        
        class IShape:
            def draw(self):
                raise NotImplementedError
        
        class Circle(IShape):
            def draw(self):
                pass
        
        class Square(IShape):
            def draw(self):
                pass
        
        class Rectangle(IShape):
            def draw(self):
                pass
        
        """
        We can then use the I -interfaces to create Shape specifics like Semi Circle, Right-Angled Triangle, Equilateral Triangle, Blunt-Edged Rectangle, etc.
        """
        ```
        
    - Dependency Inversion Principle
        
        ```python
        """
        Dependency Inversion Principle
        Dependency should be on abstractions not concretions
        A. High-level modules should not depend upon low-level modules. Both should depend upon abstractions.
        B. Abstractions should not depend on details. Details should depend upon abstractions.
        There comes a point in software development where our app will be largely composed of modules. 
        When this happens, we have to clear things up by using dependency injection. 
        High-level components depending on low-level components to function.
        """
        
        class XMLHttpService(XMLHttpRequestService):
            pass
        
        class Http:
            def __init__(self, xml_http_service: XMLHttpService):
                self.xml_http_service = xml_http_service
            
            def get(self, url: str, options: dict):
                self.xml_http_service.request(url, 'GET')
        
            def post(self, url, options: dict):
                self.xml_http_service.request(url, 'POST')
        
        """
        Here, Http is the high-level component whereas HttpService is the low-level component. 
        This design violates DIP A: High-level modules should not depend on low-level level modules. It should depend upon its abstraction.
        This Http class is forced to depend upon the XMLHttpService class. 
        If we were to change to change the Http connection service, maybe we want to connect to the internet through cURL or even Mock the http service. 
        We will painstakingly have to move through all the instances of Http to edit the code and this violates the OCP principle.
        The Http class should care less the type of Http service you are using. We make a Connection interface:
        """
        
        class Connection:
            def request(self, url: str, options: dict):
                raise NotImplementedError
        
        """
        The Connection interface has a request method. With this, we pass in an argument of type Connection to our Http class:
        """
        
        class Http:
            def __init__(self, http_connection: Connection):
                self.http_connection = http_connection
            
            def get(self, url: str, options: dict):
                self.http_connection.request(url, 'GET')
        
            def post(self, url, options: dict):
                self.http_connection.request(url, 'POST')
        
        """
        So now, no matter the type of Http connection service passed to Http it can easily connect to a network 
        without bothering to know the type of network connection.
        We can now re-implement our XMLHttpService class to implement the Connection interface:
        """
        
        class XMLHttpService(Connection):
            xhr = XMLHttpRequest()
        
            def request(self, url: str, options:dict):
                self.xhr.open()
                self.xhr.send()
        
        """
        We can create many Http Connection types and pass it to our Http class without any fuss about errors.
        """
        class NodeHttpService(Connection):
            def request(self, url: str, options:dict):
                pass
        
        class MockHttpService(Connection):
            def request(self, url: str, options:dict):
                pass
        
        """
        Now, we can see that both high-level modules and low-level modules depend on abstractions. 
        Http class(high level module) depends on the Connection interface(abstraction) and 
        the Http service types(low level modules) in turn, depends on the Connection interface(abstraction).
        Also, this DIP will force us not to violate the Liskov Substitution Principle: 
        The Connection types Node-XML-MockHttpService are substitutable for their parent type Connection.
        """
        ```
        

- Creational Design Patterns
    
    
    - Singleton Design Pattern
        
        ## not safe
        
        - 
        - 
        
        ```python
        """
        EN: Singleton Design Pattern
        
        Intent: Lets you ensure that a class has only one instance, while providing a
        global access point to this instance. One instance per each subclass (if any).
        """
        
        class SingletonMeta(type):
            """
            EN: The Singleton class can be implemented in different ways in Python. Some
            possible methods include: base class, decorator, metaclass. We will use the
            metaclass because it is best suited for this purpose.
            """
        
            _instances = {}
        
            def __call__(cls, *args, **kwargs):
                """
                EN: Possible changes to the value of the `__init__` argument do not
                affect the returned instance.
                """
                if cls not in cls._instances:
                    instance = super().__call__(*args, **kwargs)
                    cls._instances[cls] = instance
                return cls._instances[cls]
        
        class Singleton(metaclass=SingletonMeta):
            def some_business_logic(self):
                """
                EN: Finally, any singleton should define some business logic, which can
                be executed on its instance.
                """
        
                # ...
        
        if __name__ == "__main__":
            # EN: The client code.
            #
            # RU: Клиентский код.
        
            s1 = Singleton()
            s2 = Singleton()
        
            if id(s1) == id(s2):
                print("Singleton works, both variables contain the same instance.")
            else:
                print("Singleton failed, variables contain different instances.")
        ```
        
        - safe
            
            ```python
            """
            EN: Singleton Design Pattern
            
            Intent: Lets you ensure that a class has only one instance, while providing a
            global access point to this instance. One instance per each subclass (if any).
            """
            
            from threading import Lock, Thread
            
            class SingletonMeta(type):
                """
                EN: This is a thread-safe implementation of Singleton.
            
                """
            
                _instances = {}
            
                _lock: Lock = Lock()
                """
                We now have a lock object that will be used to synchronize
                threads during first access to the Singleton.
                """
            
                def __call__(cls, *args, **kwargs):
                    """
                    EN: Possible changes to the value of the `__init__` argument do not
                    affect the returned instance.
                    """
                    # EN: Now, imagine that the program has just been launched.
                    # Since there's no Singleton instance yet, multiple threads can
                    # simultaneously pass the previous conditional and reach this
                    # point almost at the same time. The first of them will acquire
                    # lock and will proceed further, while the rest will wait here.
                    with cls._lock:
                        # EN: The first thread to acquire the lock, reaches this
                        # conditional, goes inside and creates the Singleton
                        # instance. Once it leaves the lock block, a thread that
                        # might have been waiting for the lock release may then
                        # enter this section. But since the Singleton field is
                        # already initialized, the thread won't create a new
                        # object.
                        if cls not in cls._instances:
                            instance = super().__call__(*args, **kwargs)
                            cls._instances[cls] = instance
                    return cls._instances[cls]
            
            class Singleton(metaclass=SingletonMeta):
                value: str = None
                """
                EN: We'll use this property to prove that our Singleton really works.
                """
            
                def __init__(self, value: str) -> None:
                    self.value = value
            
                def some_business_logic(self):
                    """
                    EN: Finally, any singleton should define some business logic, which can
                    be executed on its instance.
                    """
            
            def test_singleton(value: str) -> None:
                singleton = Singleton(value)
                print(singleton.value)
            
            if __name__ == "__main__":
                # EN: The client code.
                
            
                print("If you see the same value, then singleton was reused (yay!)\n"
                      "If you see different values, "
                      "then 2 singletons were created (booo!!)\n\n"
                      "RESULT:\n")
            
                process1 = Thread(target=test_singleton, args=("FOO",))
                process2 = Thread(target=test_singleton, args=("BAR",))
                process1.start()
                process2.start()
            ```
            
    - Prototype
        
        ```python
        """
        *What is this pattern about?
        This patterns aims to reduce the number of classes required by an
        application. Instead of relying on subclasses it creates objects by
        copying a prototypical instance at run-time.
        
        This is useful as it makes it easier to derive new kinds of objects,
        when instances of the class have only a few different combinations of
        state, and when instantiation is expensive.
        
        *What does this example do?
        When the number of prototypes in an application can vary, it can be
        useful to keep a Dispatcher (aka, Registry or Manager). This allows
        clients to query the Dispatcher for a prototype before cloning a new
        instance.
        
        Below provides an example of such Dispatcher, which contains three
        copies of the prototype: 'default', 'objecta' and 'objectb'.
        
        *TL;DR
        Creates new object instances by cloning prototype.
        """
        from __future__ import annotations
        
        from typing import Any
        
        class Prototype:
            def __init__(self, value: str = "default", **attrs: Any) -> None:
                self.value = value
                self.__dict__.update(attrs)
        
            def clone(self, **attrs: Any) -> Prototype:
                """Clone a prototype and update inner attributes dictionary"""
                # Python in Practice, Mark Summerfield
                # copy.deepcopy can be used instead of next line.
                obj = self.__class__(**self.__dict__)
                obj.__dict__.update(attrs)
                return obj
        
        class PrototypeDispatcher:
            def __init__(self):
                self._objects = {}
        
            def get_objects(self) -> dict[str, Prototype]:
                """Get all objects"""
                return self._objects
        
            def register_object(self, name: str, obj: Prototype) -> None:
                """Register an object"""
                self._objects[name] = obj
        
            def unregister_object(self, name: str) -> None:
                """Unregister an object"""
                del self._objects[name]
        
        def main() -> None:
            """
            >>> dispatcher = PrototypeDispatcher()
            >>> prototype = Prototype()
        
            >>> d = prototype.clone()
            >>> a = prototype.clone(value='a-value', category='a')
            >>> b = a.clone(value='b-value', is_checked=True)
            >>> dispatcher.register_object('objecta', a)
            >>> dispatcher.register_object('objectb', b)
            >>> dispatcher.register_object('default', d)
        
            >>> [{n: p.value} for n, p in dispatcher.get_objects().items()]
            [{'objecta': 'a-value'}, {'objectb': 'b-value'}, {'default': 'default'}]
        
            >>> print(b.category, b.is_checked)
            a True
            """
        
        if __name__ == "__main__":
            import doctest
        
            doctest.testmod()
        ```
        
    - ****Factory Pattern****
        
        ```python
        """ What is this pattern about?
        A Factory is an object for creating other objects.
        
        *What does this example do?
        The code shows a way to localize words in two languages: English and
        Greek. "get_localizer" is the factory function that constructs a
        localizer depending on the language chosen. The localizer object will
        be an instance from a different class according to the language
        localized. However, the main code does not have to worry about which
        localizer will be instantiated, since the method "localize" will be called
        in the same way independently of the language.
        
        *Where can the pattern be used practically?
        The Factory Method can be seen in the popular web framework Django:
        https://docs.djangoproject.com/en/4.0/topics/forms/formsets/
        For example, different types of forms are created using a formset_factory
        
        *References:
        http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/
        
        *TL;DR
        Creates objects without having to specify the exact class.
        """
        from typing import Dict
        from typing import Protocol
        from typing import Type
        
        class Localizer(Protocol):
            def localize(self, msg: str) -> str:
                pass
        
        class GreekLocalizer:
            """A simple localizer a la gettext"""
        
            def __init__(self) -> None:
                self.translations = {"dog": "σκύλος", "cat": "γάτα"}
        
            def localize(self, msg: str) -> str:
                """We'll punt if we don't have a translation"""
                return self.translations.get(msg, msg)
        
        class EnglishLocalizer:
            """Simply echoes the message"""
        
            def localize(self, msg: str) -> str:
                return msg
        
        def get_localizer(language: str = "English") -> Localizer:
        
            """Factory"""
            localizers: Dict[str, Type[Localizer]] = {
                "English": EnglishLocalizer,
                "Greek": GreekLocalizer,
            }
        
            return localizers[language]()
        
        def main():
            """
            # Create our localizers
            >>> e, g = get_localizer(language="English"), get_localizer(language="Greek")
        
            # Localize some text
            >>> for msg in "dog parrot cat bear".split():
            ...     print(e.localize(msg), g.localize(msg))
            dog σκύλος
            parrot parrot
            cat γάτα
            bear bear
            """
        
        if __name__ == "__main__":
            import doctest
        
            doctest.testmod()
        ```
        
- structure Design Patterns
    - proxy pattern
        
        ```python
        """
        *What is this pattern about?
        Proxy is used in places where you want to add functionality to a class without
        changing its interface. The main class is called `Real Subject`. A client should
        use the proxy or the real subject without any code change, so both must have the
        same interface. Logging and controlling access to the real subject are some of
        the proxy pattern usages.
        
        *References:
        https://refactoring.guru/design-patterns/proxy/python/example
        https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Fronting.html
        
        *TL;DR
        Add functionality or logic (e.g. logging, caching, authorization) to a resource
        without changing its interface.
        """
        
        from typing import Union
        
        class Subject:
            """
            As mentioned in the document, interfaces of both RealSubject and Proxy should
            be the same, because the client should be able to use RealSubject or Proxy with
            no code change.
        
            Not all times this interface is necessary. The point is the client should be
            able to use RealSubject or Proxy interchangeably with no change in code.
            """
        
            def do_the_job(self, user: str) -> None:
                raise NotImplementedError()
        
        class RealSubject(Subject):
            """
            This is the main job doer. External services like payment gateways can be a
            good example.
            """
        
            def do_the_job(self, user: str) -> None:
                print(f"I am doing the job for {user}")
        
        class Proxy(Subject):
            def __init__(self) -> None:
                self._real_subject = RealSubject()
        
            def do_the_job(self, user: str) -> None:
                """
                logging and controlling access are some examples of proxy usages.
                """
        
                print(f"[log] Doing the job for {user} is requested.")
        
                if user == "admin":
                    self._real_subject.do_the_job(user)
                else:
                    print("[log] I can do the job just for `admins`.")
        
        def client(job_doer: Union[RealSubject, Proxy], user: str) -> None:
            job_doer.do_the_job(user)
        
        def main():
            """
            >>> proxy = Proxy()
        
            >>> real_subject = RealSubject()
        
            >>> client(proxy, 'admin')
            [log] Doing the job for admin is requested.
            I am doing the job for admin
        
            >>> client(proxy, 'anonymous')
            [log] Doing the job for anonymous is requested.
            [log] I can do the job just for `admins`.
        
            >>> client(real_subject, 'admin')
            I am doing the job for admin
        
            >>> client(real_subject, 'anonymous')
            I am doing the job for anonymous
            """
        
        if __name__ == "__main__":
            import doctest
        
            doctest.testmod()
        #***************************************************************
        # pylint: disable=too-few-public-methods
        # pylint: disable=arguments-differ
        "A Proxy Concept Example"
        
        from abc import ABCMeta, abstractmethod
        
        class ISubject(metaclass=ABCMeta):
            "An interface implemented by both the Proxy and Real Subject"
            @staticmethod
            @abstractmethod
            def request():
                "A method to implement"
        
        class RealSubject(ISubject):
            "The actual real object that the proxy is representing"
        
            def __init__(self):
                # hypothetically enormous amounts of data
                self.enormous_data = [1, 2, 3]
        
            def request(self):
                return self.enormous_data
        
        class Proxy(ISubject):
            """
            The proxy. In this case the proxy will act as a cache for
            `enormous_data` and only populate the enormous_data when it
            is actually necessary
            """
        
            def __init__(self):
                self.enormous_data = []
                self.real_subject = RealSubject()
        
            def request(self):
                """
                Using the proxy as a cache, and loading data into it only if
                it is needed
                """
                if not self.enormous_data:
                    print("pulling data from RealSubject")
                    self.enormous_data = self.real_subject.request()
                    return self.enormous_data
                print("pulling data from Proxy cache")
                return self.enormous_data
        
        # The Client
        SUBJECT = Proxy()
        # use SUBJECT
        print(id(SUBJECT))
        # load the enormous amounts of data because now we want to show it.
        print(SUBJECT.request())
        # show the data again, but this time it retrieves it from the local cache
        print(SUBJECT.request())
        
        ```
        
    - Decorator pattern
        
        ```python
        """
        *What is this pattern about?
        The Decorator pattern is used to dynamically add a new feature to an
        object without changing its implementation. It differs from
        inheritance because the new feature is added only to that particular
        object, not to the entire subclass.
        
        *What does this example do?
        This example shows a way to add formatting options (boldface and
        italic) to a text by appending the corresponding tags (<b> and
        <i>). Also, we can see that decorators can be applied one after the other,
        since the original text is passed to the bold wrapper, which in turn
        is passed to the italic wrapper.
        
        *Where is the pattern used practically?
        The Grok framework uses decorators to add functionalities to methods,
        like permissions or subscription to an event:
        http://grok.zope.org/doc/current/reference/decorators.html
        
        *References:
        https://sourcemaking.com/design_patterns/decorator
        
        *TL;DR
        Adds behaviour to object without affecting its class.
        """
        
        class TextTag:
            """Represents a base text tag"""
        
            def __init__(self, text: str) -> None:
                self._text = text
        
            def render(self) -> str:
                return self._text
        
        class BoldWrapper(TextTag):
            """Wraps a tag in <b>"""
        
            def __init__(self, wrapped: TextTag) -> None:
                self._wrapped = wrapped
        
            def render(self) -> str:
                return f"<b>{self._wrapped.render()}</b>"
        
        class ItalicWrapper(TextTag):
            """Wraps a tag in <i>"""
        
            def __init__(self, wrapped: TextTag) -> None:
                self._wrapped = wrapped
        
            def render(self) -> str:
                return f"<i>{self._wrapped.render()}</i>"
        
        def main():
            """
            >>> simple_hello = TextTag("hello, world!")
            >>> special_hello = ItalicWrapper(BoldWrapper(simple_hello))
        
            >>> print("before:", simple_hello.render())
            before: hello, world!
        
            >>> print("after:", special_hello.render())
            after: <i><b>hello, world!</b></i>
            """
        
        if __name__ == "__main__":
            import doctest
        
            doctest.testmod()
        ```
        
    - Adapter pattern
        
        ```python
        """
        *What is this pattern about?
        The Adapter pattern provides a different interface for a class. We can
        think about it as a cable adapter that allows you to charge a phone
        somewhere that has outlets in a different shape. Following this idea,
        the Adapter pattern is useful to integrate classes that couldn't be
        integrated due to their incompatible interfaces.
        
        *What does this example do?
        
        The example has classes that represent entities (Dog, Cat, Human, Car)
        that make different noises. The Adapter class provides a different
        interface to the original methods that make such noises. So the
        original interfaces (e.g., bark and meow) are available under a
        different name: make_noise.
        
        *Where is the pattern used practically?
        The Grok framework uses adapters to make objects work with a
        particular API without modifying the objects themselves:
        http://grok.zope.org/doc/current/grok_overview.html#adapters
        
        *References:
        http://ginstrom.com/scribbles/2008/11/06/generic-adapter-class-in-python/
        https://sourcemaking.com/design_patterns/adapter
        http://python-3-patterns-idioms-test.readthedocs.io/en/latest/ChangeInterface.html#adapter
        
        *TL;DR
        Allows the interface of an existing class to be used as another interface.
        """
        v# Target Interface
        class MediaPlayer:
            def play(self, filename):
                pass
        
        # Adaptee
        class LegacyPlayer:
            def start(self, file):
                print(f"LegacyPlayer: Playing {file}")
        
        # Adapter
        class MediaPlayerAdapter(MediaPlayer):
            def __init__(self, legacy_player):
                self.legacy_player = legacy_player
        
            def play(self, filename):
                print("Adapter: Converting MediaPlayer play() to LegacyPlayer start()")
                self.legacy_player.start(filename)
        
        # Client
        def client_code(media_player):
            media_player.play("movie.mp4")
        
        # Usage
        legacy_player = LegacyPlayer()
        adapter = MediaPlayerAdapter(legacy_player)
        client_code(adapter)
        
        #-------------------------------------------------------------------
        from typing import Callable, TypeVar
        
        T = TypeVar("T")
        
        class Dog:
            def __init__(self) -> None:
                self.name = "Dog"
        
            def bark(self) -> str:
                return "woof!"
        
        class Cat:
            def __init__(self) -> None:
                self.name = "Cat"
        
            def meow(self) -> str:
                return "meow!"
        
        class Human:
            def __init__(self) -> None:
                self.name = "Human"
        
            def speak(self) -> str:
                return "'hello'"
        
        class Car:
            def __init__(self) -> None:
                self.name = "Car"
        
            def make_noise(self, octane_level: int) -> str:
                return f"vroom{'!' * octane_level}"
        
        class Adapter:
            """Adapts an object by replacing methods.
        
            Usage
            ------
            dog = Dog()
            dog = Adapter(dog, make_noise=dog.bark)
            """
        
            def __init__(self, obj: T, **adapted_methods: Callable):
                """We set the adapted methods in the object's dict."""
                self.obj = obj
                self.__dict__.update(adapted_methods)
        
            def __getattr__(self, attr):
                """All non-adapted calls are passed to the object."""
                return getattr(self.obj, attr)
        
            def original_dict(self):
                """Print original object dict."""
                return self.obj.__dict__
        
        def main():
            """
            >>> objects = []
            >>> dog = Dog()
            >>> print(dog.__dict__)
            {'name': 'Dog'}
        
            >>> objects.append(Adapter(dog, make_noise=dog.bark))
        
            >>> objects[0].__dict__['obj'], objects[0].__dict__['make_noise']
            (<...Dog object at 0x...>, <bound method Dog.bark of <...Dog object at 0x...>>)
        
            >>> print(objects[0].original_dict())
            {'name': 'Dog'}
        
            >>> cat = Cat()
            >>> objects.append(Adapter(cat, make_noise=cat.meow))
            >>> human = Human()
            >>> objects.append(Adapter(human, make_noise=human.speak))
            >>> car = Car()
            >>> objects.append(Adapter(car, make_noise=lambda: car.make_noise(3)))
        
            >>> for obj in objects:
            ...    print("A {0} goes {1}".format(obj.name, obj.make_noise()))
            A Dog goes woof!
            A Cat goes meow!
            A Human goes 'hello'
            A Car goes vroom!!!
            """
        
        if __name__ == "__main__":
            import doctest
        
            doctest.testmod(optionflags=doctest.ELLIPSIS)
        '''
        __getattr__ special method. This method is part of Python's attribute lookup mechanism and is invoked when
         an attribute is not found in the usual way.
        __getattr__ method is defined within a class. This class acts as an adapter or wrapper for another object 
        (self.obj). When an attribute is accessed on an instance of this class and the attribute is not found,
         the __getattr__ method is called.
        
        The purpose of this __getattr__ implementation is to forward any non-adapted attribute calls to the underlying
         object (self.obj). It uses the getattr function to retrieve the attribute from self.obj. Essentially,
         this method allows the adapter class to transparently pass through attribute access to the wrapped object.
        '''
        ```
        
    - Facade pattern
        
        ```python
        """
        Example from https://en.wikipedia.org/wiki/Facade_pattern#Python
        
        *What is this pattern about?
        The Facade pattern is a way to provide a simpler unified interface to
        a more complex system. It provides an easier way to access functions
        of the underlying system by providing a single entry point.
        This kind of abstraction is seen in many real life situations. For
        example, we can turn on a computer by just pressing a button, but in
        fact there are many procedures and operations done when that happens
        (e.g., loading programs from disk to memory). In this case, the button
        serves as an unified interface to all the underlying procedures to
        turn on a computer.
        
        *Where is the pattern used practically?
        This pattern can be seen in the Python standard library when we use
        the isdir function. Although a user simply uses this function to know
        whether a path refers to a directory, the system makes a few
        operations and calls other modules (e.g., os.stat) to give the result.
        
        *References:
        https://sourcemaking.com/design_patterns/facade
        https://fkromer.github.io/python-pattern-references/design/#facade
        http://python-3-patterns-idioms-test.readthedocs.io/en/latest/ChangeInterface.html#facade
        
        *TL;DR
        Provides a simpler unified interface to a complex system.
        """
        
        # Complex computer parts
        class CPU:
            """
            Simple CPU representation.
            """
        
            def freeze(self) -> None:
                print("Freezing processor.")
        
            def jump(self, position: str) -> None:
                print("Jumping to:", position)
        
            def execute(self) -> None:
                print("Executing.")
        
        class Memory:
            """
            Simple memory representation.
            """
        
            def load(self, position: str, data: str) -> None:
                print(f"Loading from {position} data: '{data}'.")
        
        class SolidStateDrive:
            """
            Simple solid state drive representation.
            """
        
            def read(self, lba: str, size: str) -> str:
                return f"Some data from sector {lba} with size {size}"
        
        class ComputerFacade:
            """
            Represents a facade for various computer parts.
            """
        
            def __init__(self):
                self.cpu = CPU()
                self.memory = Memory()
                self.ssd = SolidStateDrive()
        
            def start(self):
                self.cpu.freeze()
                self.memory.load("0x00", self.ssd.read("100", "1024"))
                self.cpu.jump("0x00")
                self.cpu.execute()
        
        def main():
            """
            >>> computer_facade = ComputerFacade()
            >>> computer_facade.start()
            Freezing processor.
            Loading from 0x00 data: 'Some data from sector 100 with size 1024'.
            Jumping to: 0x00
            Executing.
            """
        
        if __name__ == "__main__":
            import doctest
        
            doctest.testmod(optionflags=doctest.ELLIPSIS)
        ```
        
    - flyweight pattern
        
        ```python
        """
        *What is this pattern about?
        This pattern aims to minimize the number of objects that are needed by
        a program at run-time. A Flyweight is an object shared by multiple
        contexts and is indistinguishable from an object that is not shared.
        
        The state of a Flyweight should not be affected by its context, this
        is known as its intrinsic state. The decoupling of the object's state
        from the object's context, allows the Flyweight to be shared.
        
        *What does this example do?
        The example below sets up an 'object pool' which stores initialised
        objects. When a 'Card' is created it first checks to see if it already
        exists instead of creating a new one. This aims to reduce the number of
        objects initialised by the program.
        
        *References:
        http://codesnipers.com/?q=python-flyweights
        https://python-patterns.guide/gang-of-four/flyweight/
        
        *Examples in Python ecosystem:
        https://docs.python.org/3/library/sys.html#sys.intern
        
        *TL;DR
        Minimizes memory usage by sharing data with other similar objects.
        """
        
        import weakref
        
        class Card:
            """The Flyweight"""
        
            # Could be a simple dict.
            # With WeakValueDictionary garbage collection can reclaim the object
            # when there are no other references to it.
            _pool: weakref.WeakValueDictionary = weakref.WeakValueDictionary()
        
            def __new__(cls, value, suit):
                # If the object exists in the pool - just return it
                obj = cls._pool.get(value + suit)
                # otherwise - create new one (and add it to the pool)
                if obj is None:
                    obj = object.__new__(Card)
                    cls._pool[value + suit] = obj
                    # This row does the part we usually see in `__init__`
                    obj.value, obj.suit = value, suit
                return obj
        
            # If you uncomment `__init__` and comment-out `__new__` -
            #   Card becomes normal (non-flyweight).
            # def __init__(self, value, suit):
            #     self.value, self.suit = value, suit
        
            def __repr__(self):
                return f"<Card: {self.value}{self.suit}>"
        
        def main():
            """
            >>> c1 = Card('9', 'h')
            >>> c2 = Card('9', 'h')
            >>> c1, c2
            (<Card: 9h>, <Card: 9h>)
            >>> c1 == c2
            True
            >>> c1 is c2
            True
        
            >>> c1.new_attr = 'temp'
            >>> c3 = Card('9', 'h')
            >>> hasattr(c3, 'new_attr')
            True
        
            >>> Card._pool.clear()
            >>> c4 = Card('9', 'h')
            >>> hasattr(c4, 'new_attr')
            False
            """
        
        if __name__ == "__main__":
            import doctest
        
            doctest.testmod()flyweight.py
        #--------------------------------------------------------------------------------------------------
        # pylint: disable=too-few-public-methods
        "The Flyweight Concept"
        
        class IFlyweight():
            "Nothing to implement"
        
        class Flyweight(IFlyweight):
            "The Concrete Flyweight"
        
            def __init__(self, code: str) -> None:
                self.code = code
        
        class FlyweightFactory():
            "Creating the FlyweightFactory as a singleton"
        
            _flyweights: dict[str, Flyweight] = {}  # Python 3.9
            # _flyweights = {}  # Python 3.8 or earlier
        
            def __new__(cls):
                return cls
        
            @classmethod
            def get_flyweight(cls, code: str) -> Flyweight:
                "A static method to get a flyweight based on a code"
                if not code in cls._flyweights:
                    cls._flyweights[code] = Flyweight(code)
                return cls._flyweights[code]
        
            @classmethod
            def get_count(cls) -> int:
                "Return the number of flyweights in the cache"
                return len(cls._flyweights)
        
        class Context():
            """
            An example context that holds references to the flyweights in a
            particular order and converts the code to an ascii letter
            """
        
            def __init__(self, codes: str) -> None:
                self.codes = list(codes)
        
            def output(self):
                "The context specific output that uses flyweights"
                ret = ""
                for code in self.codes:
                    ret = ret + FlyweightFactory.get_flyweight(code).code
                return ret
        
        # The Client
        CONTEXT = Context("abracadabra")
        
        # use flyweights in a context
        print(CONTEXT.output())
        
        print(f"abracadabra has {len('abracadabra')} letters")
        print(f"FlyweightFactory has {FlyweightFactory.get_count()} flyweights")
        ```
        
- behavior Design Patterns
