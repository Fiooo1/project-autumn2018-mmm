from common import AMQP_client
import json

class InterfaceClient(AMQP_client):
	def parse(self, Id, Type, Data):
		if Type == "post_taskList":
			print("Task list:", Data)
		if Type == "get_task":
			
			self.send("facade", 2, "get_task", {"task_id": Data, "args": ""})
		if Type == "post_task":
			with open("out.json", "w") as fout:
				fout.write(str(json.loads(Data)))
			print("See out.json")

Client = InterfaceClient("localhost", "interface")
Client.start_consume()
print("At this time must run Django web-server")
Client.send("facade", 1, "get_taskList")
try:
	while True:
		pass
except KeyboardInterrupt:
	Client.stop_consume()
	print("Close connection & stop thread")