import asyncio
import flatbuffers
import demo
import aiosmf
from demo.demo_service_smf_client import SmfStorageClient
import demo.Request


async def main():
    conn = await aiosmf.create_connection("127.0.0.1:20776")
    client = SmfStorageClient(conn)

    # build an rpc request buffer
    builder = flatbuffers.Builder(32)
    key = builder.CreateString("my.key")
    demo.Request.RequestStart(builder)
    demo.Request.RequestAddName(builder, key)
    put = demo.Request.RequestEnd(builder)
    builder.Finish(put)
    buf = builder.Output()

    resp, status = await client.Get(buf)
    print(resp.Name(), status)

    conn.close()
    await conn.wait_closed()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
