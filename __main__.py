import asyncio
import websockets




class Server:
	"""docstring for Server"""
	def __init__(self, url='localhost', port=123):
		super(Server, self).__init__()
		self.connection = set()
		self.url = url
		self.port = port
		self.webserver = websockets.serve(self._server, url, port)

		#loop =
		self.run()

	def run(self):
		print(f'Running a websocket server on {self.url}:{self.port}')
		asyncio.get_event_loop().run_until_complete(self.webserver)
		asyncio.get_event_loop().run_forever()

	async def _server(self, websocket, path):
		self.connection.add(websocket)
		try:
			async for message in websocket:
				print(message)
				await websocket.send(f'Got your msg its: {message}')
		finally:
			#unregister
			self.connection.remove(websocket)
	

if __name__ == "__main__":
	Server(url='localhost', port=8765)