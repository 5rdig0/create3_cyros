# Copyright 2021 iRobot Corporation. All Rights Reserved.

import rclpy
import sys
from create3_procedures.dodge import dodge_procedure as dp

def main(args=None):
    rclpy.init(args=args)
    cp = dp.ColorPalette()
    '''
    DANCE SEQUENCE is defined as a list of pairs with 
    (time to start action in seconds, action to take)
    '''
    global sequence
    sequence = float(0.0)

    def move(m): 
        global sequence
        Max_speed = float(0.306)
        t = float(abs(m/Max_speed))
        m = float(m/abs(m))
        sequence = float(sequence + t)
        return((sequence - t, dp.Move(Max_speed*m,0.0)))

    def rotate(o): 
        global sequence
        Max_angular_speed = float(146.1)
        t = float(abs(o/Max_angular_speed))
        o = float(o/abs(o))
        sequence = float(sequence + t)
        return((sequence - t, dp.Move(0.0,Max_angular_speed*o)))

    DANCE_SEQUENCE = [
        rotate(-90.0),
        (sequence, dp.FinishedDance())
        ]
    
    dance_publisher = None
    try: 
        dance_choreographer = dp.DanceChoreographer(DANCE_SEQUENCE)
        dance_publisher = dp.DanceCommandPublisher(dance_choreographer)
        rclpy.spin(dance_publisher)
    except dp.FinishedDance:
        print('Finished dodge')
    except KeyboardInterrupt:
        print('Caught keyboard interrupt')
    except BaseException:
        print('Exception in dance:', file=sys.stderr)
    finally:
        # Destroy the node explicitly
        # (optional - otherwise it will be done automatically
        # when the garbage collector destroys the node object)
        if dance_publisher:
            dance_publisher.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
