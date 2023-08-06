'''
Created on Dec 27, 2019

@author: VINAY
'''
from math import pi
# to find the angle between hours and minutes hand or mintues and seconds hand
def angle(hr,mn,sc):
    '''
    claculation of 1 complete rotation of hours hand multiplied by hour
    so if the hours are 12 then it rotates full 360 degrees
    '''
    aoh=(2*180*hr)/12
    '''
    claculation of 1 complete rotation of minutes hand mulitiplied by minutes
    if minutes are 60 then it rotates full 360 degrees
    '''
    aom=(2*180*mn)/60
    '''
    similary with seconds hand
    '''
    aos=(2*180*sc)/60
    '''
    now we calculate the extra distance travelled by minutes hand for x secs
    '''
    dom=(30*sc)/60
    '''
    similary the extra distance travalled by hours hand in x minutes is given by
    '''
    doh=(30*mn)/60
    '''
    the distance between hours and minutes hand is given by
    the ditsance covered by hours hand from rest - mintues hand from rest + exxtra distance travalled by
    hours hand in x minutes
    '''
    abhm=abs((aoh+doh)-aom)
    '''
    the distance between hours and minutes hand is given by
    the ditsance covered by mintues hand from rest - seconds hand from rest + exxtra distance travalled by
    mintues hand in x seconds
    '''
    abms=abs((aom+dom)-aos)

    '''
    in order to calculate the shortest angle if use 360 minus of angle to get with in 180 degrees
    '''
    if abhm>180:
        abhm=abs(360-abhm)
    if abms>180:
        abms=abs(360-abms)

    '''
    print the result using .format
    '''
    print("angle btw hrs hand and min hand is {} degees ".format(abhm))
    print("angle btw mintues and seconds hand is {} degree".format(abms))

angle(9,45,1)
