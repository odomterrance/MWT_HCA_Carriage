import gclib


def main():
    g = gclib.py()  # make an instance of the gclib python class

class CarriageFunctions:
    g = gclib.py()  # make an instance of the gclib python class

    try:
        print('gclib version:', g.GVersion())  # prints installed gclib version

        ###########################################################################
        # Connection Utilities
        ###########################################################################
        # Get Ethernet controllers requesting IP addresses
        print('Listening for controllers requesting IP addresses...')
        ip_requests = g.GIpRequests()
        for device_id in ip_requests.keys():
            print(device_id, 'at mac', ip_requests[device_id])

        # device_ips = {'DMC4000-783': '192.168.0.42', 'DMC4103-9998': '192.168.0.43'}  # map hardware to ip addresses

        # for device_id in device_ips.keys():
        #     if device_id in ip_requests:  # if our controller needs an IP
        #         print("\nAssigning", device_ips[device_id], "to", ip_requests[device_id])
        #         g.GAssign(device_ips[device_id], ip_requests[device_id])  # send the mapping
        #         g.GOpen(device_ips[device_id])  # connect to it
        #         print(g.GInfo())
        #         g.GCommand('BN')  # burn the IP
        #         g.GClose()  # disconnect

        print('\nAvailable addresses:')  # print ready connections
        available = g.GAddresses()
        for a in sorted(available.keys()):
            print(a, available[a])

        print('\n')

        ###########################################################################
        #  Connect
        ###########################################################################
        # g.GOpen('192.168.0.42 -s ALL')
        g.GOpen('COM1')  # change to COM port used by carriage
        print(g.GInfo())  # prints connection information for carriage

        ###########################################################################
        # Carriage Attributes
        ###########################################################################
        # c = g.GCommand  # alias the command callable
        # c('SHA')  # servo x-axis ("A")  # sets servo motor A to x-axis
        # c('SHB')  # servo y-axis ("B")  # sets servo motor B to y-axis
        # c('SHC')  # servo z-axis ("C")  # sets servo motor C to z-axis
        # c('SPA=2000')  # x-axis speed, 2000 cts/sec
        # # c('SPB=1500')  # y-axis speed, 1500 cts/sec
        # # c('SPC=300')  # z-axis speed, 300 cts/sec
        # c('ACA=1024')  # x-axis acceleration, 1024 cts/sec
        # # c('ACB=1024')  # y-axis acceleration, 1024 cts/sec
        # # c('ACC=1024')  # z-axis acceleration, 1024 cts/sec
        # c('DCA=1024')  # x-axis deceleration, 1024 cts/sec
        # # c('DCB=1024')  # y-axis deceleration, 1024 cts/sec
        # # c('DCC=1024')  # z-axis deceleration, 1024 cts/sec
        # c('KPA=2')  # x-axis proportional Kp, 2
        # # c('KPB=4')  # y-axis proportional Kp, 4
        # # c('KPC=4')  # z-axis proportional Kp, 4
        # c('KIA=0.008')  # x-axis integral Ki, 0.008
        # # c('KIB=0.024')  # y-axis integral Ki, 0.024
        # # c('KIC=0.008')  # z-axis integral Ki, 0.008
        # c('KDA=500')  # x-axis derivative Kd, 500
        # # c('KDB=100')  # y-axis derivative Kd, 100
        # # c('KDC=1000')  # z-axis derivative Kd, 1000

        ###########################################################################
        # Callable Functions
        ###########################################################################
        # immediately aborts motion of all motors
        # def abort_motion():
        #     c = g.GCommand  # alias the command callable
        #     c('AB')  # abort motion and program
        #     del c  # delete the alias
        #
        # turns off all motors and ends carriage communication
        # def motors_off():
        #     c = g.GCommand  # alias the command callable
        #     c('MO')  # turn off all motors
        #     del c  # delete the alias
        #
        # sets speed attribute of focused motor
        # def set_speed(axis):
        #     c = g.GCommand  # alias the command callable
        #     c('SPA=2000')  # x-axis speed, 2000 cts/sec
        #     del c  # delete the alias
        #
        # sets acceleration attribute of focused motor
        # def set_accel(axis):
        #     c = g.GCommand  # alias the command callable
        #     c('ACA=1024')  # x-axis acceleration, 1024 cts/sec
        #     del c  # delete the alias
        #
        # sets deceleration attribute of focused motor
        # def set_decel(axis):
        #     c = g.GCommand  # alias the command callable
        #     c('DCA=1024')  # x-axis deceleration, 1024 cts/sec
        #     del c  # delete the alias
        #
        # sets proportional attribute of focused motor
        # def set_proportional(axis):
        #     # proportional: SV minus MV, "how far", positive or negative
        #     # proportional: provides rapid response to controller error
        #     c = g.GCommand  # alias the command callable
        #     c('KPA=2')  # x-axis proportional Kp, 2
        #     del c  # delete the alias
        #
        # sets integral attribute of focused motor
        # def set_integral(axis):
        #     # integral: the longer MV is not at SV, the harder it will try to get there, "how long" and "how far"
        #     # integral: eliminates offset but increases rolling behavior of set point
        #     c = g.GCommand  # alias the command callable
        #     c('KIA=0.008')  # x-axis integral Ki, 0.008
        #     del c  # delete the alias
        #
        # sets derivative attribute of focused motor
        # def set_derivative(axis):
        #     # derivative: slope/rate of change, controls overshoots, "how fast", always positive, units of time
        #     # derivative: works to decrease oscillations in set point, especially when set point is moving
        #     c = g.GCommand  # alias the command callable
        #     c('KDA=500')  # x-axis derivative Kd, 500
        #     del c  # delete the alias
        #
        # moves focused axis to user-input set point
        # def move_axis(axis, set_point):
        #     c = g.GCommand  # alias the command callable
        #     sp = c(set_point)  # relative position move in x-axis ("A"), 1000 cts
        #     print(' Starting move...')
        #     c('BGA')  # begin motion in x-axis ("A")
        #     g.GMotionComplete('A')
        #     print(' done.')
        #     del c  # delete the alias

    ###########################################################################
    # except handler
    ###########################################################################
    except gclib.GclibError as e:
        print('Unexpected GclibError:', e)

    finally:
        g.GClose()  # don't forget to close connections!

    # return


# runs main() if carriage_movement.py called from the console
# if __name__ == '__main__':
#     main()
if __name__ == "__main__":
    CarriageFunctions()
