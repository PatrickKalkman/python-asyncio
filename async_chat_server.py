import asyncio


async def handle_client(reader, writer):
    addr = writer.get_extra_info("peername")
    print(f"New connection from {addr}")

    while True:
        message = await reader.read(100)
        if not message:
            print(f"Connection closed with {addr}")
            break

        print(f"Received message from {addr}: {message.decode()}")
        writer.write(f"Echo: {message.decode()}".encode())
        await writer.drain()


async def main():
    server = await asyncio.start_server(handle_client, "localhost", 12345)
    addr = server.sockets[0].getsockname()
    print(f"Serving on {addr}")

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Server stopped.")
