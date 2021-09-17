import time
import pyscreeze
import flask
import io


def capture_screen_as_compression():
    img = pyscreeze.screenshot()
    vfp = io.BytesIO()
    img.save(vfp, format='JPEG')
    return vfp.getvalue()


def route_all(app, config):
    @app.route('/api/v0/stream')
    def stream_screen():
        multipart_boundary = 'compressed-screen'

        def stream_image():
            while True:
                try:
                    img = capture_screen_as_compression()
                    yield bytes(f'--{multipart_boundary}\r\n',
                                encoding='utf-8') + b'Content-Type: image/jpeg\r\n\r\n' + img + b'\r\n'
                    time.sleep(0.1)
                except OSError:
                    yield bytes(f'--{multipart_boundary}\r\nContent-Type: text/plain\r\n\r\nOn Error\r\n',
                                encoding='utf-8')
                    yield bytes(f'--{multipart_boundary}--', encoding='utf-8')
                    return

        return flask.Response(stream_image(), mimetype=f'multipart/x-mixed-replace; boundary={multipart_boundary}')

    @app.route('/')
    def index_page():
        resp = flask.make_response(flask.render_template('index.html', title=config.title))
        resp.headers.add('Set-Cookie', 'cross-site-cookie=bar; SameSite=None; Secure')
        return resp
