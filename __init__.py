import time

from modules.core.props import Property, StepProperty
from modules.core.step import StepBase
from modules import cbpi

@cbpi.step
class TwoKettleLogic(StepBase):
    '''
    Just put the decorator @cbpi.step on top of a method. The class name must be unique in the system
    '''
    # Properties
    kettle1 = StepProperty.Kettle("Kettle")
    temp1 = Property.Number("Temperature", configurable=True)
    kettle2 = StepProperty.Kettle("Kettle")
    temp2 = Property.Number("Temperature", configurable=True)

    def init(self):
        '''
        Initialize Step. This method is called once at the beginning of the step
        :return: 
        '''
        # set target tep
        self.set_target_temp(self.temp1, self.kettle1)
        self.set_target_temp(self.temp2, self.kettle2)
        

    def finish(self):
        pass
    

    def execute(self):
        '''
        This method is execute in an interval
        :return: 
        '''

        # Check if Target Temp is reached for both kettles
        if self.get_kettle_temp(self.kettle1) >= int(self.temp1) and self.get_kettle_temp(self.kettle2) >= int(self.temp2):
            self.notify("Kettle Temps Reached!", "Starting the next step.", timeout=None)
            self.next()