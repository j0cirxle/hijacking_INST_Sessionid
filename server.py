import asyncio
import websockets

async def echo(websocket, path):
    try:
        async for message in websocket:
            if message == "ping":
                print(">>> Ping received")
                continue

            if message == "Test send":
                print("Test send")
                await websocket.send("Test send")
            else:
                print(f"Received message: {message}")
                await websocket.send(f"Echo: {message}")

    except websockets.exceptions.ConnectionClosedError as e:
        print(f"Connection closed unexpectedly: {e}")
    except Exception as e:
        print(f"Unhandled error in echo: {e}")

async def main():
    async with websockets.serve(echo, "yourIP", 8765):
        print(' ######  ###  ##   #####   ######## '+'\n'+'   ##     ### ##  ##   ##  ## ## ## ' + '\n' +'   ##     ######  ##          ##    ' +'\n'+'   ##     ## ###   #####      ##    '+'\n'+'   ##     ##  ##       ##     ##    '+'\n'+'   ##     ##  ##  ##   ##     ##' + '\n' +'######  ###  ##   #####     ####')
        for i in range(11):
            print("\r/ loading "+str(i*10) +'%', end="")
            await asyncio.sleep(0.3)
            print("\r-- loading "+str(i*10) +'%', end="")
            await asyncio.sleep(0.3)
            print("\r| loading "+str(i*10) +'%', end="")
            await asyncio.sleep(0.3)
        print("\n Server started on ws://yourIP")
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
