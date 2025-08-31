class Validator:
    """A data descriptor that enforces type & range on attribute set,
    and transparently returns the stored value on get."""
    def __init__(self, name, typ, min_=None, max_=None):
        self.name = name              # attribute name on the instance
        self.typ = typ
        self.min = min_
        self.max = max_

    def __set_name__(self, owner, name):
        # If not given explicitly, learn our attribute name from the class body
        if self.name is None:
            self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            # Accessed via the class (e.g., MyClass.attr) -> return the descriptor itself
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.typ):
            raise TypeError(f"{self.name} must be {self.typ.__name__}, got {type(value).__name__}")
        if self.min is not None and value < self.min:
            raise ValueError(f"{self.name} must be ≥ {self.min}")
        if self.max is not None and value > self.max:
            raise ValueError(f"{self.name} must be ≤ {self.max}")
        instance.__dict__[self.name] = value

class Account:
    # Two *data descriptors* that enforce constraints on assignment
    balance = Validator("balance", typ=float, min_=0.0)
    rate    = Validator("rate",    typ=float, min_=0.0, max_=1.0)

    def __init__(self, balance, rate):
        self.balance = float(balance)  # triggers Validator.__set__
        self.rate = float(rate)

    @property
    def yearly_interest(self):
        # Normal @property is also a descriptor under the hood (non-data)
        return self.balance * self.rate

a = Account(1000.0, 0.05)
print(a.yearly_interest)   # 50.0
a.balance = 1500.0         # OK
try:
    a.rate = 2.0           # ValueError: rate must be ≤ 1.0
except Exception as e:
    print(type(e).__name__, e)



# First access computes value = func(instance), stores it on instance.__dict__[name], and returns it.
# Subsequent gets return the stored value without recomputing.
# Bonus: add an invalidate(instance) helper to clear the cache.

