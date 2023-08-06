import abc


class Publisher(metaclass=abc.ABCMeta):
    @property
    @abc.abstractmethod
    def triggerable_messages(self):
        pass

    @property
    def subscribers(self):
        if not hasattr(self, "_subscribers"):
            self._subscribers = {}

        return self._subscribers

    def attach(self, subscriber, message):
        if message not in self.triggerable_messages:
            raise ValueError(
                "Message '{}' not in triggerable_messages.".format(message)
            )

        if not isinstance(subscriber, Subscriber):
        	raise ValueError(
        		"{} is not of type subscriber but of type {}.".format(
        			subscriber, type(subscriber)
        		)
        	)

        self.subscribers.setdefault(message, set()).add(subscriber)

    def detach(self, subscriber, message):
        self.subscribers.setdefault(message, set()).discard(subscriber)

    def trigger(self, message, arg=None):
        subscribers = self.subscribers.setdefault(message, set())
        _ = [sub.on_message(message, arg) for sub in subscribers]


class Subscriber(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def on_message(self, message, arg):
        pass


if __name__ == "__main__":
    class DummyPublisher(Publisher):
        @property
        def triggerable_messages(self):
            return ["test"]

    class DummySubscriber(Subscriber):
        def on_message(self, message, arg):
            print(message)
            print(arg)

    pub = DummyPublisher()
    sub = DummySubscriber()

    pub.attach(sub, "test")
    pub.trigger("test", "Hello")
    pub.detach(sub, "test")
    pub.trigger("test", "World")

    try:
    	pub.attach(sub, "not in messages")
    except Exception as e:
    	print(e)
    	pass

    try:
    	pub.attach("TOTO", "test")
    except Exception as e:
    	print(e)
    	pass
