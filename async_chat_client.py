import asyncio


async def send_message(writer):
    while True:
        message = input("Enter message: ")
        writer.write(message.encode())
        await writer.drain()


async def receive_message(reader):
    while True:
        data = await reader.read(100)
        if not data:
            print("Connection closed.")
            break
        print(data.decode())


async def main():
    reader, writer = await asyncio.open_connection("localhost", 12345)

    try:
        await asyncio.gather(send_message(writer), receive_message(reader))
    finally:
        writer.close()
        await writer.wait_closed()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Client stopped.")
