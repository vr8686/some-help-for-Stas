""" #3
from components.base import Base

class LeftFilter(Base):
    def __init__(self, driver):
        super().__init__(driver)"""

#4
from components.base import Base

class LeftFilter(Base):
    LOCATOR = "//*"

    def __init__(self, driver):
        super().__init__(driver)

    def select_option(self, option, visible=False):
        super().select_option(option, visible)
        print(self.LOCATOR)
