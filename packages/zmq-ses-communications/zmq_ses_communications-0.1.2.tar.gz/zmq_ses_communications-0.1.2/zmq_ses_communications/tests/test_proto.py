from msgs.command_pb2 import CommandRequest

testDeviceRequst = CommandRequest()
testDeviceRequst.request = "test"
testDeviceRequst.command_id = 1
testDeviceRequst.action = "sdosm"

print(testDeviceRequst.IsInitialized())
print(testDeviceRequst)
print(testDeviceRequst.action)
print(testDeviceRequst.SerializeToString())

