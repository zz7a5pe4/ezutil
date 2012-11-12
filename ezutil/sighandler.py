#!/usr/bin/python                                  
#############################################################
# Script: sighandler.py                                      
# Description:                                               
#   Demonstrate generic polymorphism example of how to setup and
#   handle implemented signals through python.                  
#                                                               
# Author: Cody Lane                                             
# Date: 12-4-2009                                               
#############################################################   

import signal
import sys   
import os    

class SignalHandler:
    '''             
    This class is used to handle and trap a signal and associate
    it back to a python callable object. When a new SignalHandler
    object is created you must call the register() method to register
    the signal and callback.  See register() for details.            

    This superclass has an abstract method called 'handler' which
    should be defined in a sub-class.                            

    This class is a super class for SigAction. SigAction is the 
    class that performs the signal event handling.              
    '''                                                         
    SIGNALS = ()                                                
                                                                
    def register(self, signum, callback):                       
        '''                                                     
        Registers a new signal handler action object (SigAction) 
        for trapping a signal and then calling a python object.  

        When this method is called it also updates the static SIGNALS
        tuple appending the new SigAction class.  To get this tuple  
        see getActions().                                            

        @param signum: int -> Should be signal int.  Ex: signal.SIGTERM
        @param callback: pythonObj -> Should be python object.  Ex: somemethod
            NOTE: Don't put () around your callback function or the function  
                  will be called when the callback is initialized..           
        '''                                                                   
        self.SIGNALS += (SigAction(signum, callback), )                       

    def getActions(self):
        '''              
        Return a tuple of defined signal actions if any.  If defined, 
        the tuple will contain SigAction instances.                   
        '''                                                           
        return self.SIGNALS                                           

    def handler(self, signum, frame):
        '''                          
        Abstract method, which must be defined when sub-classing.
        If the method is not defined, an AssertionError will be raised.
        '''                                                            
        assert 0, "You must define a handler(signum, frame) method in %s" %(self)

    def __repr__(self):
        '''            
        Custom string method when printing the class object.  
            Example:                                          
                >>> print self                                
                <Class: SignalHandler>                        
        '''                                                   
        return "<Class:%s>" %(self.__class__.__name__)        

class SigAction(SignalHandler):
    '''                        
    This class defines how a signal should be traped and what do when
    a signal trap occurs.  This class should NOT be instantiated because
    the superclass SignalHandler will setup and create a SigAction object
    when the SignalHandler.register() method is called.                  

    '''
    def __init__(self, signum, callback):
        '''                              
        Create a SigAction object.  Also setup the signal trap.

        @param signum: int -> Should be signal int.  Ex: signal.SIGTERM
        @param callback: pythonObj -> Should be python object.  Ex: somemethod
            NOTE: Don't put () around your callback function or the function  
                  will be called when the callback is initialized..           
        '''                                                                   
        self.signum = signum                                                  
        self.callback = callback                                              
        signal.signal(self.signum, self.handler)                              

    def handler(self, signum, frame):
        '''                          
        Overrides the superclass definition so that each new signal performs
        it's own action.                                                    

        NOTE: You do not have to pass arguments to this method. See help(signal)
        for details.                                                            
        '''
        self.callback()

    def __repr__(self):
        '''
        Custom string message when class object is printed.

        Example:
            >>> print self
            <Class:SigAction signal:15>
        '''
        return "<Class:%s signal:%s>" %(self.__class__.__name__, self.signum)

def stop():
    print "Called the stop().... Exitting 0"
    sys.exit(0)

def abort():
    print "Called abort().... Exitting 1"
    sys.exit(1)

if __name__ == '__main__':
    # Create SignalHandler object
    sighandler = SignalHandler()

    # Now register a SIGTERM (kill -15) and callback
    # object when signal is trapped.
    sighandler.register( signal.SIGTERM, stop)

    # Register a SIGINT (kill -2) and callback
    # object when sign is trapped.
    # This is equivalent to CTRL-C
    sighandler.register( signal.SIGINT, abort )

    # Display the current registered signal events.
    # This is just for show and tell purposes.
    print "Implemented Signals: ", sighandler.getActions()

    while True:
        print "Waiting for signal.... Running pid: %s" %(os.getpid())
        signal.pause()

