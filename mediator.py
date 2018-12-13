from http.server import HTTPServer, BaseHTTPRequestHandler
from http.client import HTTPConnection

class GenReqId:
	_ID = 0
	def next():
		GenReqId._ID = GenReqId._ID + 1
		return GenReqId._ID

class Hosts:
	def set_hosts(*hosts):
		Hosts.Interface, Hosts.Facade, Hosts.Tex, Hosts.DataBase = hosts

def get_request(host, req, data=None, **addhead):
	connection = HTTPConnection(host)
	reqID = GenReqId.next()
	if (data != None):
		conLen = len(data)
	else:
		conLen = 0
	head = {"request": req, "reqID": reqID, "Content-Length": conLen}
	head.update(addhead)
	print("REQ HEAD =", head)
	print("REQ BODY =", data)
	connection.request("GET", '/', headers=head, body=data)
	response = connection.getresponse()
	connection.close()
	return response.getheaders(), response.read()

def get_taskList():
	rheaders, rdata = get_request(Hosts.Facade, "get_taskList")
	return rdata

def get_task_Facade(task):
	rheaders, rdata = get_request(Hosts.Facade, "get_task", taskID=task)
	return rdata

def get_Tex(taskFile):
	print("in get_Tex taskFile = ", str(taskFile))
	rheaders, rdata = get_request(Hosts.Tex, "get_tex", data=taskFile)
	return rdata

class MediatorHTTPRequestHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		request, reqID = self.headers["request"], self.headers["reqID"]
		print("Request from", self.client_address)
		print("Request =", request, reqID)
		#TODO check Fasade & Tex is runing
		if request == "get_taskList":
			taskList = get_taskList()
			self.send_response(200)
			self.send_header("response", "get_taskList")
			self.send_header("resID", reqID)
			self.end_headers()
			self.wfile.write(taskList)
		if request == "get_task":
			taskID = self.headers["taskID"]
			print("taskID = ", taskID)
			#TODO request from database
			taskFile = get_task_Facade(taskID)
			print("taskFile = ", taskFile)
			texFile = get_Tex(taskFile)
			self.send_response(200)
			self.send_header("response", "get_task")
			self.send_header("resID", reqID)
			self.send_header("Content-Type", "text/tex;charset=utf-8")
			self.end_headers()
			self.wfile.write(texFile)

serv = HTTPServer(("127.0.0.1", 25700), MediatorHTTPRequestHandler)
Hosts.set_hosts("127.0.0.1:25000", "127.0.0.1:25500", "127.0.0.1:25600", "127.0.0.1:25000")
print("Mediator start")
serv.serve_forever()