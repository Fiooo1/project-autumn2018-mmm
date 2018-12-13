from http.server import HTTPServer, BaseHTTPRequestHandler
from get_json import get_json_file

class GenReqId:
	_ID = 0
	def next():
		GenReqId._ID = GenReqId._ID + 1
		return GenReqId._ID

def get_json(taskFile):
	rheaders, rdata = get_request("get_json", taskFile)
	return rdata

class TexHTTPRequestHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		request, reqID, conLen = self.headers["request"], self.headers["reqID"], self.headers["Content-Length"]
		print("Request =", request, reqID)
		data = self.rfile.read(int(conLen))
		print(str(data))
		if request == "get_tex":
			self.send_response(200)
			self.send_header("response", "get_tex")
			self.send_header("resID", reqID)
			self.send_header("Content-Type", "text/tex;charset=utf-8")
			self.end_headers()
			print("ATTENTION!")
			wdata = get_json_file(data).encode()
			print("\nWDATA =", str(wdata))
			self.wfile.write(wdata)

serv = HTTPServer(("127.0.0.1", 25600), TexHTTPRequestHandler)
print("Tex start")
serv.serve_forever()
