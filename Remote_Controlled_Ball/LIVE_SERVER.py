import asyncio
from websockets.asyncio.server import serve

DEVICES = set()

async def middle_man(sock):
	DEVICES.add(sock)
	ip = sock.remote_address
	print(f"@SERVER: Connection Established with {ip}")
	
	try:
		async for cmd in sock:
			for device in DEVICES:
				if device != sock:
					try:
						print(cmd)
						await device.send(cmd)
					except Exception:
						DEVICES.discard(device)
					
	except Exception as exet:
		print("@SERVER_ERROR: ", exet)
		
	finally:
	   DEVICES.discard(sock)
	   print("@SERVER_UPDATE: Connection Closed and Terminated")
		
async def main():
    print("@SERVER_STATUS: Running On Port [8080] | Active")
    async with serve(middle_man, "0.0.0.0", 8080) as server:
        await server.serve_forever()

asyncio.run(main())