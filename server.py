from aiohttp import web

async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.type == web.WSMsgType.TEXT:
            # Эхо обратно
            await ws.send_str(msg.data)
        elif msg.type == web.WSMsgType.ERROR:
            print('ws connection closed with exception %s' % ws.exception())

    return ws

app = web.Application()
app.add_routes([web.get('/', websocket_handler)])

if __name__ == '__main__':
    web.run_app(app, port=int(os.environ.get('PORT', 8080)))