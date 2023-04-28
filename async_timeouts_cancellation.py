import asyncio


async def long_running_task():
    try:
        await asyncio.sleep(10)
        print("Task completed")
    except asyncio.CancelledError:
        print("Task canceled")


async def main():
    task = asyncio.create_task(long_running_task())

    try:
        await asyncio.wait_for(task, timeout=3)
    except asyncio.TimeoutError:
        print("Timeout reached, canceling task")
        task.cancel()
        await task


asyncio.run(main())
