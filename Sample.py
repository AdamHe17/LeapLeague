import Leap, sys, thread, time, keyoutput
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
from keyoutput import PressKey, VK_Q, VK_W, VK_E, VK_R, AltTab


class SampleListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']

    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"

        controller.set_policy_flags(Leap.Controller.POLICY_BACKGROUND_FRAMES);

        # Enable gestures
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        controller.config.set("Gesture.KeyTap.MinDownVelocity", 10.0)
        controller.config.set("Gesture.KeyTap.HistorySeconds", .2)
        controller.config.set("Gesture.KeyTap.MinDistance", 5.0)
        controller.config.save()

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print "Disconnected"


    def on_exit(self, controller):
        print "Exited"

    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        frame = controller.frame()
        # Get gestures
        for gesture in frame.gestures():
            if gesture.type == Leap.Gesture.TYPE_KEY_TAP:
                keytap = KeyTapGesture(gesture)
                tapper = keytap.pointable
                finger = Leap.Finger(tapper)
                tap_id = finger.type
                if finger.type == 1:
                    PressKey(VK_R)
                elif finger.type == 2:
                    PressKey(VK_E)
                elif finger.type == 3:
                    PressKey(VK_W)
                elif finger.type == 4:
                    PressKey(VK_Q)
                time.sleep(.2)
                print "  Key Tap id: %d, %s, position: %s, direction: %s" % (
                        finger.type, self.state_names[gesture.state],
                        keytap.position, keytap.direction )
                return

    def state_string(self, state):
        if state == Leap.Gesture.STATE_START:
            return "STATE_START"

        if state == Leap.Gesture.STATE_UPDATE:
            return "STATE_UPDATE"

        if state == Leap.Gesture.STATE_STOP:
            return "STATE_STOP"

        if state == Leap.Gesture.STATE_INVALID:
            return "STATE_INVALID"

def main():
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()
