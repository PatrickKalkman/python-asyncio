import asyncio


async def async_operation():
    await asyncio.sleep(1)
    return 42


async def main():
    loop = asyncio.get_event_loop()
    future = loop.create_future()

    async def set_future_result():
        result = await async_operation()
        future.set_result(result)

    await asyncio.gather(set_future_result(), future)

    print(f"Future result: {future.result()}")


asyncio.run(main())
