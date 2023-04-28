import asyncio
import aiosqlite


async def create_table(db_name):
    async with aiosqlite.connect(db_name) as db:
        cursor = await db.cursor()
        await cursor.execute(
            """CREATE TABLE IF NOT EXISTS users
        (id INTEGER PRIMARY KEY, name TEXT);"""
        )
        await db.commit()


async def add_user(db_name, name):
    async with aiosqlite.connect(db_name) as db:
        cursor = await db.cursor()
        await cursor.execute("INSERT INTO users (name) VALUES (?);", (name,))
        await db.commit()


async def get_users(db_name):
    async with aiosqlite.connect(db_name) as db:
        cursor = await db.cursor()
        await cursor.execute("SELECT * FROM users;")
        users = await cursor.fetchall()
        return users


async def main():
    db_name = "./db/example.db"
    await create_table(db_name)

    users = ["Alice", "Bob", "Charlie"]
    tasks = [add_user(db_name, user) for user in users]
    await asyncio.gather(*tasks)

    fetched_users = await get_users(db_name)
    print("Users in the database:")
    for user in fetched_users:
        print(f"ID: {user[0]}, Name: {user[1]}")


if __name__ == "__main__":
    asyncio.run(main())
