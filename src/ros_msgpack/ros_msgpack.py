
from turtlesim.msg import Color
from sensor_msgs.msg import JointState

def adding(a,b):
    return(a+b)

def square(a):
    b = a*a
    return(b)

class Multiply():
    def __init__(self):
        self.a = 100
    def two(self,n):
        return(2*n)
    def three(self,n):
        return(3*n)
    def four(self,n):
        return(4*n)


class Encode():
    def __init__(self):
        pass

    def Color(self, data):
        ser = {}
        ser['r'] = data.r
        ser['g'] = data.g
        ser['b'] = data.b
        return(ser)

    def JointState(self, data):
        ser = {}
        ser['seq'] = data.header.seq
        ser['secs'] = data.header.stamp.secs
        ser['nsecs'] = data.header.stamp.nsecs
        ser['frame_id'] = data.header.frame_id
        ser['name'] = data.name
        ser['position'] = data.position
        ser['velocity'] = data.velocity
        ser['effort'] = data.effort
        return(ser)


class Decode():
    def __init__(self):
        pass

    def Color(self, ser):
        color = Color()
        color.r = ser['r']
        color.g = ser['g']
        color.b = ser['b']
        return(color)

    def JointState(self, ser):
        js = JointState()
        js.header.seq = ser['seq']
        js.header.stamp.secs = ser['secs']
        js.header.stamp.nsecs = ser['nsecs']
        js.header.frame_id = ser['frame_id']
        js.name = ser['name']
        js.position = ser['position']
        js.velocity = ser['velocity']
        js.effort = ser['effort']
        return(js)
