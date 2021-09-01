#!/usr/bin/env python
import time
import rospkg, rospy
import serial 

from flexbe_core import EventState, Logger
from flexbe_core.proxy import ProxyServiceCaller

from strategy.srv import wifi_srv


class ServiceBell(EventState):
    """
    Publishes a number from receive_board so that it can let robot know which table to go.

    -- port                   string           which port you used
    -- baud                   int              which baud you used

    <= done								       program close.
    <= fail							    	   receive_board not work.

    """
	
    def __init__(self, port, baud):
        """Constructor"""
        super(ServiceBell, self).__init__(outcomes=['done', 'fail'])
        self.port_name  = port
        self.BAUD_RATES = baud
        self.list_ser = []

        self.wifi_service = 'wifi_module'
        self.wifi_client = ProxyServiceCaller({self.wifi_service: wifi_srv})

        self.ser = serial.Serial(self.port_name, self.BAUD_RATES) 

    def execute(self, userdata):
        # if not self.wifi_client.is_available(self.wifi_service):
        #     return 'fail'

        while not rospy.is_shutdown():

            while self.ser.in_waiting:          
                self.list_ser.append(self.ser.read(1))
            
            if len(self.list_ser) >= 3:
                if self.list_ser[0] == 's' and self.list_ser[2] == 'e':
                    print(self.list_ser)
                    table_num = str(ord(self.list_ser[1]))

                    try:
                        res = self.wifi_client.call(self.wifi_service, table_num)
                    except rospy.ServiceException as e:
                        print ("Service call failed: %s" % e)

                    del self.list_ser [:]
                    
                else:
                    del self.list_ser [:]
           
        self.ser.close()    
        print('good bye!')
        return 'finish'

    def on_enter(self, userdata):
        time.sleep(0.2)

    def on_stop(self):
        return super().on_stop()