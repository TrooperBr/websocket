import asyncio
import websockets


connection = set()


async def _server( websocket, path):
	connection.add(websocket)
	try:
		async for message in websocket:
			await websocket.send(f'Got your msg its: {message}')
	finally:
		#unregister
		connection.remove(websocket)

url = 'localhost'
port = 8765
webserver = websockets.server(_server, url, port)

asyncio.get_event_loop().run_until_complete(self.webserver)
asyncio.get_event_loop().run_forever()